@echo off
echo ========================================
echo Uploading to Hugging Face Spaces
echo ========================================
echo.

echo Step 1: Adding files...
git add app.py config.py models.py sample_texts.py
git add requirements.txt Dockerfile docker-compose.yml .env.example LICENSE
git add templates/ services/ static/
git add README_HF.md

echo.
echo Step 2: Committing files...
git commit -m "Add all application files for deployment"

echo.
echo Step 3: Pushing to Hugging Face...
echo NOTE: You may be asked to login to Hugging Face
echo.
git push huggingface main

echo.
echo ========================================
echo Upload complete!
echo Check your Space at:
echo https://huggingface.co/spaces/lokesh061106/contract-simplifier
echo ========================================
pause
