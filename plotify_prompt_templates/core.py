from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
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

para =input("Enter the poem or story to analyze: ")
print("Paste your poem or story. Type END on a new line when finished:")

lines = []

while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

para = "\n".join(lines)
final_prompt= prompt.invoke({"input": para})

model=ChatMistralAI(model_name="open-mistral-7b", temperature=0.7)
res=model.invoke(final_prompt)
print(res.content)


