from pydantic import BaseModel

class BuscarRespostaRequest(BaseModel):
    name: str
    urlSite: str