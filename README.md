# 🧠 Mental Health Check Bot  
*Built with LangChain & Gemini*

A compassionate AI agent that helps users reflect on their mental well-being. It performs daily mood check-ins, suggests coping strategies, logs emotional states, and ensures user data remains private by default.

## 🌟 Features
- 🗓️ Daily mood check-ins
- 🎭 Emotion detection through tone analysis
- 💡 Tailored coping tips and advice
- 📒 Timestamped local logs of user moods
- 🔐 Privacy-focused, no external sync by default

## ⚙️ Installation

### 1. Set up virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your Gemini API key (if needed)

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your-gemini-api-key
```

---

## 🚀 Usage

To start the chatbot:

```bash
python main.py
```

The bot will ask about your mood, provide empathetic responses, suggest strategies, and log your input in the `logs/` folder with timestamps.

---

## 🔐 Privacy First

* All emotional data is stored **locally** by default.
* No external syncing or cloud storage is used unless added explicitly.
* You may later extend functionality to include cloud sync or calendar reminders.

---

## 💬 Why It Matters

* Promotes daily self-awareness and journaling
* Flags negative emotional trends (e.g., burnout, sadness)
* Encourages mental wellness with consistent reflection
* Helps build emotional resilience over time

---
