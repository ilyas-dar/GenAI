from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from langchain_mistralai import ChatMistralAI

from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

model=ChatMistralAI(model_name="open-mistral-7b", temperature=0.7)
print("^-^-----^-^ Wlcome to the Mistral AI Chatbot! ^-^-----^-^")
print("^-^-----^-^ Ask me anything! ^-^-----^-^")
print("^-^-----^-^ Type 'exit' to quit the chat. ^-^-----^-^")

history = [
    SystemMessage(content="You are a comedian by profession.")
]

while True:
    text=input("You: ")
    history.append(HumanMessage(content=text))
    if text.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break
    

    res=model.invoke(history)
    history.append(AIMessage(content=res.content))
    print(f"Bot: {res.content}")
print(history)
