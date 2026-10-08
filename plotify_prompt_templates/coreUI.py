from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

import streamlit as st

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You work for Atlas Storyworks.

        Analyze the poem or story provided by the user.

        Extract:
        - Title
        - Type
        - Genre
        - Summary
        - Main Theme
        - Key Characters
        - Setting
        - Tone
        - Mood
        - Important Keywords
        - Major Emotions
        - Tags

        Keep the analysis concise.
        """
    ),
    (
        "user",
        "{input}"
    )
])

st.title("Atlas Storyworks")

para = st.text_area(
    "Enter your poem or story",
    height=300
)

if st.button("Analyze"):

    final_prompt = prompt.invoke({"input": para})

    model = ChatMistralAI(
        model_name="open-mistral-7b",
        temperature=0.7
    )

    res = model.invoke(final_prompt)

    st.write(res.content)