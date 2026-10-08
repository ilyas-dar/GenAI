# GenAI Learning Repository

A personal repository where I document my journey of learning Generative AI, Large Language Models (LLMs), Hugging Face, LangChain, and related tools.

The goal of this repository is not to build production-ready applications, but to understand concepts step by step, experiment with different technologies, and maintain code examples that I can revisit later.

## Current Learning Focus

* Working with chat models
* Using Hugging Face models
* Running local LLMs
* Understanding model downloads and caching
* Learning LangChain fundamentals
* Prompt Templates
* ChatPromptTemplate
* Prompt Engineering
* Building simple Streamlit interfaces

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
│   ├── core.py
│   └── coreUI.py
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
* Make requests using LangChain integrations
* Understand the difference between local and hosted inference

### Local Models with Hugging Face Pipeline

Learned how to:

* Download models locally
* Load models using Hugging Face pipelines
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
* Work with different model providers through a common API
* Send prompts to hosted and local models
* Build reusable LLM workflows

### Prompt Templates

Learned how to:

* Create reusable prompts using `ChatPromptTemplate`
* Separate system instructions from user input
* Use variables inside prompts
* Generate prompts dynamically
* Build information extraction workflows

Example:

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])
```

### Prompt Engineering

Practiced:

* Designing clear system instructions
* Structuring output formats
* Information extraction tasks
* Content analysis workflows
* Improving response consistency through prompt design

### Streamlit Basics

Learned how to:

* Create simple web interfaces for LLM applications
* Accept user input through forms
* Trigger model execution with buttons
* Display model responses in a browser
* Connect LangChain applications to a UI

## Mini Projects and Experiments

### Plotify Prompt Templates

A small prompt engineering project built while learning LangChain Prompt Templates.

The project simulates a fictional company called **Plotify** that receives poems and short stories from users and analyzes them using an LLM.

Current features:

* Title extraction
* Type detection
* Genre classification
* Summary generation
* Theme identification
* Character extraction
* Setting identification
* Tone analysis
* Mood analysis
* Keyword extraction
* Emotion detection
* Tag generation

Files:

* `core.py` – Prompt template and LangChain workflow
* `coreUI.py` – Streamlit interface

### Chat Model Experiments

Contains examples exploring:

* Basic chat interactions
* Hugging Face hosted models
* Local model execution
* Chatbot development concepts

## Learning Roadmap

### Completed

* Chat Models
* Hugging Face Endpoint Models
* Hugging Face Pipelines
* Local Model Execution
* Model Downloading
* Model Caching
* Environment Variables
* LangChain Chat Interfaces
* Local vs Hosted LLMs

### Currently Learning

* Prompt Templates
* ChatPromptTemplate
* Prompt Engineering
* Streamlit Integration

### Next Topics

* Structured Outputs
* Output Parsers
* Embeddings
* Chains
* Vector Databases
* FAISS
* Retrieval Augmented Generation (RAG)

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

The focus is learning, understanding, and documenting progress rather than building production-ready systems.
