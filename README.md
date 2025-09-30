# PortfoliAI 🤖📈

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![OpenAI](https://img.shields.io/badge/OpenAI-Powered-green.svg)](https://openai.com/)

> **PortfoliAI** is an AI-powered portfolio management assistant that leverages **multi-agent AI architecture** to analyze investments, assess risks, conduct research, and deliver personalized recommendations.

---

## 🚀 Introduction

Managing an investment portfolio can be complex and time-consuming. Investors need to track performance, assess risks, and stay updated with rapidly changing market conditions.  

**PortfoliAI** simplifies this process by combining multiple AI agents into a unified assistant. Each agent specializes in tasks such as portfolio analysis, risk evaluation, market research, and recommendation generation. With support for **CSV** and **PDF** portfolio files, PortfoliAI provides professional-grade insights through an easy-to-use Streamlit interface.

---

## ✨ Key Features

- 📤 **Multi-format Upload** – Upload CSV or PDF portfolio files seamlessly  
- 🔍 **Intelligent Portfolio Analysis** – Extracts and summarizes holdings automatically  
- ⚖️ **Risk Assessment** – Evaluates volatility, correlations, and concentration risks  
- 🔬 **Market Research Integration** – Retrieves real-time insights via Google Programmable Search  
- 💡 **AI-Powered Recommendations** – Actionable suggestions for diversification and optimization  
- 📊 **Interactive Visualizations** – Charts and metrics for better understanding  
- 🤖 **Multi-Agent Orchestration** – Specialized agents working together, powered by **LangGraph**  

---

## 🏗️ Architecture

PortfoliAI uses a **multi-agent asynchronous workflow** orchestrated by LangGraph:

```
Portfolio Upload → Input Converter → Portfolio Agent → Risk Agent
↓ ↓
Portfolio Research Agent Risk Research Agent
↓ ↓
Recommendation Agent → Final Report
```


- **Portfolio Agent** – Parses files, extracts holdings, and summarizes allocations  
- **Risk Agent** – Calculates risk metrics and portfolio volatility  
- **Research Agents** – Gather contextual insights from web search  
- **Recommendation Agent** – Synthesizes all results into actionable advice  

---

## ⚙️ Technology Stack

| Component          | Technology |
|--------------------|------------|
| **Frontend**       | Streamlit |
| **Data Processing**| Pandas, PDFPlumber |
| **AI/LLM**         | Gemini API, OpenAI Agents SDK |
| **Orchestration**  | LangGraph, asyncio |
| **Validation**     | Pydantic |
| **Visualization**  | Matplotlib, Streamlit Charts |

---

## 📦 Installation

### Prerequisites
- Python 3.8+  
- pip package manager  
- Git  

### Setup Steps

```bash
# Clone repository
git clone https://github.com/shanks1554/portfoliai.git
cd portfoliai

# Create virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```
Environment Variables

Create a .env file in the root directory with the following:
```
GEMINI_API_KEY=your_gemini_api_key
GEMINI_BASE_URL="https://generativelanguage.googleapis.com/v1beta/openai/"
GOOGLE_CSE_ID=your_google_custom_search_id
GOOGLE_API_KEY=your_google_api_key
```

🚀 Usage

Run the application with Streamlit:

```
streamlit run app.py
```
Then open http://localhost:8501
 in your browser.

Workflow:

  1. Upload a CSV or PDF portfolio file

  2. Wait while AI agents process the data

  3. View results in sections:

      - Portfolio Summary

      - Risk Assessment

      - Market Research

      - Investment Recommendations

📸 Demo

Live Demo: https://portfoliai.onrender.com/

GitHub Repository: https://github.com/shanks1554/portfoliai.git

📄 License

This project is licensed under the MIT License.
