# Knowledge Intelligence System

## Project Description

The goal of this project is to build a Retrieval-Augmented Generation (RAG)–based Knowledge Intelligence System that allows users to ingest, organize, search, and converse with their internal documents and data sources using a conversational AI interface. The system combines a vector-based retrieval layer with a Large Language Model (LLM) to provide accurate, context-aware answers grounded in the user’s knowledge base, while offering an admin-friendly interface for managing content and monitoring usage.

---

## Features

- Retrieval-Augmented Generation (RAG) pipeline
- Conversational AI interface for querying documents
- Vector-based semantic search using embeddings
- OpenAI LLM integration
- Document ingestion and storage
- AWS S3 storage integration
- Conversational memory with LangChain
- Flask-based API and UI
- Dockerization and CI/CD ready structure

---

## Tech Stack

- Python 3.10
- Flask
- LangChain
- OpenAI API
- ChromaDB (Vector Store)
- AWS S3
- HTML / CSS
- Docker

---


---

## Implementation Flow

### Section 1: Foundations & Architecture
- Introduction to Project
- Project Architecture
- Project Setup
- Project Structure Creation

### Section 2: Cloud Infrastructure & Storage
- Create S3 Bucket & Get AWS Access Keys
- LLM Configuration & Conversational Retrieval Chain

### Section 3: Core AI Implementation
- Implementation of AWS S3 Storage Service
- Implementation of Vector Store

### Section 4: API, UI & Deployment
- Implementation of Final Endpoint
- Implementation of Flask API & UI
- Dockerization and CI/CD Deployment

---

## Installation

### Clone Repository
git clone <your-repo-url>
cd knowledge-intelligence-system
Create Environment
conda create -n llmapp310 python=3.10 -y
conda activate llmapp310
Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables

### Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_REGION=your_region
▶️ Run Application
python app/main.py

### Open in browser:

http://127.0.0.1:8080
📂 Project Structure
app/
 ├── models/
 ├── services/
 ├── templates/
 ├── static/
 ├── main.py
 └── config.py

data/
README.md
requirements.txt

## Author

Sneha Priyadarshini S S
