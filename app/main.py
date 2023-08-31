from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from starlette.responses import RedirectResponse

from app.Presentation.GebeurtenissenRouter import gebeurtenissen_router
from app.Presentation.VariabelenRouter import variabelen_router

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

App.include_router(variabelen_router)
App.include_router(gebeurtenissen_router)


@App.get('/')
def redirect_to_docs():
    redirect_url = '/docs'  # replace with docs URL or use app.url_path_for()
    return RedirectResponse(url=redirect_url)


if __name__ == "__main__":
    uvicorn.run(App, host="0.0.0.0", port=8000)
