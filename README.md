# LocalRAG — Local-First Knowledge Intelligence Platform

**A privacy-focused, locally hosted Retrieval-Augmented Generation (RAG) platform for intelligent document search, contextual question answering, and evidence-grounded AI responses.**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688.svg)](https://fastapi.tiangolo.com/)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-black.svg)](https://ollama.com/)
[![Qdrant](https://img.shields.io/badge/Vector_DB-Qdrant-red.svg)](https://qdrant.tech/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Project Status:** In Development

## Overview

LocalRAG is a local-first AI knowledge intelligence platform designed to make private documents searchable and understandable using Retrieval-Augmented Generation.

Instead of relying entirely on an LLM's pretrained knowledge, LocalRAG retrieves relevant information from a user's own documents and provides that information as context to a locally hosted language model.

The system is designed to provide answers grounded in retrieved evidence, with references to the original documents.

The primary goal is to explore and implement production-oriented RAG architecture, including document processing, embedding generation, vector search, retrieval optimization, context construction, and evaluation.

## Why LocalRAG?

Traditional LLM applications can struggle with:

- Answering questions about private or domain-specific documents.
- Providing reliable references for generated answers.
- Handling large collections of documents.
- Retrieving relevant information from long documents.
- Maintaining control over sensitive information.
- Measuring retrieval and answer quality.

LocalRAG aims to address these challenges through a modular RAG architecture powered by locally hosted models.

## Key Features

### Document Intelligence
- Document ingestion and preprocessing.
- Support for PDF, DOCX, TXT and Markdown.
- Configurable text chunking strategies.
- Document metadata extraction.
- Document-level organization.

### Embedding and Retrieval
- Local embedding generation.
- Vector-based semantic search.
- Metadata filtering.
- Hybrid retrieval (keyword + semantic search).
- Configurable retrieval parameters.
- Optional reranking pipeline.

### Context-Aware Generation
- Integration with locally hosted LLMs through Ollama.
- Context-aware question answering.
- Source-grounded responses.
- Document references and citations.
- Configurable prompt templates.

### Evaluation and Observability
- Retrieval quality evaluation.
- Recall@K and Mean Reciprocal Rank (MRR).
- Answer faithfulness evaluation.
- Query latency tracking.
- Retrieval and generation logs.

*Features will be implemented incrementally. Refer to the roadmap for current development status.*

## Architecture

```mermaid
flowchart TD
    A[User] --> B[React Frontend]
    B --> C[FastAPI Backend]

    C --> D[Document Ingestion]
    D --> E[Text Extraction]
    E --> F[Chunking Engine]
    F --> G[Embedding Model]
    G --> H[(Qdrant Vector Database)]

    C --> I[Query Processing]
    I --> J[Retrieval Engine]
    J --> H
    J --> K[Hybrid Search]
    K --> L[Reranking]
    L --> M[Context Builder]
    M --> N[Ollama LLM]
    N --> O[Answer with Sources]
    O --> B
```

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, FastAPI |
| Frontend | React |
| LLM Runtime | Ollama |
| Language Model | Qwen / Llama |
| Embedding Model | nomic-embed-text |
| Vector Database | Qdrant |
| Relational Database | PostgreSQL |
| Containerization | Docker |
| Evaluation | Custom evaluation pipeline |

## How It Works

### 1. Document Ingestion

Users upload documents through the application. The ingestion pipeline extracts text and metadata from supported file formats.

### 2. Text Chunking

Extracted text is divided into smaller chunks using configurable chunk sizes and overlapping windows.

### 3. Embedding Generation

Each chunk is converted into a numerical vector using a locally hosted embedding model.

### 4. Vector Storage

Generated embeddings, document identifiers and metadata are stored in Qdrant.

### 5. Query Processing

When a user submits a question, the retrieval engine searches for relevant document chunks.

### 6. Context Construction

Retrieved chunks are filtered, ranked and assembled into a context window.

### 7. Response Generation

The locally hosted LLM generates an answer based on the retrieved context.

### 8. Source Attribution

The response includes references to the documents and relevant chunks used to construct the answer.

## Getting Started

### Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Ollama
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/localrag-knowledge-intelligence.git

cd localrag-knowledge-intelligence
```

### 2. Start Ollama

Install Ollama from https://ollama.com.

Pull the required models:

```bash
ollama pull qwen2.5-coder:1.5b
ollama pull nomic-embed-text
```

### 3. Start Qdrant

```bash
docker compose up -d qdrant
```

### 4. Configure Environment Variables

Create a `.env` file using `.env.example`.

```env
OLLAMA_BASE_URL=http://localhost:11434
LLM_MODEL=qwen2.5-coder:1.5b
EMBEDDING_MODEL=nomic-embed-text

QDRANT_URL=http://localhost:6333
QDRANT_COLLECTION=documents

DATABASE_URL=postgresql://user:password@localhost:5432/localrag
```

### 5. Install Dependencies

```bash
python -m venv .venv
```

Activate the virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
uvicorn app.main:app --reload
```

API documentation will be available at:

```text
http://localhost:8000/docs
```

*Setup commands and configuration will be finalized as the application is implemented.*

## Project Structure

```text
localrag/
│
├── app/
│   ├── api/
│   │   ├── routes/
│   │   └── dependencies.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   │
│   ├── ingestion/
│   │   ├── loaders.py
│   │   ├── parser.py
│   │   └── chunker.py
│   │
│   ├── embeddings/
│   │   └── provider.py
│   │
│   ├── retrieval/
│   │   ├── vector_search.py
│   │   ├── hybrid_search.py
│   │   └── reranker.py
│   │
│   ├── generation/
│   │   ├── llm_provider.py
│   │   ├── prompts.py
│   │   └── answer.py
│   │
│   ├── evaluation/
│   │   ├── retrieval_metrics.py
│   │   └── answer_metrics.py
│   │
│   └── main.py
│
├── frontend/
├── tests/
├── data/
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Development Roadmap

- [ ] Phase 1: Project setup and FastAPI foundation.
- [ ] Phase 2: Document ingestion and text extraction.
- [ ] Phase 3: Chunking and embedding generation.
- [ ] Phase 4: Qdrant integration and semantic retrieval.
- [ ] Phase 5: Local LLM integration through Ollama.
- [ ] Phase 6: Context-aware responses and source citations.
- [ ] Phase 7: Hybrid search and reranking.
- [ ] Phase 8: Retrieval and answer evaluation.
- [ ] Phase 9: React frontend and document management.
- [ ] Phase 10: Docker deployment and performance optimization.

## Evaluation Metrics

The system will be evaluated using a repeatable dataset of questions and expected relevant document chunks.

| Metric | Purpose |
|---|---|
| Recall@K | Measures retrieval coverage |
| MRR | Measures ranking quality |
| Precision@K | Measures retrieval relevance |
| Faithfulness | Measures grounding in retrieved context |
| Answer Relevance | Measures how well answers address questions |
| Latency | Measures end-to-end response time |

Actual benchmark results will be published after implementation and testing.

## Design Principles

1. **Local-first:** Run LLM inference and embedding generation locally.
2. **Modularity:** Keep ingestion, retrieval and generation independent.
3. **Traceability:** Make retrieved evidence visible to users.
4. **Evaluation-driven:** Measure system quality instead of relying on subjective responses.
5. **Extensibility:** Support alternative models and retrieval strategies.

## License

This project is licensed under the MIT License.

## Author

Developed as a hands-on AI Engineering project exploring Retrieval-Augmented Generation, local LLM inference, vector search, and production-oriented AI system design.