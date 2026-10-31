from fastapi import APIRouter, Response
from typing import List
from schemas.BuscandoEndereco import BuscandoEndereco
from services.endereco_disponivel_service import EnderecoDisponivelService
from services.cache_service import criar_chave_cache, obter_cache, obter_ttl, salvar_cache

router = APIRouter(prefix="/endereco_disponivel")

@router.get("", response_model=List[BuscandoEndereco])
def buscar_enderecos(response: Response):
    chave_cache = criar_chave_cache("enderecos-disponiveis", {})
    cache = obter_cache(chave_cache)

    if cache is not None:
        response.headers["X-Cache"] = "HIT"
        return cache

    service = EnderecoDisponivelService()
    enderecos = service.buscando_enderecos()
    salvar_cache(
        chave_cache,
        [endereco.model_dump() for endereco in enderecos],
        obter_ttl("CACHE_ENDERECOS_TTL_SECONDS", 300),
    )
    response.headers["X-Cache"] = "MISS"
    return enderecos
