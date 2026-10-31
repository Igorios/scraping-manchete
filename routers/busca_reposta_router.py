from fastapi import APIRouter, Response
from pydantic import BaseModel
from typing import List

from components.controlador_site import controlador_site
from schemas.BuscarRespostaRequest import BuscarRespostaRequest
from services.cache_service import criar_chave_cache, obter_cache, obter_ttl, salvar_cache

router = APIRouter(prefix="/busca_resposta")

class Manchete(BaseModel):
    titulo: str
    link: str

class BuscarRespostaResponse(BaseModel):
    resposta: list[Manchete]

    class Config:
        orm_mode = True

@router.post("", response_model=List[Manchete])
def buscar_resposta(request: BuscarRespostaRequest, response: Response):
    chave_cache = criar_chave_cache(
        "manchetes",
        {"name": request.name, "urlSite": request.urlSite},
    )
    cache = obter_cache(chave_cache)

    if cache is not None:
        response.headers["X-Cache"] = "HIT"
        return cache

    respostas = controlador_site(request)
    salvar_cache(
        chave_cache,
        respostas,
        obter_ttl("CACHE_BUSCA_RESPOSTA_TTL_SECONDS", 60),
    )
    response.headers["X-Cache"] = "MISS"

    return respostas
