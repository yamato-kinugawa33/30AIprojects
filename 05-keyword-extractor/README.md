# 05-keyword-extractor - SEOキーワード抽出ツール

OpenAIのStructured Outputs機能を使用して、テキストからSEOに有効なキーワードを自動抽出するツールです。

## 機能

- 📝 テキストからキーワードを自動抽出
- 📊 各キーワードの関連度スコアを表示
- 🏷️ キーワードのカテゴリ分類
- 🎯 メイントピックの特定
- 📋 JSON形式でのエクスポート

## セットアップ

### 1. 仮想環境の有効化

```bash
cd 05-keyword-extractor
source .venv/bin/activate
```

### 2. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 3. APIキーの設定

`.env`ファイルにOpenAI APIキーを設定：

```
OPENAI_API_KEY=your_api_key_here
```

## 使用方法

### アプリの起動

```bash
streamlit run app.py
```

ブラウザで `http://localhost:8501` を開いてアプリにアクセスします。

### 使い方

1. テキストエリアに分析したいテキストを入力
2. サイドバーで抽出するキーワード数を設定
3. 「キーワードを抽出」ボタンをクリック
4. 抽出されたキーワードと関連度が表示されます

## プロジェクト構成

```
05-keyword-extractor/
├── .env                  # APIキー設定
├── .venv/                # 仮想環境
├── app.py                # Streamlit UI
├── keyword_utils.py      # コア機能（キーワード抽出）
├── requirements.txt      # 依存関係
├── README.md             # このファイル
└── docs/
    └── todo.md           # プロジェクトTodoリスト
```

## 技術スタック

- **Python 3.x**
- **OpenAI API** - GPT-4o-miniモデルを使用
- **Pydantic** - 構造化出力のスキーマ定義
- **Streamlit** - WebUI

## 出力例

```json
{
  "main_topic": "人工知能",
  "summary": "AIの最新トレンドとビジネス活用について",
  "keywords": [
    {
      "word": "機械学習",
      "relevance": 0.95,
      "category": "技術"
    },
    {
      "word": "自然言語処理",
      "relevance": 0.85,
      "category": "技術"
    }
  ]
}
```
