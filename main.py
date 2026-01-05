from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routers import busca_reposta_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
def ping():
    return "pong"

app.include_router(busca_reposta_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8082)