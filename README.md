# 🔍 FactCheck Agent

An AI-powered fact-checking web application that automatically verifies claims in PDF documents against live web data.

## 📌 Overview

Marketing reports, research documents, and business presentations often contain outdated statistics, inaccurate figures, or hallucinated AI-generated content.

FactCheck Agent acts as a **Truth Layer** by:

* Extracting factual claims from uploaded PDFs
* Searching live web sources for supporting evidence
* Verifying claim accuracy
* Flagging inaccurate or false information
* Providing corrected facts and source references


---

## 🏗️ System Architecture

```text
PDF Upload
    ↓
PDF Text Extraction (PyMuPDF)
    ↓
Claim Extraction (Gemini)
    ↓
Web Search (Tavily)
    ↓
Evidence Collection
    ↓
Fact Verification (Gemini)
    ↓
Fact Check Report
```

---

## ✨ Features

### Claim Extraction

Automatically identifies:

* Statistics
* Percentages
* Dates
* Financial figures
* Technical metrics

### Live Fact Verification

Searches the web using Tavily Search API and validates claims against current information.

### Classification

Claims are classified into:

| Status     | Description                              |
| ---------- | ---------------------------------------- |
| VERIFIED   | Evidence supports the claim              |
| INACCURATE | Claim is outdated or partially incorrect |
| FALSE      | Evidence contradicts the claim           |

### Correct Fact Generation

For inaccurate or false claims, the system provides:

* Updated factual information
* Supporting explanation
* Source URL

### Report Generation

Produces:

* Executive Summary
* Detailed Claim Analysis
* Downloadable CSV Report

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### LLM

* Google Gemini 2.5 Flash

### Search Engine

* Tavily Search API

### PDF Processing

* PyMuPDF

### Data Processing

* Pandas

### Environment Management

* python-dotenv

---

## 📂 Project Structure

```text
factcheck-agent/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── utils/
│   ├── claim_extractor.py
│   ├── verifier.py
│   └── pdf_parser.py
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/mohang553/factcheck-agent
cd factcheck-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

Application will be available at:

```text
http://localhost:8501
```

---

## 🧪 Sample Test Case

Input PDF:

```text
OpenAI was founded in 2012.
India population is 1.2 billion.
Python was released in 2018.
Microsoft revenue in 2024 was $50 billion.
```

Output:

| Claim                         | Result     |
| ----------------------------- | ---------- |
| OpenAI founded in 2012        | FALSE      |
| India population 1.2 billion  | INACCURATE |
| Python released in 2018       | FALSE      |
| Microsoft revenue $50 billion | FALSE      |

---

## 📊 Example Output

The application generates:

* Executive Summary
* Confidence Score
* Claim Explanation
* Correct Fact
* Source Reference

Example:

```text
Claim:
India population is 1.2 billion

Status:
INACCURATE

Correct Fact:
India's population is estimated to be over 1.43 billion.

Source:
https://www.worldometers.info
```

---

## 🎯 Assignment Objectives Covered

✅ PDF Upload Interface

✅ Automated Claim Extraction

✅ Live Web Verification

✅ False Claim Detection

✅ Correct Fact Identification

✅ Source Attribution

✅ Downloadable Report

✅ Deployment Ready

---

## 🔮 Future Enhancements

* Multi-document comparison
* PDF report export
* Source credibility scoring
* Batch document processing
* OCR support for scanned PDFs
* RAG-based evidence retrieval
* Citation highlighting inside PDFs

---

## 📜 License

This project was developed as part of a Product Management Trainee assessment and is intended for educational and demonstration purposes.
