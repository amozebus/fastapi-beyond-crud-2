<div align="center">

# FastAPI Beyond CRUD 2 (with PostgreSQL)

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

Template for API that uses [PostgreSQL](https://postgresql.org)-database. Written in [Python](https://python.org) with [FastAPI](https://fastapi.tiangolo.com), [asyncpg](https://github.com/MagicStack/asyncpg) as database client, [SQLModel](https://sqlmodel.tiangolo.com) as ORM

Included [Alembic](https://alembic.sqlalchemy.org) for database migrations

Users' passwords hashing with [BCrypt](https://en.wikipedia.org/wiki/Bcrypt) and users authorization with access [JWTs](https://jwt.io)

</div>

## How to run

1. Rename `.env.example` to `.env` and fill fields

    * Fields:

    ```
    DATABASE_URL (str): PostgreSQL-database URL

    JWT_SECRET (str): secret for JWTs signature

    ACCESS_TOKEN_EXPIRE (int): access JWTs expire time in seconds
    ```

2. Install dependencies:

```sh
pip install -r requirements.txt
```

3. Run database migrations:

```sh
alembic upgrade head
```

3. Run app:

```sh
python src/main.py
```

### Docker

2. Build Docker image:

```sh
docker build . --tag api
```

3. Run Docker image:

```sh
docker run -d api
```

4. Run database migrations:

```sh
docker exec {container id} alembic upgrade head
```