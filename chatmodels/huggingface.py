from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm= HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1"
)


model=ChatHuggingFace(llm=llm, temperature=0.7)

response=model.invoke("tell me a joke not skeleton joke")
print(response.content)