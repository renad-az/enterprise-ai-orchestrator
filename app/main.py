from datetime import datetime, timezone
from uuid import uuid4

from fastapi import FastAPI

from app.schemas import RequestCreate, RequestResponse, RequestStatus


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


@app.post(
    "/requests",
    response_model=RequestResponse,
    status_code=201,
)
def create_request(request: RequestCreate):
    return RequestResponse(
        request_id=uuid4(),
        message="Request received successfully",
        status=RequestStatus.RECEIVED,
        created_at=datetime.now(timezone.utc),
        request=request,
    )