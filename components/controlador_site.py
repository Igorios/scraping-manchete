from schemas.BuscarRespostaRequest import BuscarRespostaRequest
from services.buscador import *

def controlador_site(request: BuscarRespostaRequest):

    match request.name:
        case "G1 Notícias":
            return buscar_g1(request.urlSite)
        case "Jornal Correio":
            return buscar_jornal_correio(request.urlSite)
        case _:
            return []

