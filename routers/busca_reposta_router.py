from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from services.buscar_resposta_service import BuscarRespostaService

router = APIRouter(prefix="/busca_resposta")

class Manchete(BaseModel):
    titulo: str
    link: str

class BuscarRespostaResponse(BaseModel):
    resposta: list[Manchete]

    class Config:
        orm_mode = True

class BuscarRespostaRequest(BaseModel):
    urlSite: str


@router.post("", response_model=List[Manchete])
def buscar_resposta(request: BuscarRespostaRequest):

    servico = BuscarRespostaService()

    respostas = servico.buscando_resposta_site(request.urlSite)

    return respostas