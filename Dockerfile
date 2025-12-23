FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]
