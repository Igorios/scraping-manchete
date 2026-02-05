from pydantic import BaseModel

class BuscarRespostaRequest(BaseModel):
    urlSite: str
    name: str