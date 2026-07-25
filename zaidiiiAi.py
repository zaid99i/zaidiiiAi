import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Zaidiii AI", page_icon="✨")
st.title("✨ Zaidiii AI")
st.caption("ChatGPT Style AI")

# 1. Key check karo
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
    st.sidebar.success("API Key Connected ✅")
except Exception as e:
    st.error(f"API Key ka masla hai: {e}")
    st.stop()

# 2. Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 3. Chat input
if prompt := st.chat_input("Zaidiii se poocho..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Soch rahi hun..."):
            try:
                # Sabse stable model use kar rahe
                model = genai.GenerativeModel('gemini-1.0-pro') 
                response = model.generate_content(prompt)
                st.write(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
             File "/mount/src/zaidiiiai/zaidiiiAi.py", 
  
                  ^

