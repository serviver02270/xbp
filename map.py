import openai

openai.api_key = "YOUR_API_KEY"

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Translate the following English text to French: 'Hello, how are you?'",
    max_tokens=50
)

print(response.choices[0].text)
