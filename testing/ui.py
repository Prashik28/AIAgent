import streamlit as st
import random
import time


#Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi! I am in the making.. ",
            "Hi! Can you please be more specific"
        ]
    )

    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("AI SQUILLE CHAT")

#Initialize chat History
if "messages" not in st.session_state:
    st.session_state.messages = []


#Display chant messages from history on app rerun 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


#Accept user input
if prompt := st.chat_input("Ask a question?"):
    #Add user message to the chat history
    st.session_state.messages.append({"role":"user","content": prompt})
    #Display user message in chat meassage container
    with st.chat_message("user"):
        st.markdown(prompt)

    #Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    
    #Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})