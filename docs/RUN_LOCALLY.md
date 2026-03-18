# 🏠 Running Contract Simplifier Locally

## Option 1: Docker (Recommended - Easiest!)

### Prerequisites
- Install Docker Desktop for Windows from: https://www.docker.com/products/docker-desktop/

### Steps

1. **Open PowerShell** in your project folder:
   ```powershell
   cd "c:\Users\LOKESH\OneDrive\ドキュメント\Infosys-Task-1\Contract Language Simplifier"
   ```

2. **Build the Docker image**:
   ```powershell
   docker build -t contract-simplifier .
   ```
   ⏱️ This takes 5-10 minutes (downloads AI models)

3. **Run the container**:
   ```powershell
   docker run -p 5000:7860 contract-simplifier
   ```

4. **Access the app**:
   Open browser: http://localhost:5000

5. **Stop the app**:
   Press `Ctrl+C` in PowerShell

---

## Option 2: Direct Python (Requires Python 3.10 or 3.11)

### ⚠️ Important: Your Current Python 3.13 Won't Work!

You need Python 3.10 or 3.11 because AI libraries don't support 3.13 yet.

### Install Python 3.11

1. **Download Python 3.11**:
   - Go to: https://www.python.org/downloads/release/python-3119/
   - Download "Windows installer (64-bit)"
   - During installation, check "Add Python to PATH"

2. **Verify installation**:
   ```powershell
   python --version
   # Should show: Python 3.11.x
   ```

### Install Dependencies

```powershell
# Navigate to project folder
cd "c:\Users\LOKESH\OneDrive\ドキュメント\Infosys-Task-1\Contract Language Simplifier"

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### Run the Application

```powershell
# Make sure virtual environment is activated
.\venv\Scripts\Activate.ps1

# Run the app
python app.py
```

### Access the Application

Open browser: http://localhost:5000

### Stop the Application

Press `Ctrl+C` in PowerShell

---

## 🎯 Quick Comparison

| Method | Pros | Cons |
|--------|------|------|
| **Docker** | ✅ No Python version issues<br>✅ All dependencies included<br>✅ Works immediately | ❌ Requires Docker Desktop<br>❌ Larger download (~2GB) |
| **Direct Python** | ✅ Faster startup<br>✅ Easier debugging | ❌ Requires Python 3.10/3.11<br>❌ Manual dependency installation |

---

## 🐛 Troubleshooting

### Docker Issues

**Problem**: "Docker daemon is not running"
```powershell
# Start Docker Desktop from Start Menu
```

**Problem**: Port 5000 already in use
```powershell
# Use different port
docker run -p 8000:7860 contract-simplifier
# Then access: http://localhost:8000
```

### Python Issues

**Problem**: "No module named 'torch'"
```powershell
# Make sure virtual environment is activated
.\venv\Scripts\Activate.ps1

# Reinstall requirements
pip install -r requirements.txt
```

**Problem**: "Microsoft Visual C++ 14.0 is required"
- Download and install: https://visualstudio.microsoft.com/visual-cpp-build-tools/
- Select "Desktop development with C++"

---

## 📝 First Time Setup

After running the app for the first time:

1. **Register an account**
   - Go to: http://localhost:5000/register
   - Fill in username, email, password
   - First user becomes admin automatically

2. **Login**
   - Use your email and password

3. **Test the simplifier**
   - Go to "Simplify" page
   - Paste contract text or upload .txt file
   - Click "Simplify"

---

## 🎉 Success!

You should now have the Contract Language Simplifier running locally with:
- ✅ User authentication
- ✅ AI-powered simplification
- ✅ Readability analysis
- ✅ Contract summarization
- ✅ Legal term highlighting
- ✅ Admin dashboard

**No internet required** (after initial setup)!
