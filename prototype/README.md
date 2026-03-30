Contract Language Simplifier — Prototype

This is a self-contained Streamlit prototype that simplifies legal language,
produces a short summary, and shows a readability score.

Quick start (Windows PowerShell):

```powershell
cd "Contract Language Simplifier"\prototype
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m streamlit run app.py --server.port 8501
```

Open: http://localhost:8501

Notes:

- This prototype is intentionally lightweight (no external AI models).
- For production, wire in real simplification models, a database, and secure secrets.
