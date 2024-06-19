## PostgreSQL, Qdrant, Redis
In this profile you can use `postgresql` database, `qdrant` vector database and `redis` as part of your infra. 


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
