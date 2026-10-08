# GenAI Learning Repository

A personal repository where I document my journey of learning Generative AI, Large Language Models (LLMs), Hugging Face, and LangChain.

The goal of this repository is not to build a complete application, but to understand the fundamentals step by step and maintain code examples that I can revisit later.

## Current Learning Focus

* Working with chat models
* Using Hugging Face models
* Running local LLMs
* Understanding model downloads and caching
* Learning LangChain fundamentals
* Prompt Engineering
* Prompt Templates
* ChatPromptTemplate
* Embeddings
* Building simple chatbot applications

## Project Structure

```text
GenAI/
├── README.md
├── chatmodels
│   ├── UI_chatbot.py
│   ├── chat.py
│   ├── chatbot.py
│   ├── huggingface.py
│   └── localmodel.py
├── embeddingModels
│   └── huggingFace.py
├── plotify_prompt_templates
│   └── core.py
├── pyproject.toml
├── requirements.txt
├── src
│   └── genai
│       └── __init__.py
├── test.py
└── uv.lock
```

## What I Have Learned So Far

### Hugging Face Endpoint Models

Learned how to:

* Connect LangChain with Hugging Face hosted models
* Use API tokens securely with `.env`
* Make requests using `ChatHuggingFace`
* Understand the difference between local and hosted inference

### Local Models with Hugging Face Pipeline

Learned how to:

* Download models locally
* Load models using `HuggingFacePipeline`
* Run inference without API costs
* Understand Hugging Face model caching

Example model:

* TinyLlama/TinyLlama-1.1B-Chat-v1.0

### Model Caching

Discovered that models are downloaded only once and stored locally.

Example cache location:

```bash
~/.cache/huggingface/hub
```

After the first download, future executions reuse the cached model.

### Environment Variables

Learned how to store API keys securely using:

```env
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

and load them with:

```python
from dotenv import load_dotenv
import os

load_dotenv()
```

### LangChain Chat Models

Learned how to:

* Use LangChain chat model interfaces
* Send prompts to different providers
* Work with hosted and local models through a common API
* Build reusable LLM workflows

### Prompt Templates

Learned how to:

* Create reusable prompts using `PromptTemplate`
* Use variables inside prompts
* Separate instructions from user input
* Generate dynamic prompts from templates

Example concept:

```python
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple terms."
)
```

### ChatPromptTemplate

Learned how to:

* Build chat-style prompts with system and user messages
* Create reusable conversational templates
* Inject user input dynamically
* Structure prompts for chatbot and extraction tasks

Example concept:

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])
```

### Embeddings

Currently experimenting with:

* Text embeddings
* Converting text into vector representations
* Understanding similarity search foundations
* Preparing for vector databases and RAG systems

### Mini Projects and Experiments

#### Chatbots

Built simple chatbot examples to understand:

* User interaction loops
* Prompt-response workflows
* Chat model integration
* Terminal-based chatbot interfaces

#### Plotify Prompt Templates

Experimenting with prompt templates through a fictional company scenario where stories and poems are analyzed to extract:

* Title
* Genre
* Summary
* Theme
* Tone
* Mood
* Keywords
* Tags

This project is used to understand prompt engineering and structured information extraction.

## Learning Roadmap

### Completed

* Chat Models
* Hugging Face Endpoint
* Hugging Face Pipeline
* Local Model Execution
* Model Downloading
* Model Caching
* Environment Variables
* LangChain Chat Interfaces
* Local vs Hosted LLMs

### Currently Learning

* Prompt Templates
* ChatPromptTemplate
* Basic Prompt Engineering

### Next Topics

* Structured Outputs


### Next Topics

* Chains
* Vector Databases
* FAISS
* Retrieval Augmented Generation (RAG)
* Document Loaders
* Text Splitters
* Retrieval Chains

## Resources

### LangChain Documentation

Official Documentation:

https://python.langchain.com/docs/introduction/

Prompt Templates Reference:

https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate

### Additional Learning Resource

Microsoft's LangChain for Beginners:

https://github.com/microsoft/langchain-for-beginners

This resource covers chat models, prompt templates, structured outputs, chains, agents, and RAG systems.

## Notes

This repository is intentionally beginner-friendly.

Code may change frequently as I learn new concepts, refactor examples, and experiment with different models and LangChain components.

The focus is learning, understanding, and documenting progress rather than building a production-ready system.
