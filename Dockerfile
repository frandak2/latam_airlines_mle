FROM python:3.9-slim-buster

WORKDIR /app

COPY api/requirements.txt .

RUN pip install -U pip && pip install -r requirements.txt

COPY api/ ./api

COPY models/model_balanced_over.pkl .models/model_balanced_over.pkl

COPY initializer.sh .

RUN chmod +x initializer.sh

EXPOSE 8000

ENTRYPOINT ["./initializer.sh"]