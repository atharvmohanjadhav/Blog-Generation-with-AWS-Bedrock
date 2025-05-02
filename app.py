import boto3    # it is used to invoke the foundation model
import botocore.config
import json
from datetime import datetime
import os
from dotenv import load_dotenv


def blog_generate_bedrock(topic:str)->str:
    prompt = f"""
    <s>[INST]Human: Write a 175 words blog on a topic {topic}
    Assistant:[/INST] 
    """
    body = {
        "prompt":prompt,
        "max_gen_len":512,
        "temperature":0.5,
        "top_p":0.9
    }

    try:
        bedrock_client = boto3.client("bedrock-runtime",region_name="us-east-1",
                        config = botocore.config.Config(read_timeout = 300,retries={"max_attempts":3}))
        response = bedrock_client.invoke_model(body=json.dumps(body),modelId="meta.llama3-8b-instruct-v1:0")
        res = response.get("body").read()
        res_data = json.loads(res)
        print(res_data)
        blog_details = res_data['generation']
        return blog_details

    except Exception as e:
        print(f"Error occured {e}")
        return ""

def save_blog_in_s3(s3_key,s3_bucket_name,generate_blog):
    s3 = boto3.client("s3")
    try:
        s3.put_object(Bucket=s3_bucket_name,Key = s3_key,Body = generate_blog)
        print("code saved in s3 bucket!")
    except Exception as e:
        print(f"Error occured {e}")
        return ""

    
def lambda_handler(event, context):
    # TODO implement
    event = json.loads(event["body"])
    blog_topic = event['blog_topic']

    generate_blog = blog_generate_bedrock(topic=blog_topic)

    if generate_blog:
        load_dotenv()
        s3_bucket_name = os.getenv("S3_BUCKET_NAME")
        curr_time = datetime.now().strftime("%H%M%S")
        s3_key = f"blog-op/{curr_time}.txt"
        s3_bucket_name = os.getenv("S3_BUCKET_NAME")

        save_blog_in_s3(s3_key=s3_key,s3_bucket_name=s3_bucket_name,generate_blog=generate_blog)
    else:
        print("no blog was generated!")
    return {
        "status_code":200,
        "body":json.dumps("Blog generated successfully!")
    }

