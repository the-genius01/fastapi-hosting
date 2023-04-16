from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

#openai.api_key = "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"


openai.organization = "org-Fjb39r5N9zfTvgdoeasm0OLi"
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class SearchRequest(BaseModel):
    query: str

class SearchResponse(BaseModel):
    response: str

@app.post("/", response_model=SearchResponse)
def search(request: SearchRequest) -> SearchResponse:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=request.query,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5
    )
    return SearchResponse(response=response.choices[0].text)
