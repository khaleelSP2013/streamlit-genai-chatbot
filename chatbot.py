from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

# streamlit page setup

st.set_page_config(
    page_title="Gen AI ChatBot", 
    page_icon="💬.",
    layout="centered",
    ) 

st.title("💬 Gen AI ChatBot")

# initialize the ChatGroq model with the API key from environment variables
#chat_history = []

if("chat_history" not in st.session_state):
    st.session_state.chat_history = []

#show the chat history if it exists
if st.session_state.chat_history:
    for  message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# initialize the ChatGroq model with the API key from environment variables            
llm = ChatGroq(
   model="llama-3.3-70b-versatile",
    temperature=0.0,
)

# input box for user input
user_prompt = st.chat_input("Ask ChatBot...") 

if user_prompt:
    # Append user input to chat history
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    response = llm.invoke(
        input=[{"role": "user", "content": "You are helpful assistant. "}, *st.session_state.chat_history] 
    )

    # show and save the assistant's response
    assistant_response = response.content

    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
    
    with st.chat_message("assistant"):
        st.markdown(assistant_response)




