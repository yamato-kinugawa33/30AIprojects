from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {"role": "system", "content": 
    "あなたは中2病の男性です。userのinputを全て中2病口調に翻訳してください。"
    },
]

print("exitと入力すると終了です。")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("さらばだ、運命の糸よ！闇の中で再び会おう！")
        break
    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.0
        )
        bot_response = response.choices[0].message.content
        messages.append({"role": "assistant", "content": bot_response})
        print(f"Bot: {bot_response}")

    except Exception as e:
        print("ふふ、運命の歯車が狂ったか…！だが、我が力でこのエラーを打ち砕いてみせる！闇の魔法を解き放つ時が来たようだ！")
        print(f"Error: {e}")