from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routers import busca_reposta_router
from routers import endereco_disponivel
from services.redis_service import obter_cliente_redis

app = FastAPI()

enderecos = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
    "https://fast-news.igorborgesweb.com",
    "https://console.cron-job.org"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=enderecos,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
def ping():
    return "pong"


@app.get("/redis/health")
def redis_health():
    try:
        obter_cliente_redis().ping()
    except Exception as erro:
        raise HTTPException(status_code=503, detail="Redis indisponivel") from erro

    return {"status": "ok", "redis": "conectado"}

app.include_router(busca_reposta_router.router)
app.include_router(endereco_disponivel.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
