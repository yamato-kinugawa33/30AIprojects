# Simple Chat App

StreamlitとOpenAI APIを使用したシンプルなチャットアプリケーションです。

## 機能

- OpenAIのGPTモデル（gpt-4o-mini）を使用したチャット機能
- ストリーミング応答によるリアルタイム表示
- チャット履歴の保持（セッション内）

## セットアップ

1. 仮想環境の作成と有効化
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

2. 依存ライブラリのインストール
   ```bash
   pip install -r requirements.txt
   ```

3. 環境変数の設定
   `.env`ファイルを作成し、OpenAI APIキーを設定してください。
   ```
   OPEN_AI_API_KEY=your_api_key_here
   ```

## 実行方法

以下のコマンドでアプリケーションを起動します。

```bash
streamlit run app.py
```

### コンソール版の実行

Web UIを使用せず、ターミナルでチャットを行う場合は以下のコマンドを実行します。

```bash
python main.py
```
