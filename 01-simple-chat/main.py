from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))

messages = [
    {"role": "system", "content": "日本語で話してください。"}
]

print("AIとのチャットを開始します。'exit'と入力すると終了します。")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7
    )

    assistant_content = response.choices[0].message.content
    print(f"AI: {assistant_content}")
    
    messages.append({"role": "assistant", "content": assistant_content})
