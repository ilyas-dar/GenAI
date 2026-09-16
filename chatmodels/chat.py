from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from langchain_mistralai import ChatMistralAI

model=ChatMistralAI(model_name="open-mistral-7b", temperature=0.7)

res=model.invoke("tell me a joke not skeleton joke")


print(res.content)