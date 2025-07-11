import boto3
import json

# Create a Bedrock Runtime client
client = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

# Replace with your chosen model ID
model_id = "anthropic.claude-instant-v1"

# Example document to summarize
document_text = """
Cloud computing allows businesses to rent computing power instead of buying physical servers.
It provides scalability, flexibility, and cost efficiency.
However, it requires careful planning around security, architecture, and cost management.
"""

# Prompt for summarization
prompt = f"""
Human: Summarize the following document in 2-3 sentences:

{document_text}

Assistant:
"""

# Payload for Bedrock
payload = {
    "prompt": prompt,
    "max_tokens_to_sample": 200,
    "temperature": 0.3,
}

# Call Bedrock
response = client.invoke_model(
    modelId=model_id,
    contentType="application/json",
    accept="application/json",
    body=json.dumps(payload),
)

# Parse and print result
response_body = json.loads(response['body'])
completion_text = response_body.get("completion", "")

print("Summary:")
print(completion_text.strip())