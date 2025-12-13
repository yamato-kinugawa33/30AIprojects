import streamlit as st
import os
from dotenv import load_dotenv
from sentiment_utils import analyze_text
import time

# 環境変数の読み込み
load_dotenv()

st.title("感情分析ツール")

# APIキーの確認
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OpenAI APIキーが設定されていません。.envファイルを確認してください。")
else:
    st.success("APIキーが検出されました。")

text_input = st.text_area("分析するテキストを入力してください", height=150)

def stream_text(text):
    for word in text:
        yield word
        time.sleep(0.02)

if st.button("分析する"):
    if not text_input:
        st.warning("テキストを入力してください。")
    else:
        with st.spinner("AIが感情を読み取っています..."):
            result = analyze_text(text_input)
        
        if result:
            st.subheader("分析結果")
            
            # 結果表示用のコンテナ
            with st.container():
                # 結果の表示 (色分け)
                color = "gray"
                emoji = "😐"
                if result.classification == "positive":
                    color = "#28a745"
                    emoji = "😄"
                elif result.classification == "negative":
                    color = "#dc3545"
                    emoji = "😢"
                
                # 大きく判定を表示
                st.markdown(
                    f"""
                    <div style="padding: 20px; border-radius: 10px; background-color: {color}20; border: 2px solid {color}; text-align: center; margin-bottom: 20px;">
                        <h2 style="color: {color}; margin: 0;">{emoji} {result.classification.upper()}</h2>
                        <p style="margin: 0; color: {color}; font-weight: bold;">信頼度: {result.confidence_score:.2f}</p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                
                st.write("**判定理由:**")
                # タイプライター風アニメーション
                st.write_stream(stream_text(result.reason))
            
            with st.expander("詳細データ (JSON)"):
                st.json({
                    "classification": result.classification,
                    "confidence_score": result.confidence_score,
                    "reason": result.reason
                })
        else:
            st.error("分析に失敗しました。APIキーまたは通信環境を確認してください。")
