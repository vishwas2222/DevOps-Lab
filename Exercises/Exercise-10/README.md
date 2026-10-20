# Exercise 10: Multi-Node Kubernetes Cluster with Multiple Applications and Replicasets

## Objective

Deploy two Flask applications to a three-node Minikube Kubernetes cluster.

- **Product Catalog:** 2 replicas; provides `GET /products`.
- **Shopping Cart:** 3 replicas; provides `GET /cart` and `POST /cart`.
- **Deployments:** Manage application replicas.
- **Pod anti-affinity:** Encourages replicas to run on different nodes.
- **NodePort Services:** Expose both applications.

## Architecture

```text
                    Windows Host
                         |
                   Docker Desktop
                         |
                Minikube: 3 Nodes
                         |
              Kubernetes Deployments
                    /          \
                   /            \
          Product Catalog     Shopping Cart
             2 replicas        3 replicas
                   |                |
             NodePort 30081    NodePort 30082
                   |                |
              GET /products     GET /cart
                               POST /cart
```

## Project Structure

```text
Exercise-10/
├── screenshots/
├── Dockerfile.product
├── Dockerfile.shopping
├── README.md
├── product_catalog.py
├── product_catalog_deployment.yaml
├── product_catalog_service.yaml
├── shopping_cart.py
├── shopping_cart_deployment.yaml
└── shopping_cart_service.yaml
```

## Prerequisites

- Docker Desktop
- Minikube
- kubectl
- Git
- Python (optional for local syntax checks)

## 1. Create the Three-Node Cluster

Clean up an old default Minikube profile if needed:

```cmd
minikube stop
minikube delete
```

Create the cluster:

```cmd
minikube start --nodes 3 -p devops-multinode --driver=docker
```

Verify the nodes:

```cmd
kubectl --context=devops-multinode get nodes
```

Enable the registry add-on:

```cmd
minikube -p devops-multinode addons enable registry
minikube -p devops-multinode addons list
```

## 2. Build the Docker Images

Run these commands from the `Exercise-10` directory:

```cmd
docker build -t product-catalog:latest -f Dockerfile.product .
docker build -t shopping-cart:latest -f Dockerfile.shopping .
docker images
```

## 3. Load Images into Minikube

```cmd
minikube -p devops-multinode image load product-catalog:latest
minikube -p devops-multinode image load shopping-cart:latest
minikube -p devops-multinode ssh -- sudo crictl images
```

Confirm that both images are available to the cluster nodes.

## 4. Deploy the Applications

Apply the Deployments:

```cmd
kubectl --context=devops-multinode apply -f product_catalog_deployment.yaml
kubectl --context=devops-multinode apply -f shopping_cart_deployment.yaml
```

Apply the Services:

```cmd
kubectl --context=devops-multinode apply -f product_catalog_service.yaml
kubectl --context=devops-multinode apply -f shopping_cart_service.yaml
```

## 5. Verify Deployments and Services

```cmd
kubectl --context=devops-multinode rollout status deployment/product-catalog
kubectl --context=devops-multinode rollout status deployment/shopping-cart
kubectl --context=devops-multinode get pods -o wide
kubectl --context=devops-multinode get deployments
kubectl --context=devops-multinode get services
kubectl --context=devops-multinode get endpoints shopping-cart-service
```

Expected replicas:

| Application | Desired replicas |
|---|---:|
| Product Catalog | 2 |
| Shopping Cart | 3 |

All five pods should reach `Running` state and become ready.

## 6. Access the Services

Start the Product Catalog service:

```cmd
minikube -p devops-multinode service product-catalog-service
```

Start the Shopping Cart service in a separate terminal:

```cmd
minikube -p devops-multinode service shopping-cart-service
```

Use the local tunnel URLs printed by Minikube. Keep the corresponding terminals open while testing.

## 7. Test Product Catalog

Replace the example port with the actual local tunnel port:

```cmd
curl http://127.0.0.1:YOUR_PRODUCT_PORT/products
```

Expected result: JSON containing Laptop, Phone, and Headphones.

Test the health endpoint:

```cmd
curl http://127.0.0.1:YOUR_PRODUCT_PORT/health
```

## 8. Test Shopping Cart

Replace the example port with the actual Shopping Cart tunnel port.

Retrieve the cart:

```cmd
curl http://127.0.0.1:YOUR_CART_PORT/cart
```

Add a Laptop:

```cmd
curl -X POST http://127.0.0.1:YOUR_CART_PORT/cart -H "Content-Type: application/json" -d "{\"id\":1,\"name\":\"Laptop\",\"quantity\":1}"
```

Retrieve the cart again:

```cmd
curl http://127.0.0.1:YOUR_CART_PORT/cart
```

### Testing Note

The Shopping Cart application stores items in memory. Each replica has separate memory, so requests routed to different replicas may return different cart contents.

For a consistent test against one pod, use port-forwarding:

```cmd
kubectl --context=devops-multinode port-forward service/shopping-cart-service 61908:80
```

Keep that terminal open. In another CMD window, run:

```cmd
curl http://127.0.0.1:61908/cart
```

Add the Laptop:

```cmd
curl -X POST http://127.0.0.1:61908/cart -H "Content-Type: application/json" -d "{\"id\":1,\"name\":\"Laptop\",\"quantity\":1}"
```

Retrieve the cart:

```cmd
curl http://127.0.0.1:61908/cart
```

The final response should contain the Laptop item.

Port-forwarding is a testing workaround, not a persistent shared-storage solution.

## 9. Screenshots

Save screenshots in the `screenshots/` directory.

| Screenshot | Description |
|---|---|
| `01-check-tools.png` | Verify Docker, Minikube, kubectl, and Git |
| `02-create-multinode-cluster.png` | Create and verify three nodes |
| `03-enable-minikube-registry.png` | Enable the registry add-on |
| `04-create-application-files.png` | Create the Flask applications and Dockerfiles |
| `05-build-application-images.png` | Build both Docker images |
| `06-list-local-docker-images.png` | List the local images |
| `07-verify-images-in-minikube.png` | Verify images inside Minikube |
| `08-create-deployment-files.png` | Create the Deployment manifests |
| `09-create-service-files.png` | Create the Service manifests |
| `10-apply-kubernetes-manifests.png` | Apply all four manifests |
| `11-verify-pods-and-deployments.png` | Verify replicas and pod placement |
| `12-verify-services-and-endpoints.png` | Verify Services and endpoints |
| `13-access-product-catalog-service.png` | Access Product Catalog |
| `14-test-product-catalog-endpoint.png` | Test `GET /products` |
| `15-access-shopping-cart-service.png` | Access Shopping Cart |
| `16-test-shopping-cart-endpoints.png` | Test cart GET and POST |

Use screenshots of your actual command output. If a screenshot has not yet been captured, take it before treating the checklist as complete.

## Conclusion

This exercise demonstrates how to containerize two Flask applications, deploy multiple replicas to a three-node Minikube cluster, expose the applications through NodePort Services, distribute replicas using pod anti-affinity, and verify the APIs using curl.

The Product Catalog and Shopping Cart APIs were tested successfully. The Shopping Cart's in-memory storage is replica-specific and is not intended as a production persistence solution.