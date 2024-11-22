#!/usr/bin/env python3
import logging
import app.logger
from langserve import add_routes
from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import load_dotenv
from app.chain.marketing_chain import donut_naming_agent

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # code before yield run before the app starts processing HTTP requests
    yield
    # code after yield run after the app stops processing HTTP requests and about to shutdown


fast_api_app = FastAPI(
    title="challenge-repo",
    version="0.10",
    description="This is repo contains the code for the challenge",
    lifespan=lifespan
)

add_routes(
    fast_api_app,
    donut_naming_agent,
    path="/recommendation"
)

if __name__ == "__main__":
    import uvicorn

    uvicorn_access_logger = logging.getLogger("uvicorn.access")
    uvicorn_access_logger.setLevel(logging.WARNING)
    uvicorn.run(fast_api_app, host="0.0.0.0", port=8080, log_config=None, loop="asyncio")
