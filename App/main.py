from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# define a model to validate the request body
class CellUpdate(BaseModel):
    row: int
    col: int
    role: str

# define the game grid
game_grid = [["empty" for _ in range(5)] for _ in range(5)]

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

# handle POST requests to /update-cell
@app.post("/update-cell")
async def update_cell(cell: CellUpdate):
    game_grid[cell.row][cell.col] = cell.role
    return {"message": "Cell updated successfully"}
