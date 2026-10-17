# Expenses App

## Docker Setup

Requires Docker Engine and the Docker Compose plugin. Create a root `.env`
from `.env.example` if one does not already exist and set `POSTGRES_PASSWORD`
to a private value. Compose uses the same credentials for the database and API;
no separate `DATABASE_URL` is needed for this stack.

### Start the Application

Run from the project root (the directory containing `compose.yaml`) to build
and start the frontend, backend, and database in the background, waiting until
the services are ready:

```sh
docker compose up --build -d --wait
```

Check the running services:

```sh
docker compose ps
```

Open http://localhost:8080 (or the `FRONTEND_PORT` configured in `.env`).
This is a deployment-style build, not a hot-reloading development server.

## Service Communication

```text
Browser -> localhost:8080 -> frontend (nginx)
                               /api/* -> backend:8000 -> db:5432
```

Only nginx is published, on localhost. Compose provides private service-name
DNS for `backend` and `db`. The browser must use relative `/api/...` URLs, not
Docker service names. nginx strips `/api/` before forwarding requests, so
`/api/expence/add` reaches `/expence/add`. Same-origin requests need no CORS
configuration. Neither PostgreSQL nor the backend is exposed to the host.

The frontend currently uses mock expenses in local state. This stack establishes
API/database connectivity; wiring UI actions to the API is separate work.

PostgreSQL must be healthy before the API starts. The API creates missing tables
on startup and its healthcheck queries PostgreSQL. This is not a schema migration
system; existing table changes need a migration strategy.

## Verification

```sh
curl --fail http://localhost:8080/
curl --fail http://localhost:8080/api/health
curl --fail http://localhost:8080/api/openapi.json
docker compose exec db sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "\dt"'
```

`/api/health` returns `{"status":"ok"}` only if the backend can query the database.

## Operations

```sh
docker compose logs -f
docker compose up --build -d --wait
docker compose down
```

Database data is stored in the `postgres_data` named volume and survives normal
shutdowns and container replacement. `docker compose down --volumes` permanently
deletes that data; do not use it unless you intend to reset the database.

PostgreSQL credentials initialize a new volume only. Changing `.env` does not
change credentials in an existing database. Do not attach older PostgreSQL data
directories to this PostgreSQL 17 volume without a supported migration.

The older `docker-compose.test.yml` and `Database/docker-compose.yml` are legacy
configurations. Use the root `compose.yaml` with the commands above.

For public deployment, add HTTPS, backups, and review application authentication
and API validation first. The current stack is bound to localhost intentionally.
