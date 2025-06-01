# Arxiv Chatbot

A chatbot application that searches and extracts research paper information from arXiv using the Anthropic Claude API.

## Features

- Search arXiv papers by topic and store metadata locally  
- Extract detailed information about a specific paper by ID  
- Conversational interface powered by Anthropic Claude API  
- Dockerized for easy deployment  

## Setup Instructions

### Local Python Environment

1. Create and activate a Python virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file with your Anthropic API key:

    ```
    ANTHROPIC_API_KEY=your_api_key_here
    ```

4. Run the chatbot:

    ```bash
    python chatbot.py
    ```

### Using Docker

1. Build the Docker image:

    ```bash
    docker build -t arxiv_papers_chatbot .
    ```

2. Run the container (make sure `.env` is in your project root):

    ```bash
    docker run -it --env-file .env arxiv_papers_chatbot
    ```

## Project Structure

```
chatbot.py         — Main script to run the chat loop  
paper_tools.py     — Functions to search and extract paper info  
tool_mapping.py    — Tool definitions and execution logic  
requirements.txt   — Python dependencies  
Dockerfile         — Docker build instructions  
.env               — Environment variables (not committed)  
papers/            — Directory where paper info is saved  
```
