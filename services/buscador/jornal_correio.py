import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter, Retry

def buscar_jornal_correio(urlSite: str):
    response = requests.get(urlSite)
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
        response = session.get(urlSite, headers=headers, timeout=10)
    except requests.exceptions.Timeout:
        raise Exception("Timeout ao acessar o site G1!")
    except Exception as e:
        raise Exception(f"Erro ao acessar site: {e}")

    soup = BeautifulSoup(response.text, "html.parser")
    div_wrapper = soup.find("div", class_="s4n-wrapper")

    if div_wrapper:

        links = div_wrapper.find_all("a")

        for m in links:

            h3_tag = m.find("h3")
            titulo = h3_tag.get_text(strip=True)

            link = m.get("href")

            if not link:
                continue

            dados.append({
                "titulo": titulo,
                "link": link
            })

        return dados
    return None
