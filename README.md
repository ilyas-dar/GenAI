# GenAI Learning Repository

A personal repository where I document my journey of learning Generative AI, Large Language Models (LLMs), Hugging Face, and LangChain.

The goal of this repository is not to build a complete application, but to understand the fundamentals step by step and maintain code examples that I can revisit later.

## Current Learning Focus

* Working with chat models
* Using Hugging Face models
* Running local LLMs
* Understanding model downloads and caching
* Learning LangChain fundamentals
* Experimenting with different model interfaces

## Project Structure

```text
GenAI/
├── README.md
├── chatmodels
│   ├── chat.py
│   ├── huggingface.py
│   └── localmodel.py
├── embeddingModels
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

## Learning Roadmap

### Completed

* Chat Models
* Hugging Face Endpoint
* Hugging Face Pipeline
* Local Model Execution
* Model Downloading
* Model Caching
* Environment Variables

### Currently Learning

* LangChain Chat Interfaces
* Local vs Hosted LLMs

### Next Topics

* Prompt Templates
* ChatPromptTemplate
* Output Parsers
* Chains
* Embeddings
* Vector Databases
* FAISS
* Retrieval Augmented Generation (RAG)

## Resources

### LangChain Documentation

Official Documentation:

[LangChain Documentation](https://python.langchain.com/docs/introduction/?utm_source=chatgpt.com)

Prompt Templates Reference:

[LangChain PromptTemplate Reference](https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate?utm_source=chatgpt.com)

LangChain explains Prompt Templates as reusable templates that accept variables and generate prompts dynamically.

### Additional Learning Resource

Microsoft's LangChain for Beginners:

[LangChain for Beginners (Microsoft)](https://github.com/microsoft/langchain-for-beginners/blob/main/03-prompts-messages-outputs/README.md?utm_source=chatgpt.com)

This resource covers chat models, prompt templates, structured outputs, chains, agents, and RAG systems.

## Notes

This repository is intentionally beginner-friendly.

Code may change frequently as I learn new concepts, refactor examples, and experiment with different models and LangChain components.

The focus is learning, understanding, and documenting progress rather than building a production-ready system.
