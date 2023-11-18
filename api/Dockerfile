FROM python:3.9 AS builder

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY ./src /api

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "80", "--reload"]

# FROM builder as dev-envs

# RUN <<EOF
# apt-get update
# apt-get install -y --no-install-recommends git
# EOF

# RUN <<EOF
# useradd -s /bin/bash -m vscode
# groupadd docker
# usermod -aG docker vscode
# EOF
# # install Docker tools (cli, buildx, compose)
# COPY --from=gloursdocker/docker / /

