
import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://g1.globo.com/"
url = BASE_URL

response = requests.get(url)
dados = []

if response.status_code != 200:
    print("Erro ao acessar site!")
    exit()

if url:
    soup = BeautifulSoup(response.text, "html.parser")
    manchetes = soup.find_all("a", class_="feed-post-link")
    
    for m in manchetes:
        titulo = m.get_text(strip=True)
        link = m.get("href")
        
        dados.append({
            "Titulo da manchete": titulo,
            "Link da manchete": link
        })


df = pd.DataFrame(dados)
#df.to_excel("data/manchetes-g1.xlsx", index=False, engine="openpyxl")
df.to_csv("arquivos/manchetes-g1.csv",index=False, encoding="utf-8")

print(f"{len(dados)} manchetes encontradas")




