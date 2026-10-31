import hashlib
import json
import os
from typing import Any

from redis.exceptions import RedisError

from services.redis_service import obter_cliente_redis


def criar_chave_cache(prefixo: str, dados: dict[str, Any]) -> str:
    """Cria uma chave previsivel, sem incluir URL ou dados do cliente em texto puro."""
    conteudo = json.dumps(dados, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
    identificador = hashlib.sha256(conteudo.encode("utf-8")).hexdigest()
    return f"fastnews:cache:{prefixo}:{identificador}"


def obter_cache(chave: str) -> Any | None:
    try:
        valor = obter_cliente_redis().get(chave)
        return json.loads(valor) if valor is not None else None
    except (RedisError, RuntimeError, ValueError, json.JSONDecodeError):
        # Cache e uma otimizacao: se o Redis estiver indisponivel, a rota continua funcional.
        return None


def salvar_cache(chave: str, valor: Any, ttl_segundos: int) -> None:
    try:
        obter_cliente_redis().set(chave, json.dumps(valor, ensure_ascii=False), ex=ttl_segundos)
    except (RedisError, RuntimeError, TypeError, ValueError):
        # Nao interrompe a consulta caso a instancia remota de Redis esteja indisponivel.
        pass


def obter_ttl(nome_variavel: str, padrao: int) -> int:
    try:
        return max(1, int(os.getenv(nome_variavel, str(padrao))))
    except ValueError:
        return padrao
