import streamlit as st
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables (for local testing)
load_dotenv()

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🤖 Simple LangChain + Groq Chatbot")

user_input = st.text_input("Ask me anything:")

def query_groq(question):
    llm = ChatGroq(
        temperature=0.7,
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile"  # ✅ Supported model
    )
    messages = [
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content=question)
    ]
    response = llm.invoke(messages)
    return response.content

if user_input:
    with st.spinner("Thinking..."):
        answer = query_groq(user_input)
    st.success("**Answer:** " + answer)
