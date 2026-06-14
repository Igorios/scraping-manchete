from pydantic import BaseModel

class BuscandoEndereco(BaseModel):
    name: str
    urlSite: str