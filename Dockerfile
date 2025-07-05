FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x wait-for-db.sh run.sh

ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["./wait-for-db.sh", "db"]
CMD ["./run.sh"]
