from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))

st.title("Simple chat app")

# セッション状態でメッセージ履歴を初期化
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "日本語で話してください。"}
    ]

# 過去のメッセージを表示（システムメッセージ以外）
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# ユーザー入力の処理
if user_input := st.chat_input("こんにちは"):
    # ユーザーのメッセージを表示・保存
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # AIの応答を生成・表示（ストリーミング）
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
            stream=True,
        )
        response = st.write_stream(stream)
    
    # AIのメッセージを保存
    st.session_state.messages.append({"role": "assistant", "content": response})