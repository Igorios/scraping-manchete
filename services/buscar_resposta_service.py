import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter, Retry

class BuscarRespostaService:

    def buscando_resposta_site(self, url: str):
        response = requests.get(url)
        dados = []

        if response.status_code != 200:
            print("Erro ao acessar site!")
            raise Exception("Erro ao acessar site!")

        session = requests.Session()

        retry_strategy = Retry(
            total=5,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504]
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("https://", adapter)
        session.mount("http://", adapter)

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8",
            "Referer": "https://www.google.com/"
        }

        try:
            response = session.get(url, headers=headers, timeout=10)
        except requests.exceptions.Timeout:
            raise Exception("Timeout ao acessar o site G1!")
        except Exception as e:
            raise Exception(f"Erro ao acessar site: {e}")

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