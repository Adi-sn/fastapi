# FastAPI Gemini AI Integration

A FastAPI application that integrates with Google's Gemini AI API to generate content based on user prompts.

## Features

- FastAPI backend server
- Google Gemini AI integration
- Environment variable support for API key management
- Simple REST API endpoints

## Prerequisites

- Python 3.8+
- FastAPI
- Pydantic
- python-dotenv
- requests

## Environment Setup

1. Create a virtual environment:
```bash
# Using venv
python -m venv venv

# Activate the virtual environment
# On Windows
.\venv\Scripts\activate

# On Unix or MacOS
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install fastapi uvicorn dotenv requests
```

3. Create a `.env` file in the root directory:
```bash
# Add your Gemini API key
GEMINI_API_KEY=your_api_key_here
```

## Project Setup

1. Clone the repository

2. Set up the environment (as described above)

3. Start the server:
```bash
uvicorn main:app --reload
```

## Usage

The API will be available at `http://localhost:8000`

### Available Endpoints

- `GET /`: Welcome message
- `GET /about`: About page information
- `GET /blog/{id}`: Get blog post by ID
- `POST /ask`: Send prompts to Gemini AI

### Making Requests to the Gemini AI Endpoint

Example request body for the `/ask` endpoint:
```json
{
  "contents": [
    {
      "parts": [
        {
          "text": "Write a story about a robot"
        }
      ]
    }
  ]
}
```

## Project Structure

```
├── venv/          # Virtual environment directory
├── main.py        # FastAPI application and routes
├── schemas.py     # Pydantic models for request/response validation
├── .env           # Environment variables (not tracked in git)
└── requirements.txt # Project dependencies
```

## Development Setup

1. Fork and clone the repository
2. Create and activate virtual environment
3. Install dependencies
4. Add `.env` file with your Gemini API key
5. Run the development server
