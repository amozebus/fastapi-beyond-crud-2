FROM python:3.10-slim

WORKDIR /usr/src/api

COPY pyproject.toml .

RUN pip install .

COPY . .

CMD ["python", "src/main.py"]