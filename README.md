# Projeto Scraper

### Redis remoto
- Copie `.env.example` para `.env` e preencha `REDIS_HOST` e `REDIS_PASSWORD` com os dados do Redis na VPS.
- Nao ha container Redis neste projeto: tanto localmente quanto no deploy a API usa essa instancia remota.
- Apos instalar as dependencias e iniciar a API, acesse `GET /redis/health`. Essa rota executa `PING` no Redis remoto e retorna `200` apenas quando a conexao esta funcional.
- No deploy, mantenha o `.env` no servidor, ao lado do `docker-compose.yml`. Ele e injetado no container via `env_file`, mas fica fora do Git e da imagem Docker.
- Nao use `localhost` em `REDIS_HOST`, pois dentro do container ele aponta para a propria API. Use o IP privado ou DNS que o container consegue acessar.
- As respostas de `POST /busca_resposta` ficam em cache por 60 segundos por padrao. Altere `CACHE_BUSCA_RESPOSTA_TTL_SECONDS` no `.env` para mudar esse tempo. A resposta informa `X-Cache: MISS` na primeira consulta e `X-Cache: HIT` nas seguintes, enquanto o cache for valido.

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
