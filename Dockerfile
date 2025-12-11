FROM mcr.microsoft.com/playwright/python:v1.48.0-jammy

WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers (chromium is enough for your tests)
RUN playwright install chromium

# Copy project files
COPY . .

# Create output directories
RUN mkdir -p reports screenshots

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV HEADLESS=true

# Run tests with HTML report
CMD ["pytest", "--html=reports/report.html", "--self-contained-html", "-v", "-s"]