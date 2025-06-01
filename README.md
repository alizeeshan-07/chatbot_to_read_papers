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
## Summary Workflow

1. **User Input:**  
   User types a query in the chatbot prompt (e.g., "Find papers on federated learning").

2. **Send Query to Claude:**  
   The query, along with the description of available tools, is sent to the Anthropic Claude API.

3. **Claude Response:**  
   Claude processes the query and decides whether it can answer directly or needs to call an external tool.

4. **Tool Invocation:**  
   - If a tool is required (e.g., `search_papers`), Claude returns a request specifying the tool and input arguments.  
   - The chatbot runs the corresponding Python function locally.

5. **Return Tool Results:**  
   The output from the tool function is sent back to Claude as part of the conversation context.

6. **Final Response:**  
   Claude generates the final answer based on the tool output and returns it to the user.

7. **Repeat:**  
   The chatbot waits for the next user query until the user types 'quit' to exit.

---

This workflow enables the chatbot to dynamically leverage external Python functions for up-to-date and detailed information retrieval.
