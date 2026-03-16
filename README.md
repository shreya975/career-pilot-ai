# 🚀 CareerPilot AI  
### Synchronizing Skills with Future Opportunities  

CareerPilot AI is an **AI-powered Skill Gap Analysis and Career Roadmap Platform** that analyzes a user's resume, identifies missing skills for their target role, and generates a personalized roadmap with learning resources and project suggestions.

Built for **APEX AI Hackathon 2026** 🏆


---

# 🌟 Key Features

📄 **Resume Skill Extraction**  
Automatically extracts skills from uploaded resumes (PDF/DOCX).

📊 **Skill Gap Analysis**  
Compares user skills with industry job role requirements.

📈 **Skill Match Score**  
Calculates how close the user is to their target role.

🗺️ **Personalized Career Roadmap**  
Generates structured learning phases with estimated timelines.

📚 **Learning Resource Recommendations**  
Suggests relevant courses and learning materials.

💼 **Project Suggestions**  
Recommends real-world projects to improve practical skills.

🎯 **Interactive Dashboard**  
Modern React-based dashboard with visual roadmap and analytics.

---


## 🧠 System Architecture
```
Frontend (React + Tailwind)
│
▼
API Layer (Flask)
│
▼
AI Logic Layer (Services)
│
├── Skill Extractor
├── Skill Analyzer
├── Roadmap Generator
├── Suggestion Engine
└── Resume Scorer
│
▼
Structured Data Layer (JSON Databases)

```

---

---

## 📁 Project Structure

```
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   │
│   ├── routes/
│   │   ├── analyze.py
│   │   └── roadmap.py
│   │
│   ├── services/
│   │   ├── skill_extractor.py
│   │   ├── skill_analyzer.py
│   │   ├── roadmap_generator.py
│   │   ├── suggestion_engine.py
│   │   └── resume_scorer.py
│   │
│   ├── utils/
│   │   ├── file_parser.py
│   │   └── roadmap_data_loader.py
│   │
│   ├── data/
│   │   ├── skills_db.json
│   │   ├── job_roles.json
│   │   ├── learning_resources.json
│   │   ├── project_suggestions.json
│   │   ├── phase_metadata.json
│   │   └── roadmaps.json
│   │
│   └── uploads/
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── api.js
│   │   │
│   │   ├── components/
│   │   │   ├── ResumeUpload.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── SkillsAnalysis.jsx
│   │   │   ├── RoadmapTimeline.jsx
│   │   │   ├── ProjectsList.jsx
│   │   │   ├── RoleDropdown.jsx
│   │   │   ├── ProfileCard.jsx
│   │   │   └── AnalyzeButton.jsx
│   │   │
│   │   ├── App.js
│   │   └── index.js
│   │
│   ├── package.json
│   └── tailwind.config.js
│
└── README.md

```
---

## ⚙️ Tech Stack
- Frontend
  - React.js
  - Tailwind CSS
  - JavaScript
- Backend
  - Python
  - Flask
  - REST API
- AI Logic
  - Skill extraction engine
  - Skill gap analysis algorithm
  - Roadmap generation engine
- Data
  - JSON-based structured skill datasets
---

## 🚀 Installation & Setup
- 1️⃣ Clone the Repository
    - git clone https://github.com/shreya975/career-copilot-ai.git
    - cd career-copilot-ai
      
- 2️⃣ Backend Setup
    - cd backend
      
    - python -m venv venv
    - venv\Scripts\activate
      
    - pip install -r requirements.txt
      
    - python app.py
  - Backend runs on:
    - http://localhost:5000
      
- 3️⃣ Frontend Setup
    - cd frontend
      
    - npm install
      
    - npm start

  - Frontend runs on:
    - http://localhost:3000
---

## 🧪 How It Works

1. User uploads resume
2. Resume is parsed and skills extracted
3. Skills compared with job role requirements
4. Skill gap analysis performed
5. Career roadmap generated
6. Learning resources and projects recommended
7. Results displayed on interactive dashboard

---

## 🌍 Real-World Applications
- Career guidance platforms
- University placement systems
- Job preparation tools
- Corporate skill assessment systems

---

## 🔮 Future Improvements
- NLP-based skill extraction
- LinkedIn integration
- AI-powered personalized recommendations
- Cloud deployment
- User authentication and profiles

---
## 🏆 Hackathon Project
- Developed for:
  APEX AI Hackathon 2026

- Team: MindMappers

---

## 👨‍💻 Contributors
- Backend API Engineer (SHREYA N. MAHAJAN)
- Backend AI Engineer (PRATHMESH P. BHOYAR)
- Frontend UI/UX Engineer (VEDANT P. ZOD)
- Frontend Integration Engineer (KAUSTUBH K. SAURKAR)
