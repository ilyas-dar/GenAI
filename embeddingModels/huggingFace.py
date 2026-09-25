from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L12-v2"
)
text=[
    "hey there! how have you been doing? I hope you are doing well. I am doing good too. ",
    "I have been working on a project and it has been going well.",
    "I have been learning a lot and I am excited to see the results. I hope you are having a great day!"
]

vector_embedding = embedding_model.embed_documents(text)
print(vector_embedding)

