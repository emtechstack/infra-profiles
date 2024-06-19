# EmTechStack Infra Profiles

Welcome to the EmTechStack Infra Profiles repository! This repository contains different profiles that can be used to build GenAI backend-ready AI applications with ease. Each profile represents a different combination of infrastructure components, such as databases and more.

## Getting Started

To get started with EmTechStack Infra Profiles, follow these steps:

1. Install `emtechstack`.

```sh
pip install --upgrade emtechstack
```

2. For inistiating profile you can use any profile in `profile/` directory. For example lets say you want to use `postgresql-qdrant-redis` profile which provides you Postgresql, Qdrant vector database and Redis, you can use this profile by this command

```sh
emtechstack init --profile postgresql-qdrant-redis --name your_project_name
```

3. Then you can go to your project dir `your_project_name` and build the project

```sh
cd your_project_name
emtechstack build
```

4. Then it will build an environment with installed requirements and libraries and ready to develop for you. You can start using the app by:

```sh
conda activate your_project_name
emtechstack start-infra
emteckstack start-api
```

5. For shut them down you can use:

```sh
emteckstack stop-api
emtechstack stop-infra
conda deactivate
```

or simply use:

```sh
emteckstack goodnight
conda deactivate
```

For more information check [EmTechStack](https://github.com/emtechstack/emtechstack).


## Available Profiles

| Profile Name              | Ingredients                            | Status     | Command to Run Profile                           |
|---------------------------|----------------------------------------|------------|-------------------------------------------------|
| postgres-qdrant-redis     | PostgreSQL, Qdrant Vector Database, Redis | Deprecated | `emtechstack init --profile postgres-qdrant-redis --name sample_app` |
| postgresql-qdrant-redis   | PostgreSQL, Qdrant Vector Database, Redis | Live       | `emtechstack init --profile postgresql-qdrant-redis --name sample_app` |


Choose the profile that aligns with your project requirements and explore its directory for more information.


## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the profiles as per the terms of the license.

For more information, please refer to the individual profile directories and their respective README files.
