from fastapi import APIRouter
from typing import List
from schemas.BuscandoEndereco import BuscandoEndereco
from services.endereco_disponivel_service import EnderecoDisponivelService

router = APIRouter(prefix="/endereco_disponivel")

@router.get("", response_model=List[BuscandoEndereco])
def buscar_enderecos():
    service = EnderecoDisponivelService()
    enderecos = service.buscando_enderecos()
    return enderecos