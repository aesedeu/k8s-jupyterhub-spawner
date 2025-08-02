# Jupyter Hub

Настройка spawner: https://jupyterhub.readthedocs.io/en/5.2.1/reference/api/index.html

- Запускаем minikube
- Собираем образ и пушим к себе, но тогда указываем актуальную ссылку на образ в Docker Hub:
```bash
docker build -t aesedeu/k8s-spawner:1.0 .
docker push aesedeu/k8s-spawner:1.0   
```
а также в файле `values.yaml` редактируем:
```yaml
image:
    name: aesedeu/k8s-spawner
    tag: "1.0"
    pullPolicy: Always
```


- Запускаем JupyterHub
```bash
cd jupyterhub-chart
kubectl create namespace jh
helm upgrade --cleanup-on-fail \
    --install jupyterhub \
    --namespace jh \
    -f values.yaml \
    .
```
- Выполняем проброс портов
```bash
kubectl port-forward svc/proxy-public -n jh 8080:80
```
- Для удаления проекта выполняем:
```bash
helm uninstall jupyterhub -n jh
```