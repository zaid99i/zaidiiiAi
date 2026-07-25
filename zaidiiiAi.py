import streamlit as st

st.set_page_config(page_title="zaidiiiAi", page_icon="🤖")
st.title("🤖 zaidiiiAi")
st.write("Assalamualaikum! Main tumhara AI dost hun ❤️")

user_input = st.text_input("Kuch bhi poocho:")
if st.button("Bhejo"):
    st.write("Tumne kaha: " + user_input)