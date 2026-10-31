# Travel ADK Multiagent

Laboratorio UCV de sistema multiagente de viajes con Google ADK.

## Agentes

- Travel Coordinator Agent
- Web Search Agent
- Itinerary Agent
- Budget Agent
- Risk Reviewer Agent

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install
```

## Variables de entorno

Crear archivo `.env` a partir de `.env.example`:

```bash
GOOGLE_API_KEY="TU_API_KEY"
```

## Ejecutar agente por consola

```bash
poetry run adk run travel_assistant
```

## Ejecutar agente web

```bash
poetry run adk web --port 8000
```

Abrir:

```text
http://localhost:8000
```

## Ejecutar pruebas

```bash
poetry run pytest
```

## Ejecutar lint

```bash
poetry run ruff check .
```
