# LangChain Chatbot

A Streamlit chatbot powered by Groq.

## Deploy to Render

1. Create a Groq API key in the [Groq Console](https://console.groq.com/keys).
2. Push this project to GitHub and create or update its **Blueprint** in Render. Render reads `render.yaml`.
3. Enter the Groq API key as the `GROQ_API_KEY` environment variable when Render prompts for it. If needed, add it under the service's **Environment** settings. Keep the key secret; do not commit it to GitHub.
4. Deploy the service. To use a different model, set `GROQ_MODEL` to a model available to your Groq account.

Groq account availability, model access, and usage limits depend on Groq's current offerings.

## Run locally

Install the dependencies, set your Groq API key, and start Streamlit:

```powershell
pip install -r requirements.txt
$env:GROQ_API_KEY = "your-groq-api-key"
streamlit run llama.py
```

The app uses `llama-3.3-70b-versatile` by default. Override it with the `GROQ_MODEL` environment variable if needed.
