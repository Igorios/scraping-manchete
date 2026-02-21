import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter, Retry

def _criar_sessao():
    session = requests.Session()
    retry_strategy = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def buscar_jornal_correio(urlSite: str):
    response = requests.get(urlSite)
    response_rota_brasil = requests.get(urlSite + "/brasil")

    dados = []

    if response.status_code != 200:
        print("Erro ao acessar site!")
        raise Exception("Erro ao acessar site!")

    session = _criar_sessao()

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
        response = session.get(urlSite, headers=headers, timeout=10)
    except requests.exceptions.Timeout:
        raise Exception("Timeout ao acessar o site G1!")
    except Exception as e:
        raise Exception(f"Erro ao acessar site: {e}")

    # pagina inicial
    soup = BeautifulSoup(response.text, "html.parser")
    soup_rota_brasil = BeautifulSoup(response_rota_brasil.text, "html.parser")

    div_wrapper = soup.find("div", class_="s4n-wrapper")
    div_rota_brasil = soup_rota_brasil.find("div", class_="lista--container")

    # pagina inicial
    if div_wrapper:
        links = div_wrapper.find_all("a")

        for m in links:
            h3_tag = m.find("h3")
            if not h3_tag:
                continue

            titulo = h3_tag.get_text(strip=True)
            link = m.get("href")

            if not link:
                continue

            dados.append({
                "titulo": titulo,
                "link": link
            })

    # pagina /brasil
    if div_rota_brasil:
        links = div_rota_brasil.find_all("a")

        for m in links:
            h2_tag = m.find("h2")
            if not h2_tag:
                continue

            titulo = h2_tag.get_text(strip=True)
            link = m.get("href")

            if not link:
                continue

            dados.append({
                "titulo": titulo,
                "link": link
            })

    return dados
