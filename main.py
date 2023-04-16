from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import openai

openai.api_key = "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"

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
