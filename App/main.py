from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from App.Data.DatabaseConnector import DatabaseConnector
from App.Models.BerekendeVar import BerekendeVar

app = FastAPI()

dbc = DatabaseConnector()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# define a model to validate the request body
class CellUpdate(BaseModel):
    row: int
    col: int
    role: str


# define the game grid
game_grid = [["empty" for _ in range(30)] for _ in range(30)]

# configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/db")
async def get_items_from_database(request: Request):
    return dbc.DatabaseConnector.connect(dbc.DatabaseConnector(), "select * from AlleVariabelen")


# handle POST requests to /update-cell
@app.post("/update-cell")
async def update_cell(cell: CellUpdate):
    game_grid[cell.row][cell.col] = cell.role
    return {"message": "Cell updated successfully"}


@app.post("/db")
async def updateBerekendeVar(newVar: BerekendeVar):
    newVar.printValues()
    return "all good!"
