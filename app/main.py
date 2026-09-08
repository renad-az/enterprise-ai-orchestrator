from fastapi import FastAPI

from app.schemas import RequestCreate


app = FastAPI(
    title="Enterprise AI Request & Approval Orchestrator",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Enterprise AI Orchestrator API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "version": "0.1.0",
    }


@app.post("/requests", status_code=201)
def create_request(request: RequestCreate):
    return {
        "message": "Request received successfully",
        "status": "RECEIVED",
        "request": request,
    }