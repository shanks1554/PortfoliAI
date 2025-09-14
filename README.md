# PortfoliAI 🤖📈

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenAI](https://img.shields.io/badge/OpenAI-Powered-green.svg)](https://openai.com/)

## 🚀 Introduction

**PortfoliAI** is an intelligent portfolio management assistant that harnesses the power of multi-agent AI architecture to transform how you analyze and optimize your investment portfolio. Whether you're a seasoned investor or just starting your investment journey, PortfoliAI simplifies complex portfolio management through automated analysis, risk assessment, and personalized investment recommendations.

The application accepts portfolio data in multiple formats (CSV and PDF files) and provides comprehensive insights through a sophisticated AI-driven workflow that mimics the expertise of professional financial analysts.

**Supported Input Formats:**
- 📊 CSV files with portfolio holdings
- 📄 PDF portfolio statements and reports

---

## ✨ Features

### Core Functionality
- 📤 **Multi-format Upload**: Seamlessly upload CSV or PDF portfolio files
- 🔍 **Intelligent Portfolio Analysis**: Automatic parsing and comprehensive portfolio summary
- ⚖️ **Advanced Risk Assessment**: Detailed risk analysis based on portfolio composition and market conditions
- 🔬 **Market Research Integration**: Real-time research insights for portfolio holdings
- 💡 **AI-Powered Recommendations**: Personalized investment suggestions based on portfolio analysis
- 🎨 **User-Friendly Interface**: Clean, intuitive Streamlit-based frontend

### Advanced Capabilities
- 📈 **Performance Metrics**: Historical performance analysis and trend identification
- 🎯 **Diversification Analysis**: Portfolio concentration and sector allocation insights
- 📊 **Interactive Visualizations**: Dynamic charts and graphs for better understanding
- 🤖 **Multi-Agent Orchestration**: Coordinated AI agents working together for comprehensive analysis

---

## 🏗️ Architecture

PortfoliAI employs a sophisticated multi-agent architecture with orchestrated workflow management:

### Agent Workflow

```
Portfolio Upload → Portfolio Agent → Risk Agent → Portfolio Research Agent
                                  ↓                        ↓
                         Risk Research Agent → Recommendation Agent → Final Report
```

#### Agent Roles:

1. **🎯 Portfolio Agent**
   - Parses CSV/PDF files
   - Extracts portfolio holdings and allocations
   - Generates comprehensive portfolio summary

2. **⚠️ Risk Agent**
   - Calculates portfolio risk metrics (Beta, Sharpe ratio, VaR)
   - Analyzes correlation between holdings
   - Assesses overall portfolio volatility

3. **🔍 Portfolio Research Agent**
   - Conducts market research on portfolio holdings
   - Analyzes company fundamentals and market trends
   - Provides sector and industry insights

4. **📊 Risk Research Agent**
   - Evaluates market conditions and systemic risks
   - Analyzes macroeconomic factors affecting portfolio
   - Identifies potential risk factors and market volatility

5. **💼 Recommendation Agent**
   - Synthesizes insights from all other agents
   - Generates personalized investment recommendations
   - Provides actionable advice for portfolio optimization

### Technology Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit |
| **Data Processing** | pandas, pdfplumber |
| **AI/ML** | Gemini, OpenAI Agents SDK |
| **Orchestration** | LangGraph, asyncio |
| **Data Validation** | pydantic |
| **Async Processing** | asyncio |

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/shanks1554/portfoliai.git
   cd portfoliai
   ```

2. **Create Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**
   ```bash
   # Create .env file and Add the following API keys to .env file
   
   GEMINI_API_KEY = your_gemini_api_key_here
   GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
   GOOGLE_CSE_ID = your_google_custom_search_id
   GOOGLE_API_KEY = your_google_api_key
   ```

---

## 🚀 Usage

### Running the Application

1. **Start the Streamlit App**
   ```bash
   streamlit run app.py
   ```

2. **Access the Application**
   - Open your browser and navigate to `http://localhost:8501`

### Using PortfoliAI

1. **Upload Your Portfolio**
   - Click "Upload Portfolio File" button
   - Select your CSV or PDF portfolio file
   - Wait for the file to be processed

2. **View Analysis Results**
   The application will display results in organized sections:
   - **Portfolio Summary**: Overview of holdings and allocations
   - **Risk Assessment**: Risk metrics and analysis
   - **Market Research**: Insights on portfolio holdings
   - **Investment Recommendations**: AI-generated suggestions

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 PortfoliAI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

**⭐ If you find PortfoliAI helpful, please consider giving it a star on GitHub!**