
# 🌟 WordWeaver AI - Open Source WordWork Chatbot

WordWeaver AI is a powerful open-source AI chatbot that helps users explore the transformational power of language using WordWork principles: sound meditation, the map of consciousness, energy astrology, MBTI typing, NLP, and daily High-Frequency Word rituals.

---

## 🚀 Features

- ✨ **Word Resonance Analyzer**: NLP engine that scores your words using vibrational frequency mapping.
- 🔮 **Natal Chart Integration**: Astrological profile mapping (Flatlib-ready).
- 🧠 **MBTI Personality Typing**: Simplified typing tool (expandable).
- 📅 **Personalized HFW Calendar Generator**: 31-day affirmation and energy alignment schedule.
- 🎶 **Sound Frequency Tools**: Match tones (e.g., 528Hz) to your daily word.
- 🧘 **Daily Ritual Interface**: Streamlit front-end for journaling, affirmations, and guided use.
- 🐳 **Docker Ready**: One-command containerized app.

---

## 📁 Project Structure

```
wordweaver_ai/
├── main.py              # FastAPI backend endpoints
├── analyzer.py          # NLP + HFW/LFW sentence analysis
├── calendar_gen.py      # Generates personalized 31-day WordWork calendar
├── mbti.py              # MBTI personality typing (mock)
├── astrology.py         # Natal chart profile generator (mock)
├── sound_utils.py       # (optional) Sound frequency tools
├── streamlit_app.py     # Streamlit front-end
├── requirements.txt     # Dependencies
├── Dockerfile           # Docker deployment
└── README.md            # This file
```

---

## 🧪 Run Locally

### 1. Set up virtual env
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Launch backend
```bash
uvicorn main:app --reload
```

### 3. Launch Streamlit UI
```bash
streamlit run streamlit_app.py
```

---

## 🐳 Run in Docker

```bash
docker build -t wordweaver .
docker run -p 8000:8000 wordweaver
```

---

## 💡 Example API Usage

```bash
curl -X POST http://localhost:8000/analyze -H "Content-Type: application/json" -d '{"text": "I feel joyful and abundant today."}'
```

---

## 📚 Inspired By

- Dr. David R. Hawkins - *Map of Consciousness*
- Pao Chang - *How Word Became Flesh*
- Bruce Lipton - *Biology of Belief*
- Jeffrey Allen - *Energy Awareness*
- WordWork by Markice Moore

---

## 🧠 License

Licensed under Apache 2.0. Please attribute source if reused in commercial systems.

---

## 🧔🏽‍♂️ Author

**Markice Moore** | Both Sides of the Camera Studios  
Visionary, Speaker, Creator of WordWeaver AI

---

## 🔮 Your Words Create Worlds.

Start your journey today.
