import json
import google.generativeai as genai

from tavily import TavilyClient

from config import (
    GEMINI_API_KEY,
    TAVILY_API_KEY
)

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

tavily = TavilyClient(
    api_key=TAVILY_API_KEY
)


def verify_claim(claim):

    search = tavily.search(
        query=claim,
        search_depth="advanced",
        max_results=5
    )

    evidence = []

    for result in search["results"]:

        evidence.append(
            {
                "title": result["title"],
                "url": result["url"],
                "content": result["content"]
            }
        )

    prompt = f"""
You are a professional fact checker.

Claim:

{claim}

Evidence:

{json.dumps(evidence)}

Classify using ONLY one of:

VERIFIED
INACCURATE
FALSE

Rules:

VERIFIED = evidence supports claim

INACCURATE = partially true, outdated,
or contains incorrect figures.

FALSE = evidence contradicts claim.

Return ONLY valid JSON.

Format:

{{
  "status":"VERIFIED",
  "confidence":95,
  "explanation":"short explanation",
  "correct_fact":"latest correct fact",
  "source_url":"url"
}}

Do not use markdown.
Do not add extra text.
"""

    response = model.generate_content(prompt)

    raw_text = response.text.strip()

    raw_text = raw_text.replace("```json", "")
    raw_text = raw_text.replace("```", "")
    raw_text = raw_text.strip()

    try:

        result = json.loads(raw_text)

        result["claim"] = claim

        return result

    except Exception:

        source_url = ""

        if len(search["results"]) > 0:
            source_url = search["results"][0]["url"]

        return {
            "claim": claim,
            "status": "FALSE",
            "confidence": 0,
            "explanation": "Unable to parse verifier response",
            "correct_fact": "",
            "source_url": source_url
        }