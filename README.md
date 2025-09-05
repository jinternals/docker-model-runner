# Docker Model Runner — Examples & Integrations

A hands-on starter kit for wiring **Docker Model Runner (DMR)** into real apps.

**This repo includes:**
- `spring-demo/` – Java Spring Boot app using Spring AI against DMR
- `langchain-fastapi-demo/` – Python FastAPI app using LangChain/OpenAI clients against DMR
- `docker-compose.yaml` – Optional UI via Open WebUI, prewired to DMR
- `test.http` – Ready-to-run HTTP calls for VS Code/IntelliJ REST clients

## What is Docker Model Runner?

**Docker Model Runner (DMR)** lets you serve local models behind **OpenAI-compatible APIs** directly from Docker Desktop/Engine.

- **Pull** models as OCI artifacts (e.g., `ai/llama3.2:1B-Q8_0`).
- **Call** familiar endpoints like `/v1/chat/completions`—no bespoke servers to stand up.
- **Use** existing OpenAI SDKs and tools with only a base URL change.

> See the official Docker Model Runner documentation for platform support and configuration details.

---

## Why this repo?

Most examples stop at one-off `curl` commands. This repository provides:

- **Two working integrations:** Spring Boot (Spring AI) and Python (FastAPI + LangChain/OpenAI).
- **A ready UI stack:** `docker-compose.yaml` wiring **Open WebUI** to DMR.
- **Requests:** `test.http` Ready-to-run HTTP calls for VS Code/IntelliJ REST clients

