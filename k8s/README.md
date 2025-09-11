# FastAPI Kubernetes Deployment

## Get k8s creds

```bash
az login --tenant 4635f316-0e74-4570-8cec-23a86045b000 --use-device-code
az account set --subscription ba826c91-8e52-4e07-ac7c-538858bbc813
az aks get-credentials --resource-group 1000_data_engineering_workshop --name mhpdeworkshop_aks --overwrite-existing
```

## Build and Tag Image with podman

```bash
podman build -t fastapi:1.0.0 .
podman tag fastapi:1.0.0 dataengineeringworkshop.azurecr.io/fastapi:1.0.0
```

### Run Image Locally (Optional)

```bash
podman run --name fastapi -d -p 8000:8000 fastapi:1.0.0
```

### Push image to ACR

```bash
podman login dataengineeringworkshop.azurecr.io # (enter credentials when prompted)
podman push dataengineeringworkshop.azurecr.io/fastapi:1.0.0
```

## Deployment

To deploy the FastAPI application on Kubernetes, use the following command:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

To delete the deployment, use:

```bash
kubectl delete -f k8s/deployment.yaml
```

To get all pods, use:

```bash
kubectl get pods
```

To check the logs of the deployed pod, use:

```bash
kubectl logs <pod-name>
```
