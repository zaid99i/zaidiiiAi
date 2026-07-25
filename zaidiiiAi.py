import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

st.set_page_config(page_title="Zaidiii AI", page_icon="💬", layout="wide")

# CSS for ChatGPT look
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

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["type"] == "text":
            st.write(message["content"])
        elif message["type"] == "image":
            st.image(message["content"])

# Chat Input
if prompt := st.chat_input("Zaidiii se kuch bhi poocho ya photo banwao..."):

    st.session_state.messages.append({"role": "user", "type": "text", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Soch rahi hun..."):

            # Check if user wants an image
            if "photo" in prompt.lower() or "image" in prompt.lower() or "tasveer" in prompt.lower() or "banao" in prompt.lower():
                try:
                    model = genai.GenerativeModel('gemini-2.0-flash-exp-image-generation')
                    response = model.generate_content(prompt)
                    
                    # Find image in response
                    for part in response.parts:
                        if part.inline_data:
                            image = Image.open(io.BytesIO(part.inline_data.data))
                            st.image(image, caption="Ye rahi tumhari photo janiii ❤️")
                            st.session_state.messages.append({"role": "assistant", "type": "image", "content": image})
                            break
                except Exception as e:
                    st.error(f"Photo banane me error: {e}")
                    st.write("Janiii photo abhi nahi ban rahi. Text wala sawal poocho.")
            
            # Else do normal chat
            else:
                try:
                    # Sabse stable model
                    model = genai.GenerativeModel('gemini-1.0-pro')
                    response = model.generate_content(prompt)
                    st.write(response.text)
                    st.session_state.messages.append({"role": "assistant", "type": "text", "content": response.text})
                except Exception as e:
                    st.error(f"Chat ka Error: {e}")
