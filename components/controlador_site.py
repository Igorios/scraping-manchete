from schemas.BuscarRespostaRequest import BuscarRespostaRequest
from services.buscador import *

def controlador_site(request: BuscarRespostaRequest):

    match request.name:
        case "g1":
            return buscar_g1(request.urlSite)
        case _:
            return []

