from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

import Data.DatabaseConnector

app = FastAPI()


dbc = Data.DatabaseConnector


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
async def get_items_from_database(id1: int = None):
    print(str(id1))
    return dbc.DatabaseConnector.connect(dbc.DatabaseConnector(), "select * from variabelen where nummer = " + str(id1))


# handle POST requests to /update-cell
@app.post("/update-cell")
async def update_cell(cell: CellUpdate):
    game_grid[cell.row][cell.col] = cell.role
    return {"message": "Cell updated successfully"}
