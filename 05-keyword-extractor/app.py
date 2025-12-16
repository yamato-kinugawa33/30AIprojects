import streamlit as st
import os
from dotenv import load_dotenv
from keyword_utils import extract_keywords
import time

# 環境変数の読み込み
load_dotenv()

# ページ設定
st.set_page_config(
    page_title="SEOキーワード抽出ツール",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 SEOキーワード抽出ツール")
st.markdown("テキストからSEOに有効なキーワードを自動抽出します。")

# APIキーの確認
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OpenAI APIキーが設定されていません。.envファイルを確認してください。")
else:
    st.success("APIキーが検出されました。")

# サイドバー設定
with st.sidebar:
    st.header("⚙️ 設定")
    max_keywords = st.slider("抽出するキーワード数", min_value=5, max_value=20, value=10)

# メインコンテンツ
text_input = st.text_area(
    "分析するテキストを入力してください",
    height=200,
    placeholder="ウェブページのコンテンツ、ブログ記事、商品説明などを貼り付けてください..."
)


def stream_text(text):
    """タイプライター風にテキストを表示"""
    for word in text:
        yield word
        time.sleep(0.02)


if st.button("🔍 キーワードを抽出", type="primary"):
    if not text_input:
        st.warning("テキストを入力してください。")
    else:
        with st.spinner("AIがキーワードを抽出しています..."):
            result = extract_keywords(text_input, max_keywords=max_keywords)
        
        if result:
            st.subheader("📊 抽出結果")
            
            # メイントピックと要約
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**🎯 メイントピック:** {result.main_topic}")
            with col2:
                st.markdown(f"**📝 要約:** {result.summary}")
            
            st.divider()
            
            # キーワード一覧
            st.subheader("🏷️ 抽出されたキーワード")
            
            for i, keyword in enumerate(result.keywords, 1):
                # 関連度に応じた色を設定
                if keyword.relevance >= 0.8:
                    color = "#28a745"  # 緑
                    bar_color = "green"
                elif keyword.relevance >= 0.5:
                    color = "#ffc107"  # 黄
                    bar_color = "orange"
                else:
                    color = "#6c757d"  # グレー
                    bar_color = "gray"
                
                col1, col2, col3, col4 = st.columns([1, 3, 2, 2])
                
                with col1:
                    st.markdown(f"**#{i}**")
                with col2:
                    st.markdown(f"**{keyword.word}**")
                with col3:
                    st.progress(keyword.relevance, text=f"関連度: {keyword.relevance:.0%}")
                with col4:
                    st.markdown(f"`{keyword.category}`")
            
            # JSON詳細
            with st.expander("📋 詳細データ (JSON)"):
                st.json({
                    "main_topic": result.main_topic,
                    "summary": result.summary,
                    "keywords": [
                        {
                            "word": kw.word,
                            "relevance": kw.relevance,
                            "category": kw.category
                        }
                        for kw in result.keywords
                    ]
                })
        else:
            st.error("キーワード抽出に失敗しました。APIキーまたは通信環境を確認してください。")

# フッター
st.divider()
st.markdown(
    "<p style='text-align: center; color: #666;'>Powered by OpenAI GPT-4o-mini</p>",
    unsafe_allow_html=True
)
