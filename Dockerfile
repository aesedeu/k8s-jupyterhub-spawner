FROM jupyterhub/k8s-hub:3.1.0

LABEL authors="Eugene Chernov"
LABEL telegram="https://t.me/awe_eu"

LABEL description="JupyterHub for Kubernetes with custom spawner"

USER root

COPY . .
RUN pip install .

USER 1000