FROM python:3.13-slim

LABEL maintainer="Mohammed Shaik Javeed Akhtar Abbas"
LABEL description="SexDiffKG: Sex-Differential Drug Safety Knowledge Graph"
LABEL version="3.0"

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir scikit-learn matplotlib

# Copy pipeline code
COPY scripts/ scripts/
COPY src/ src/
COPY config/ config/
COPY data/kg/ data/kg/

# Default: show help
CMD ["python3", "-c", "print('SexDiffKG v3 — run scripts in scripts/ to reproduce pipeline')"]
