import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

st.set_page_config(page_title="Zaidiii AI", page_icon="💬", layout="wide")

st.markdown("""
<style>
    .stChatMessage {border-radius: 15px; padding: 10px;}
    h1 {text-align: center; color: #4CAF50;}
</style>
""", unsafe_allow_html=True)

st.title("💬 Zaidiii AI - Tumhari Apni ChatGPT")

# API Key load
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("GOOGLE_API_KEY Secrets me nahi mili!")
    st.stop()

# Auto model dhoondo jo tumhari key pe chale
def get_working_model():
    for model_name in ['gemini-1.5-pro-latest', 'gemini-1.5-flash-latest', 'gemini-2.0-flash']:
        try:
            model = genai.GenerativeModel(model_name)
            return model
        except:
            continue
    return None

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["type"] == "text":
            st.write(message["content"])

if prompt := st.chat_input("Zaidiii se kuch bhi poocho..."):

    st.session_state.messages.append({"role": "user", "type": "text", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Soch rahi hun janiii..."):
            model = get_working_model()
            
            if model is None:
                st.error("Tumhari API key pe koi model nahi chal raha. AI Studio me jaake 'Enable Gemini API' karo.")
            else:
                try:
                    response = model.generate_content(prompt)
                    st.write(response.text)
                    st.session_state.messages.append({"role": "assistant", "type": "text", "content": response.text})
                except Exception as e:
                    st.error(f"Error: {e}")
