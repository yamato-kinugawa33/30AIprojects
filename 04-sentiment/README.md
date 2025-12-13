# 04-sentiment: 感情分析ツール

テキストの感情（ポジティブ・ネガティブ・中立）を分析するツールです。
OpenAI API の Structured Outputs (JSONモード) を使用し、判定結果だけでなく、信頼度スコアや判定理由も構造化データとして取得しています。

## 📸 デモ

![Screenshot](https://placehold.co/600x400?text=Sentiment+Analysis+Demo)
*(ここに実際のスクリーンショットを追加すると分かりやすくなります)*

## 🚀 機能

*   **感情分類**: テキストを Positive / Negative / Neutral の3クラスに分類
*   **信頼度スコア**: 判定の自信度を 0.0〜1.0 で数値化
*   **判定理由**: なぜその判定になったかを、自然言語（日本語）で説明
*   **リッチなUI**:
    *   判定結果に応じた色変化（緑/赤/グレー）
    *   タイプライター風のアニメーション表示

## 🛠️ 技術スタック

*   **Frontend**: Streamlit
*   **AI Model**: GPT-4o-mini (OpenAI API)
*   **Data Handling**: Pydantic, Structured Outputs

## 📦 セットアップ

1. **APIキーの設定**
   `.env` ファイルを作成し、OpenAI APIキーを設定します。
   ```bash
   OPENAI_API_KEY=sk-your-api-key...
   ```

2. **依存ライブラリのインストール**
   ```bash
   pip install -r requirements.txt
   ```

3. **アプリの起動**
   ```bash
   streamlit run app.py
   ```

## 📝 ファイル構成

*   `app.py`: Streamlitを使ったメインのUIアプリケーション
*   `sentiment_utils.py`: OpenAI APIとの通信、Pydanticモデルの定義、コアロジック
*   `requirements.txt`: 必要なPythonライブラリ一覧
