
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# GET endpoints ==================================================
@app.get("/")
def root():
    return {"message": "Hello World!!"}

# path parameters are defined with curly braces {} in the path
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello {name}!"}

@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    result = num1 + num2
    return {"result": result}

#query parameters are defined as function parameters with default values
@app.get("/search")
def search(keyword: str, limit: int = 5):
    return {
        "keyword": keyword,
        "limit": limit,
        "message": f"Searching for {keyword}, showing {limit} results"
    }

# POST endpoints ==================================================

# Step 1 — describe what data you expect
class QuestionRequest(BaseModel):
    question: str

# Step 2 — describe what data you will return
class QuestionResponse(BaseModel):
    question: str
    answer: str

# Step 3 — POST endpoint
@app.post("/ask", response_model=QuestionResponse)
def ask(request: QuestionRequest):
     # Error 1 — empty question
    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    # Error 2 — question too short
    if len(request.question) < 3:
        raise HTTPException(
            status_code=400,
            detail="Question too short, minimum 3 characters"
        )

    # All good — process it
    answer = f"You asked: {request.question}"
    return QuestionResponse(
        question=request.question,
        answer=answer
    )

# Error Handling ============================================
# Fake database
books = {
    "1": "Python basics",
    "2": "LangChain guide",
    "3": "RAG systems"
}

@app.get("/book/{book_id}")
def get_book(book_id: str):

    # Check empty
    if not book_id.strip():
        raise HTTPException(
            status_code=400,
            detail="Book ID cannot be empty"
        )

    # Check exists
    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail=f"Book {book_id} not found"
        )

    # Success — 200 returned automatically
    return {"book_id": book_id, "title": books[book_id]}
