from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from app.Data.DatabaseConnector import DatabaseConnector
from app.Models.BerekendeVar import BerekendeVar
from app.APIRouters.RESTtest import router

App = FastAPI()



origins = [
    "http://localhost",
    "http://localhost:3000",
]

App.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

App.include_router(router)


if __name__ == "__main__":
    uvicorn.run(App, host="0.0.0.0", port=8000)






