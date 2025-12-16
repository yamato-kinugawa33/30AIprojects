from pydantic import BaseModel, Field
from openai import OpenAI
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()


class Keyword(BaseModel):
    """抽出されたキーワードを表すモデル"""
    word: str = Field(..., description="抽出されたキーワードまたはキーフレーズ")
    relevance: float = Field(..., description="0.0から1.0の間の関連度スコア。1.0が最も関連性が高い")
    category: str = Field(..., description="キーワードのカテゴリ（例: 製品, 技術, ブランド, サービス, 業界, トピック）")


class KeywordResponse(BaseModel):
    """キーワード抽出のレスポンスモデル"""
    keywords: List[Keyword] = Field(..., description="抽出されたキーワードのリスト（関連度順）")
    main_topic: str = Field(..., description="テキストのメイントピックまたはテーマ")
    summary: str = Field(..., description="テキストの簡潔な要約（50文字以内）")


def extract_keywords(text: str, max_keywords: int = 10) -> KeywordResponse | None:
    """
    テキストからSEOキーワードを抽出する
    
    Args:
        text: 分析するテキスト
        max_keywords: 抽出するキーワードの最大数
    
    Returns:
        KeywordResponse: 抽出されたキーワード情報、エラー時はNone
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    client = OpenAI(api_key=api_key)

    system_prompt = f"""あなたはSEO専門家です。与えられたテキストから、検索エンジン最適化に有効なキーワードを抽出してください。

        抽出ルール:
        1. 最大{max_keywords}個のキーワードを抽出
        2. 単語だけでなく、重要なフレーズ（2〜3語の組み合わせ）も含める
        3. 関連度スコアは、SEO効果と検索ボリュームを考慮して設定
        4. カテゴリは適切に分類（製品, 技術, ブランド, サービス, 業界, トピック, 地名, 人名 など）
        5. キーワードは関連度の高い順にソート

        結果は指定されたJSON形式で返してください。"""

    try:
        response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ],
            response_format=KeywordResponse,
        )
        return response.choices[0].message.parsed
    except Exception as e:
        print(f"Error: {e}")
        return None
