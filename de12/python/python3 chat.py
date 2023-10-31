import openai
import os
from datetime import datetime

start_time = datetime.now()

openai.api_key = os.getenv("OPENAI_API_KEY")
model_name = "gpt-4"

question = """
Q: What is the best way to learn ChatGPT using Python?
"""


response = openai.ChatCompletion.create(
    model=model_name,
    messages=[
        {"role": "user", "content": question},
    ],
)

end_time = datetime.now()

print(response.choices[0]["message"]["content"].strip())
print(f"elapsed time: {end_time - start_time}")


with open(
    f"output-{model_name}-{datetime.now().strftime('%Y%m%dT%H%M%S')}.txt", "w"
) as f:
    f.write(f"model: {model_name}\n")
    f.write("time: " + str(end_time - start_time) + "\n")
    f.write("question: " + question + "\n")
    f.write("answer: " + response.choices[0]["message"]["content"].strip() + "\n")

from pychatgpt import Chat, Options

options = Options()

options.track = True

options.chat_log = "chat_log.txt"
options.id_log = "id_log.txt"

chat = Chat(email="", password="", options=options)
chat.cli_chat()
