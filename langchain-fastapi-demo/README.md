# Langchain + Fastapi - docker-model-runner

This repository provides developers with a set of steps and artifacts to run LLMs in a safe and secure manner using Docker and Langchain + Fastapi .

---

## Step 1: Enable Model Runner

```shell
docker desktop enable model-runner --tcp=12434
```

Verify that the runner is active:

- Browser: http://localhost:12434/engines/v1/models
- Or via curl:
  ```shell
  curl http://localhost:12434/engines/v1/models
  ```

---

## Step 2: Start Services

```shell
docker-compose up -d
```

---

## Step 3: Access the Web UI

Open in your browser:  
http://localhost:3000/

---

## Step 4: Start the Application

```shell
cd langchain-fastapi-demo
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# or .venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt 
uvicorn app.main:app --reload --port 8080
```

---

## Step 5: Use the Chat API

```shell
curl -X POST http://localhost:8080/chat   -H "Content-Type: application/json"   -d '{
    "question": "Hello"
  }'
```

---

## Step 6: Use the Embed API

```shell
curl -X POST http://localhost:8080/embed   -H "Content-Type: application/json"   -d '{
    "text": "Hello"
  }'
```
