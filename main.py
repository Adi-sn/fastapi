from fastapi import FastAPI
import schemas
import os
from dotenv import load_dotenv
import requests


load_dotenv()
app=FastAPI()

@app.get('/')
def index():
    return 'Hello, World!'

@app.get('/about')
def about():
    return {'data': 'About page'}

@app.get('/blog/{id}')
def blog(id: int):
    return {'data': f"this is blog {id}"}

@app.post('/ask')
def create(body : schemas.content):
    api=os.getenv('GEMINI_API_KEY')
    if not api:
        return {'error':'key not found'}
    
    response= requests.post(f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api}',json = body.model_dump())
    ans = response.json()
    try:
        answer= ans['candidates'][0]['content']['parts'][0]['text']
    except:
        answer = "Error: Could not extract Gemini response."

    return {"answer": answer}