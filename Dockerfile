FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install uv

RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "gunicorn", "-w", "3", "-b", "0.0.0.0:8000", "main:app"] 

