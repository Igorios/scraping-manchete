from schemas.BuscandoEndereco import BuscandoEndereco

class EnderecoDisponivelService:

    def buscando_enderecos(self) -> list[BuscandoEndereco]:
        dados: list[BuscandoEndereco] = []

        sites = [
            {"name": "G1 Notícias", "urlSite": "https://g1.globo.com/"},
            {"name": "Jornal Correio", "urlSite": "https://www.correio24horas.com.br/"},
        ]

        for site in sites:
            dados.append(BuscandoEndereco(**site))

        return dados
        

