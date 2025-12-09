from openai import OpenAI
from dotenv import load_dotenv
import os
import tiktoken

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. System Prompt (指示チューニング)
SYSTEM_PROMPT = """
あなたは優秀な編集者です。
ユーザーから提供されたテキストを、以下の制約に従って要約してください。

# 制約
- 重要なポイントを逃さないこと
- 簡潔で読みやすい日本語にすること
- 箇条書き形式で出力すること
"""

def split_text(text, limit=3000):
    """
    2. Token Optimization (tiktoken版)
    文字数ではなく、モデルが認識する正確な「トークン数」で分割します。
    """
    # モデルごとの計算機を取得
    try:
        encoding = tiktoken.encoding_for_model("gpt-4o-mini")
    except KeyError:
        # モデル名が見つからない場合は汎用的なcl100k_baseを使用
        encoding = tiktoken.get_encoding("cl100k_base")

    # テキストをトークン(数字の列)に変換
    tokens = encoding.encode(text)
    
    # リスト内包表記でトークンリストを分割
    token_chunks = [tokens[i:i+limit] for i in range(0, len(tokens), limit)]
    
    # 分割されたトークン列を再びテキストに戻す
    return [encoding.decode(chunk) for chunk in token_chunks]

print("=== 長文要約ツール (Chunibyo Edition) 起動 ===")

while True:
    user_input = input("\n要約したいテキストを入力 (exitで終了): ")
    if user_input.lower() in ["exit", "quit"]:
        print("終了")
        break
    
    # 入力が空の場合はスキップ
    if not user_input.strip():
        continue

    # 入力を分割 (トークン最適化処理のシミュレーション)
    chunks = split_text(user_input, chunk_size=2000) # 2000文字単位で分割

    try:
        final_summary = []
        for i, chunk in enumerate(chunks):
            # 文脈をリセットし、都度要約を行う (Map処理)
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"以下のテキストを要約してください:\n\n{chunk}"}
            ]

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0.0 # 事実に基づいた要約のためランダム性を排除
            )
            summary_part = response.choices[0].message.content
            final_summary.append(summary_part)
            print(f"--- 断片 {i+1} の解析完了 ---")

        # 結合して表示
        print("\n=== 【要約結果】 ===")
        print("\n".join(final_summary))
        print("====================\n")

    except Exception as e:
        print(f"Error: {e}")