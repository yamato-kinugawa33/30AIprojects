from pydantic import BaseModel, Field
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class SentimentResponse(BaseModel):
    classification: str = Field(..., description="感情の分類結果: 'positive' (ポジティブ), 'negative' (ネガティブ), 'neutral' (中立) のいずれか")
    confidence_score: float = Field(..., description="0.0 から 1.0 の間の信頼度スコア")
    reason: str = Field(..., description="その分類になった理由の簡潔な説明")

def analyze_text(text: str):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    client = OpenAI(api_key=api_key)

    try:
        response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "あなたは熟練した感情分析アシスタントです。ユーザーのテキストを分析し、それがポジティブ、ネガティブ、または中立のいずれであるかを判定してください。結果は指定されたJSON形式で返してください。"},
                {"role": "user", "content": text}
            ],
            response_format=SentimentResponse,
        )
        return response.choices[0].message.parsed
    except Exception as e:
        print(f"Error: {e}")
        return None
