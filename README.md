# 📝 Blog Generation with AWS Bedrock (GenAI Project)

This project demonstrates how to generate AI-powered blog content using Amazon Bedrock's foundation models through an AWS Lambda function, integrated with API Gateway and S3.

---

## 🚀 Project Overview

The system accepts a blog topic via an API call, uses a selected foundation model (like Meta Llama 3) from Amazon Bedrock to generate a ~175-word blog, and then stores the generated content in an S3 bucket.

---

## 🛠️ Technologies Used

- **AWS Lambda**
- **Amazon Bedrock (Llama 3 Model)**
- **API Gateway**
- **Amazon S3**
- **boto3 (Python SDK for AWS)**

---

## 🔧 Steps Followed

1. **Create Lambda Function**  
   Develop a Lambda function to interact with the Bedrock API and generate blog content.

2. **Select a Foundation Model**  
   Use a specific foundation model (e.g., `meta.llama3-8b-instruct-v1:0`) available in Bedrock.

3. **Write Lambda Code**  
   Logic includes:
   - Generating blog using Bedrock
   - Storing it in S3
   - Logging responses and errors

4. **Prepare Dependencies**  
   Create a `python` folder, install the `boto3` library into it, and zip it.

5. **Create a Lambda Layer**  
   Upload the zipped `python` folder as a layer to allow Lambda access to `boto3`.

6. **Set Up API Gateway**  
   Create a new API that connects to the Lambda function.

7. **Create Stages in API Gateway**  
   Define stages like `dev` or `prod` to manage deployments.

8. **Deploy API URL**  
   Use the generated API Gateway URL to trigger the Lambda function from external clients.

9. **Create S3 Bucket**  
   Store the generated blog posts as `.txt` files in a specified S3 bucket.

---

## 📦 Sample API Input

```json
{
  "blog_topic": "The Future of AI in Education"
}
