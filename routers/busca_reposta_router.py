from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from components.controlador_site import controlador_site
from schemas.BuscarRespostaRequest import BuscarRespostaRequest

router = APIRouter(prefix="/busca_resposta")

class Manchete(BaseModel):
    titulo: str
    link: str

class BuscarRespostaResponse(BaseModel):
    resposta: list[Manchete]

    class Config:
        orm_mode = True

@router.post("", response_model=List[Manchete])
def buscar_resposta(request: BuscarRespostaRequest):

    respostas = controlador_site(request)

    return respostas