import json
import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def extract_claims(text):

    prompt = f"""
You are an expert fact-checking assistant.

Extract ONLY factual claims that can be verified.

Include:
- Statistics
- Percentages
- Dates
- Financial figures
- Technical metrics

Return ONLY valid JSON.

Format:

[
  {{
    "claim":"India population is 1.2 billion",
    "type":"Statistic"
  }}
]

Do not use markdown.
Do not add explanations.

Document:

{text[:20000]}
"""

    response = model.generate_content(prompt)

    raw_text = response.text.strip()

    raw_text = raw_text.replace("```json", "")
    raw_text = raw_text.replace("```", "")
    raw_text = raw_text.strip()

    try:
        return json.loads(raw_text)

    except Exception:
        return []