## What is this
A simple tool that creates mirror repos in your gitea instance from selected github organization

## Usage
Fill environment fields in **docker-compose.yml**:

- `GITEA_URL` should not have a tailing **/** symbol (`/api/v1` is added inside of script)
- `GITEA_ORG` and `GITHUB_ORG` are organization names you have access with `GITEA_TOKEN` and `GITHUB_TOKEN`
- `CRON_SPEC` should have valid crontab syntax

## Dockerhub
https://hub.docker.com/repository/docker/ergrassa/gitea-migrator
