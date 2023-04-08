FROM python:3.10.11-slim-bullseye
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY *.py README.md /app/
CMD ["python", "tg_bot.py"]
