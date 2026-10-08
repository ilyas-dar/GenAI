from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# ---------- Page setup ----------
st.set_page_config(page_title="Mistral AI Chatbot", page_icon="🎭")
st.title("🎭 Mistral AI Chatbot")
st.caption("Ask me anything! I'm a comedian by profession.")


# ---------- Model (created once, reused across reruns) ----------
@st.cache_resource
def get_model():
    return ChatMistralAI(model_name="open-mistral-7b", temperature=0.7)


model = get_model()

# ---------- Chat history (kept in session state) ----------
SYSTEM_PROMPT = "You are a comedian by profession."

if "history" not in st.session_state:
    st.session_state.history = [SystemMessage(content=SYSTEM_PROMPT)]

# ---------- Sidebar ----------
with st.sidebar:
    st.header("Options")
    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.history = [SystemMessage(content=SYSTEM_PROMPT)]
        st.rerun()

# ---------- Show previous messages ----------
for msg in st.session_state.history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# ---------- Handle new input ----------
if prompt := st.chat_input("Type your message..."):
    # Show and store the user's message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.history.append(HumanMessage(content=prompt))

    # Stream the bot's reply
    with st.chat_message("assistant"):
        try:
            def stream_reply():
                for chunk in model.stream(st.session_state.history):
                    yield chunk.content

            reply = st.write_stream(stream_reply())
            st.session_state.history.append(AIMessage(content=reply))
        except Exception as e:
            st.error(f"Something went wrong: {e}")
            # Remove the unanswered user message so history stays consistent
            st.session_state.history.pop()