import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

def get_gpt_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can choose other models like text-curie-001, etc.
            prompt=prompt,
            max_tokens=150  # Adjust based on the desired length of the response
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# Example usage
prompt = "What is the capital of France?"
response = get_gpt_response(prompt)
print("Response from GPT:")
print(response)
