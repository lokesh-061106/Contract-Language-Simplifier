@echo off
echo ========================================
echo Uploading ALL files to Hugging Face
echo ========================================
echo.

cd /d "%~dp0"

echo Copying README_HF.md to README.md...
copy /Y README_HF.md README.md

echo.
echo Adding all necessary files...
git add -f app.py config.py models.py sample_texts.py
git add -f requirements.txt Dockerfile docker-compose.yml .env.example LICENSE
git add -f README.md
git add -f templates/*.html
git add -f services/*.py
git add -f static/*

echo.
echo Committing files...
git commit -m "Add all application files for deployment"

echo.
echo Pushing to Hugging Face...
echo (This may ask for your Hugging Face username and password/token)
echo.
git push https://huggingface.co/spaces/lokesh061106/contract-simplifier main

echo.
echo ========================================
echo Done! Check your Space at:
echo https://huggingface.co/spaces/lokesh061106/contract-simplifier
echo ========================================
pause
