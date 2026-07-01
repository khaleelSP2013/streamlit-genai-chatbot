from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

# streamlit page setup

st.set_page_config(
    page_title="Gen AI ChatBot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# layout 
st.markdown("""
<div class="custom-header">
    <h2 style="margin:0;">
        🤖 Gen AI ChatBot
    </h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Hide Streamlit default menu/footer/header */
#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* App Background */
.stApp{
    background:#F4F7FC;
}

/* ================= HEADER ================= */

.custom-header{
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:65px;

    background:#1E3A5F;
    color:white;

    border-bottom:0.5px solid #2D4F73;

    display:flex;
    align-items:center;

    padding:0 25px;

    z-index:9999;

    box-shadow:0 2px 6px rgba(0,0,0,.15);
}

/* ================= FOOTER ================= */

.custom-footer{
    position:fixed;

    left:0;
    bottom:0;

    width:100%;
    height:45px;

    background:#1E3A5F;
    color:white;

    border-top:0.5px solid #2D4F73;

    display:flex;
    justify-content:center;
    align-items:center;

    font-size:14px;

    z-index:9999;
}

/* ================= MAIN CONTENT ================= */

/* Prevent header/footer from covering content */
.block-container{
    padding-top:85px !important;
    padding-bottom:70px !important;
}

/* ================= SCROLLBAR ================= */

::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-track{
    background:#F4F7FC;
}

::-webkit-scrollbar-thumb{
    background:#2D4F73;
    border-radius:10px;
}

::-webkit-scrollbar-thumb:hover{
    background:#1E3A5F;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="custom-footer">
    © 2026 &nbsp;|&nbsp; Powered by Streamlit • LangChain • Groq
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>

.stChatInput {
    position: fixed;
    bottom: 50px;
    left: 0;
    right: 0;
    padding: 12px 30px;
    
    z-index:9998;
}

.stChatInput > div{
    background:white;
    border:1px solid #2D4F73;
    border-radius:20px;
    box-shadow:0 4px 12px rgba(30,58,95,.15);
}

.stChatInput textarea{
    font-size:16px;
   
}

.stChatInput button{
    background:#1E3A5F;
    color:white;
    border-radius:50%;
    width:40px;
    height:40px;
}

.stChatInput button:hover{
    background:#2D4F73;
}

</style>
""", unsafe_allow_html=True)

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




