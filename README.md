# AWS Bedrock Beginner Demo

✅ Summarize documents into shorter text  

---

## ✨ What is AWS Bedrock?

AWS Bedrock is a managed service for accessing powerful foundation models (FMs) like:

- Anthropic Claude
- AI21 Jurassic
- Amazon Titan

Instead of training your own large models, you simply send prompts via the Bedrock API.

---

## 🛠️ Prerequisites

✅ AWS Account  
✅ AWS CLI configured with credentials for Bedrock  
✅ Python 3.9+  
✅ Boto3 SDK

If you’ve never configured the AWS CLI, see:

👉 [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

---

## ⚙️ Installation

Clone this repo:


git clone https://github.com/YOUR_USERNAME/aws-bedrock-beginner.git
cd aws-bedrock-beginner

Install dependencies:

```
pip install -r requirements.txt
```

💻 How to Run

Summarize a Document
Run the summarization example:

```
python bedrock_demo/bedrock_summarize.py
```

Sample output:

Summary:
Cloud computing lets businesses rent resources instead of owning servers, offering flexibility and cost savings, but requiring careful planning for security and cost management.
(Responses vary by model and settings.)


