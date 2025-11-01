import streamlit as st
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

st.title("💬 LangChain Chatbot with Groq")

prompt = st.text_input("Ask me anything:")

if st.button("Get Answer") and prompt:
    llm = ChatGroq(temperature=0, model="llama-3.1-8b-instant", groq_api_key=groq_api_key)
    messages = [
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content=prompt),
    ]
    response = llm.invoke(messages)
    st.write("**Answer:**", response.content)
