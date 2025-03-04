import streamlit as st
from main import process_question

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔍",
    layout="centered"
)

# st.markdown("""
#     <style>
#     .main {padding: 2rem;}
#     .stTextInput textarea {font-size: 16px;}
#     .stMarkdown {font-size: 16px;}
#     </style>
#     """, unsafe_allow_html=True)

st.title("🔍 AI Research Assistant")
st.write("Enter your research question below and get comprehensive answers powered by AI agents.")

with st.sidebar:
    st.header("Settings")
    model_choice = st.selectbox(
        "Select LLM",
        ["gemini-1.5-flash", "gemini-2.0-flash" , 'gemini-2.0-flash-lite'],
        index=0
    )

question = st.text_input(
    "Research Question:",
    placeholder="Enter your research question here...",
    label_visibility="collapsed"
)

if question:
    with st.spinner("Researching and drafting answer..."):
        try:
            answer = process_question(question, model_choice)
            st.subheader("Research Answer")
            st.markdown(f"**Question:** {question}")
            st.markdown("**Answer:**")
            st.write(answer)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")