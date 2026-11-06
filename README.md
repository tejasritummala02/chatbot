# LangChain Chatbot

A Streamlit chatbot that uses an Ollama model.

## Deploy to Render

1. Push this project to a GitHub repository and create a new **Blueprint** in Render using that repository. Render will detect `render.yaml`.
2. Set `OLLAMA_BASE_URL` to the URL of your reachable Ollama server, including its port (for example, `https://ollama.example.com`).
3. Deploy the service. Set `OLLAMA_MODEL` in the Render environment if you want a model other than `llama3.1:latest`.

The Ollama server must be reachable from Render and have the selected model available. Do not expose an unauthenticated Ollama endpoint directly to the public internet; use a secured network path or an authenticated HTTPS proxy.

## Run locally

Install the dependencies and start Streamlit:

```powershell
pip install -r requirements.txt
streamlit run llama.py
```

By default, the app connects to Ollama at `http://localhost:11434` using `llama3.1:latest`. Override these with the `OLLAMA_BASE_URL` and `OLLAMA_MODEL` environment variables.
