# Projeto Scraper

### Resumo
- Projeto simples com scraper em Python que coletam dados públicos e salvam em CSV.
  - [`scraper-g1.py`](scraper-g1.py) — pega manchetes do G1 e salva em `arquivos/manchetes-g1.csv`.


### Pré-requisitos
- Python 3.11+ (ou Docker)

### Rodando com Docker
- Build e run manual:
  - docker build -t projeto-scraping .
  - docker run --rm -v "$(pwd)":/app projeto-scraping
  - O container por padrão executa [`scraper-g1.py`](scraper-g1.py) conforme o [Dockerfile](Dockerfile).
- Usando docker-compose:
  - docker-compose up --build
  - Compose usando [docker-compose.yml](docker-compose.yml).
