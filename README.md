---
title: Contract Language Simplifier
emoji: 📜
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
license: mit
# Build: v1.1
---

# Contract Language Simplifier

AI-powered web application that simplifies complex legal contracts into easy-to-understand language.

## Features

- Multi-level simplification (Basic, Intermediate, Advanced)
- Readability analysis with 6 metrics
- AI-powered summarization
- Legal term highlighting with 40+ terms
- User authentication
- Admin dashboard

### User Data & Persistence (Hugging Face Spaces)
- For **Hugging Face Spaces**, you must set a **shared database** and **secrets** so the app works for all visitors.
- See **[docs/HUGGINGFACE_SPACES.md](docs/HUGGINGFACE_SPACES.md)** for: CORS, port 7860, shared database (`DATABASE_URL`), and `SECRET_KEY` / `JWT_SECRET_KEY`.
- Without these, the app will not start in production mode.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)

## Tech Stack

- Flask + Bootstrap UI
- Hugging Face Transformers (FLAN-T5, BART)
- spaCy + NLTK for NLP
- SQLite database
- Docker deployment

## 📖 Documentation

- [**Hosting so everyone can use it from their laptops**](docs/HOSTING_REQUIREMENTS.md)
- [Running Locally](docs/RUN_LOCALLY.md)
- [Hugging Face Spaces (CORS, port 7860, shared DB, secrets)](docs/HUGGINGFACE_SPACES.md)
- [Deployment Guide](docs/DEPLOY_GUIDE.md)
- [Quick Start](docs/QUICKSTART.md)

## 🛠️ Scripts

- Windows Setup: `scripts/setup.bat`
- Linux/Mac Setup: `scripts/setup.sh`
- Docker Upload: `scripts/upload_to_huggingface.bat`
