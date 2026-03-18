@echo off
echo ========================================
echo Upload to Hugging Face with Token
echo ========================================
echo.

set /p TOKEN="Paste your Hugging Face token (starts with hf_): "

echo.
echo Navigating to project folder...
cd /d "%~dp0"

echo.
echo Initializing git if needed...
git init
git branch -M main

echo.
echo Adding files...
copy /Y README_HF.md README.md
git add app.py config.py models.py sample_texts.py
git add requirements.txt Dockerfile docker-compose.yml .env.example LICENSE README.md
git add templates/ services/ static/

echo.
echo Committing files...
git commit -m "Add all application files for deployment"

echo.
echo Pushing to Hugging Face with your token...
git push https://lokesh061106:%TOKEN%@huggingface.co/spaces/lokesh061106/contract-simplifier main --force

echo.
echo ========================================
echo Done! Check your Space at:
echo https://huggingface.co/spaces/lokesh061106/contract-simplifier
echo ========================================
pause
