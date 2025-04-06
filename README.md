# 📝 FAQ Bot (CLI) with LangGraph & Fuzzy Matching

A simple command-line FAQ bot built using LangGraph and fuzzy matching. It allows users to interact with a predefined set of FAQs in a conversational manner. The bot uses fuzzy logic to match user input even with slight spelling variations or case mismatches.

---

## 🚀 Features

- Conversational CLI interaction 🤖  
- Fuzzy matching of questions 🔍  
- Loads questions from an editable JSON file 📁  
- Custom bot name using environment variables 🔐  
- Lightweight, fast, and offline-capable 🏃‍♂️  

---

## 🛠️ Tech Stack

- **Python**
- **LangGraph**
- **FuzzyWuzzy**
- **python-dotenv**
- **json**

---

## 📁 FAQ Data Format

FAQs are stored in a separate JSON file (`faq_data.json`) like this:

```json
[
  {
    "question": "What is LangGraph?",
    "answer": "LangGraph is a framework for building stateful AI agents using graphs."
  },
  {
    "question": "How do I run this bot?",
    "answer": "Just activate your virtual environment and run python faq_bot.py."
  }
]
```

---

## 🔐 Environment Setup

Store your database credentials in a `.env` file:

```env
BOT_NAME=LangFAQBot
```

> **Important:** The `.env` file is excluded via `.gitignore` to keep credentials secure.

## 📦 Installation

### Clone this repository

```bash
git clone https://github.com/CodeSaadUmair/faq-bot-cli.git
cd blog-manager-cli
```

### Create virtual environment
```bash
python -m venv envo
source envo/bin/activate  
```
###### or on Windows
```
python -m venv envo
envo\Scripts\activate 
```

### Install dependencies
```
pip install -r requirements.txt
```

### Run the app
```
python faq_bot.py
```

## 📌 Sample Questions
- how do I update my profile information?
- update my profil
- do you ship internationally?
- how can I reset my password?
- reset my password


## ✅ To-Do / Future Improvements
- Add persistent logging of user queries 📜
- Integrate OpenAI for fallback answers 🤯
- Add a web UI using Flask or Streamlit 🌐
- FAQ categories or topic filters 🗂️

