

<p align="center">
  <a href="https://code.visualstudio.com/">
    <img src="https://code.visualstudio.com/assets/images/code-stable.png" alt="VSCode" width="100" height="100"/>
  </a>
  <a href="https://www.postgresql.org/">
    <img src="https://avatars.githubusercontent.com/u/177543?s=200&v=4" alt="PostgreSQL" width="100" height="100"/>
  </a>
  <a href="https://redis.io/">
    <img src="https://redis.io/wp-content/uploads/2024/04/Logotype.svg?auto=webp&quality=85,75&width=120" alt="Redis" width="100" height="100"/>
  </a>
  <a href="https://qdrant.tech/">
    <img src="https://github.com/qdrant/qdrant/raw/master/docs/logo.svg" alt="Qdrant" width="150" height="100"/>
  </a>
</p>



## PostgreSQL, Qdrant, Redis
In this profile you can use `postgresql` database, `qdrant` vector database and `redis` as part of your infra. 

## Ingrediants & Project Dependencies

| Library                | Version  | Description                                                      |
|------------------------|----------|------------------------------------------------------------------|
| `emtechstack`          | `latest`      | A custom library for emerging technologies stack management.     |
| `fastapi`              | `0.111.0`| A modern, fast (high-performance) web framework for building APIs.|
| `langchain`            | `0.2.5`  | Library for chaining language models together.                   |
| `langchain-community`  | `0.2.5`  | Community-driven extensions for langchain.                       |
| `langchain-openai`     | `0.1.8`  | OpenAI integration for langchain.                                |
| `langchain-qdrant`     | `0.1.1`  | Qdrant integration for langchain.                                |
| `langchainhub`         | `0.1.20` | A hub for langchain components and models.                       |
| `langgraph`            | `0.0.69` | A library for creating and manipulating language agents.         |
| `openai`               | `1.35.1` | OpenAI API client library.                                       |
| `python-dotenv`        | `0.21.0` | Reads key-value pairs from a .env file and sets them as environment variables. |
| `requests`             | `2.32.3` | Simple, yet elegant HTTP library.                                |
| `sse-starlette`        | `2.0.0`  | Server-Sent Events for Starlette.                                |
| `streamlit`            | `1.35.0` | A faster way to build and share data apps.                       |



### Installation
1. Install [Python](https://www.python.org/downloads/)
2. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
3. Install [Docker](https://www.docker.com/get-started)
4. Install [EmTeckStack CLI](https://github.com/emtechstack/emtechstack):

```sh
pip install --upgrade emtechstack
```

5. Get the profile:

```sh
emtechstack init --profile postgresql-qdrant-redis --name your_app_name
```

6. Go to your app and build it:

```sh
cd your_app_name/
emtechstack build
```

activate the virtual environment

```sh
conda activate your_app_name
```

7. Run Infra and the App:

```sh
emtechstack update
emtechstack start-infra
emtechstack start-api
```

For stop them:

```sh
emtechstack stop-api
emtechstack stop-infra
```

or simply use

```sh
emtechstack goodnight
```

Thanks
