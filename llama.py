import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to user queries"),
        ("user", "Question: {question}"),
    ]
)

# Streamlit UI
st.set_page_config(page_title="LangChain Chatbot", layout="centered")
st.title("LangChain Chatbot with Groq")

st.sidebar.title("Model Settings")

input_text = st.text_input("Search the topic you want", placeholder="Ask a question...")

# LangChain Chain
llm = ChatGroq(model=model)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    with st.spinner(f"Thinking with {model}..."):
        st.write_stream(chain.stream({"question": input_text}))
