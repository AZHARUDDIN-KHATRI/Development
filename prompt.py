from openai import OpenAI

client = OpenAI()

prompt = input("Enter your prompt: ")

response = client.responses.create(
    model="gpt-6",
    input=prompt
)

print(response.output_text)