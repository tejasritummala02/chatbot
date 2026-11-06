import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

model = os.getenv("OLLAMA_MODEL", "llama3.1:latest")
ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to user queries"),
        ("user", "Question: {question}"),
    ]
)

# Streamlit UI
st.set_page_config(page_title="LangChain Chatbot", layout="centered")
st.title("LangChain Chatbot with Ollama")

# Sidebar for model selection
st.sidebar.title("Model Settings")
# selected_model = st.sidebar.selectbox(
#     "Choose a model:",
#     options=["qwen2.5:3b", "llama2", "llama3.1:latest"],
#     index=0,
#     help="qwen2.5:3b runs much faster on CPU!"
# )

input_text = st.text_input("Search the topic you want", placeholder="Ask a question...")

# LangChain Chain
llm = Ollama(model=model, base_url=ollama_base_url)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    with st.spinner(f"Thinking with {model}..."):
        st.write_stream(chain.stream({"question": input_text}))
