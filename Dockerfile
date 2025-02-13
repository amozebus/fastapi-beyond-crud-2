FROM python:3.10-slim

WORKDIR /usr/src/api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]