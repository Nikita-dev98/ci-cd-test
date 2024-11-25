FROM python:3.10-slim

WORKDIR /CI-CD-TEST

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "facts:app", "--host", "0.0.0.0", "--port", "8000"]