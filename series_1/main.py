from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["GROQ_API_KEY"] =""


# prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. please response to the user queries"),
        ("user","Question :{question}")
    ]
)

# stremlit framework
st.title('Langchain network Created by Sangam')
input_text = st.text_input('Search the topic u want')

# grok llm
llm = ChatGroq(model="llama3-8b-8192")
output_parser = StrOutputParser()
chain =prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
