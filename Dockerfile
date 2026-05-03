FROM python:3.12-slim
RUN apt update && apt install -y figlet && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENV NOM mickey
CMD ["python", "app.py"]
