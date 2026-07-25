import streamlit as st
from groq import Groq

st.set_page_config(page_title="Zaidiii", page_icon="🤖", layout="centered")

# MOBILE AESTHETIC CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    html, body, [class*="st"] { font-family: 'Poppins', sans-serif; }
 .stApp { background: linear-gradient(180deg, #FF5F6D 0%, #FFC371 100%); }
    #MainMenu, header, footer {visibility: hidden;}
 .welcome-box {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 35px 25px;
        text-align: center;
        margin: 30px 15px;
        border: 1px solid rgba(255,255,255,0.3);
        color: white;
    }
 .welcome-box h1 { color: white; font-size: 32px; font-weight: 700; }
    [data-testid="stChatMessage"] { background: rgba(255, 255, 255, 0.9); border-radius: 20px; padding: 15px 20px; margin: 12px 15px; }
    [data-testid="stChatMessageUser"] { background: #FF5F6D; color: white; }
    [data-testid="stChatInput"] { background: rgba(255, 255, 255, 0.95)!important; border-radius: 30px!important; padding: 15px 25px!important; margin: 0 15px 20px 15px; }
    [data-testid="stSidebar"] { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); }
</style>
""", unsafe_allow_html=True)

# Groq Client
try: client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except: st.error("GROQ_API_KEY Secrets me lagao janiii"); st.stop()

# Session state
if "messages" not in st.session_state: st.session_state.messages = []
if "mode" not in st.session_state: st.session_state.mode = "AI Chat"

def set_mode(mode):
    st.session_state.mode = mode
    st.session_state.messages = [] # mode change pe chat clear

# SIDEBAR - YAHAN SAB FUNCTIONS WAPIS HAIN 👇
with st.sidebar:
    st.title("🤖 Zaidiii")
    st.caption("Your Smart Assistant")

    st.markdown("### **Choose Mode**")
    if st.button("💬 AI Chat", use_container_width=True):
        set_mode("AI Chat")
    if st.button("📝 Write Copy", use_container_width=True):
        set_mode("Write Copy")
    if st.button("🖼️ Image Prompt", use_container_width=True):
        set_mode("Image Prompt")
    if st.button("💻 Write Code", use_container_width=True):
        set_mode("Write Code")
    if st.button("📊 Data Analysis", use_container_width=True):
        set_mode("Data Analysis")
    if st.button("✍️ Write Story", use_container_width=True):
        set_mode("Write Story")
    if st.button("📧 Email Writer", use_container_width=True):
        set_mode("Email Writer")
    if st.button("🌐 Translator", use_container_width=True):
        set_mode("Translator")

    st.divider()
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# MAIN WELCOME
st.markdown(f"""
<div class="welcome-box">
    <h1>🤖 Zaidiii</h1>
    <p><b>Active Mode: {st.session_state.mode}</b></p>
    <p>Main sun rahi hun janiii ❤️</p>
</div>
""", unsafe_allow_html=True)

# CHAT HISTORY
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]): st.write(msg["content"])

# INPUT
if prompt := st.chat_input(f"Zaidiii se poocho in {st.session_state.mode} mode..."):
    full_prompt = prompt

    # HAR MODE KE LIYE ALAG PROMPT
    if st.session_state.mode == "Write Copy":
        full_prompt = "Act as a professional copywriter. " + prompt
    elif st.session_state.mode == "Write Code":
        full_prompt = "Act as an expert programmer. Give clean code with comments. " + prompt
    elif st.session_state.mode == "Image Prompt":
        full_prompt = "Describe this image in detail for AI image generation: " + prompt
    elif st.session_state.mode == "Data Analysis":
        full_prompt = "Act as a data analyst. " + prompt
    elif st.session_state.mode == "Write Story":
        full_prompt = "Act as a creative storyteller. " + prompt
    elif st.session_state.mode == "Email Writer":
        full_prompt = "Write a professional email: " + prompt
    elif st.session_state.mode == "Translator":
        full_prompt = "Translate this to Urdu and English: " + prompt

    st.session_state.messages.append({"role": "user", "content": full_prompt})
    with st.chat_message("user"): st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🤖 Zaidiii soch rahi hai..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
