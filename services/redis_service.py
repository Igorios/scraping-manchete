import os
from functools import lru_cache

from dotenv import load_dotenv
from redis import Redis


load_dotenv()


def _ler_bool(nome: str, padrao: bool = False) -> bool:
    return os.getenv(nome, str(padrao)).strip().lower() in {"1", "true", "yes", "on"}


@lru_cache
def obter_cliente_redis() -> Redis:
    host = os.getenv("REDIS_HOST")
    senha = os.getenv("REDIS_PASSWORD")

    if not host or host == "SEU_IP_DA_VPS":
        raise RuntimeError("Defina REDIS_HOST no arquivo .env.")
    if not senha or senha == "SUBSTITUA_PELA_SENHA_DO_REDIS":
        raise RuntimeError("Defina REDIS_PASSWORD no arquivo .env.")

    return Redis(
        host=host,
        port=int(os.getenv("REDIS_PORT", "6379")),
        username=os.getenv("REDIS_USERNAME") or None,
        password=senha,
        db=int(os.getenv("REDIS_DB", "0")),
        ssl=_ler_bool("REDIS_SSL"),
        decode_responses=True,
        socket_connect_timeout=5,
        socket_timeout=5,
    )
