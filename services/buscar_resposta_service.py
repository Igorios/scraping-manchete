import requests
from bs4 import BeautifulSoup

class BuscarRespostaService:

    def buscando_resposta_site(self, url: str):
        response = requests.get(url)
        dados = []

        if response.status_code != 200:
            print("Erro ao acessar site!")
            raise Exception("Erro ao acessar site!")

        soup = BeautifulSoup(response.text, "html.parser")
        manchetes = soup.find_all("a", class_="feed-post-link")

        for m in manchetes:
            titulo = m.get_text(strip=True)
            link = m.get("href") or ""

            dados.append({
                "titulo": titulo,
                "link": link
            })

        return dados