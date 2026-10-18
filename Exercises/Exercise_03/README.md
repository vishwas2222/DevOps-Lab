# Exercise 03: Scaling a Flask App Using Kubernetes ReplicaSets

## Objective

Deploy a Flask flash-sale application on Kubernetes and demonstrate replica management, scaling, health probes, and self-healing on a single-node Minikube cluster.

## Technologies Used

- Python 3.11
- Flask
- Gunicorn
- Docker Desktop
- Kubernetes
- Minikube
- kubectl
- Windows 11

## Application Endpoints

- `/` — Returns a welcome message, serving Pod hostname, and timestamp.
- `/buy` — Simulates a flash-sale purchase with a randomly selected product and user.
- `/health` — Returns the health status and Pod hostname.

## Project Structure

```text
Exercise_03/
├── app.py
├── Dockerfile
├── flashsale-replicaset.yaml
├── README.md
└── screenshots/
```

## 1. Build the Docker Image

```cmd
docker build -t yogeshg5/flashsale:1.0 .
```

Load the image into Minikube:

```cmd
minikube image load yogeshg5/flashsale:1.0
```

## 2. Deploy the ReplicaSet and Service

```cmd
kubectl apply -f flashsale-replicaset.yaml
```

Verify:

```cmd
kubectl get rs
kubectl get pods
kubectl get services
```

The initial ReplicaSet maintains three replicas.

## 3. Test the Application

Start port forwarding:

```cmd
kubectl port-forward service/flashsale-svc 8080:80
```

In another CMD window, test the endpoints:

```cmd
curl http://127.0.0.1:8080/
curl http://127.0.0.1:8080/buy
curl http://127.0.0.1:8080/health
```

## 4. Scale the ReplicaSet

Scale from three replicas to five:

```cmd
kubectl scale rs flashsale-rs --replicas=5
```

Verify:

```cmd
kubectl get rs flashsale-rs
kubectl get pods -o wide
```

## 5. Demonstrate Self-Healing

List the Flash Sale Pods:

```cmd
kubectl get pods -l app=flashsale
```

Delete one current Pod by its actual name:

```cmd
kubectl delete pod POD_NAME
```

Replace `POD_NAME` with the name of a Flash Sale Pod.

Verify that Kubernetes creates a replacement:

```cmd
kubectl get pods -l app=flashsale
kubectl get rs flashsale-rs
```

## 6. Observe Pod Placement

```cmd
kubectl get pods -o wide
kubectl get nodes
```

All five Flash Sale Pods should run on the single Minikube node.

## Key Learnings

1. A ReplicaSet maintains the desired number of Pods.
2. Scaling from three to five replicas creates two additional Pods.
3. Deleting a Pod causes the ReplicaSet to create a replacement.
4. The `kubectl get pods -o wide` command shows Pod IPs and node placement.
5. Readiness and liveness probes help Kubernetes monitor application health.

## Result

The Flask flash-sale application was containerized and deployed on Minikube. The ReplicaSet was scaled from three to five replicas, and deleting a Pod demonstrated Kubernetes self-healing.

## Screenshots

Screenshots documenting project setup, image building, deployment, endpoint testing, scaling, self-healing, and single-node placement are stored in the `screenshots/` directory.