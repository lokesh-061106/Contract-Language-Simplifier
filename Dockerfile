# Multi-stage Docker build for Contract Language Simplifier
FROM python:3.10-slim as base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Download spaCy model
RUN python -m spacy download en_core_web_sm

# Download NLTK data
RUN python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab', quiet=False)"
ENV NLTK_DATA=/root/nltk_data

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p uploads model_cache

# Expose port 7860 (Hugging Face Spaces requirement)
EXPOSE 7860

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:7860/ || exit 1

# Run with gunicorn for production on port 7860
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "--workers", "1", "--timeout", "300", "--access-logfile", "-", "--error-logfile", "-", "app:app"]
