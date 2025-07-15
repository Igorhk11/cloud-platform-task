Cloud-Platform-Task-App

What does this app do?
The goal of this application is to periodically checks the availability and response time of two external URLs (https://httpstat.us/503 and https://httpstat.us/200).
The app exposes these health checks as Prometheus-compatible metrics through a simple HTTP server, allowing you to monitor URL uptime and latency in real-time.

What to expect?
At the /metrics endpoint, you’ll see either:

sample_external_url_up{url="..."} = 1 means the URL is up (working).
sample_external_url_up{url="..."} = 0 means the URL is down (not working).

Please find the prerequisites for the Cloud-Platform-Task-App.

- Kubernetes cluster (e.g., Minikube)
- Helm 3+
- Docker installed and running

Steps
1. The first thing you would need to do is build and push Docker image:

docker build -t <your_dockerhub_username>/cloud-platform-task:latest .
docker push <your_dockerhub_username>/cloud-platform-task:latest

2. Update Docker image tag in chart/values.yaml

Set the image.repository and image.tag fields to your pushed image.

3. The third step is to Deploy Helm chart

helm install cloud-platform-task ./chart

4. Please verify deployment with below comands:

kubectl get pods
kubectl get svc

5. Forward the service port locally:

kubectl port-forward svc/cloud-platform-task 8000:8000

Then open http://localhost:8000/metrics in your browser.
