\# Exercise 02: Flask Application on Kubernetes



\## Objective



Deploy a simple Flask web application in a Docker container and run it on a local Kubernetes cluster using Minikube.



\## Technologies Used



\- Python 3.8

\- Flask

\- Docker Desktop

\- Kubernetes

\- Minikube

\- Windows 11

\- kubectl



\## Project Structure



```text

Exercise\_02/

├── app.py

├── Dockerfile

├── flask-deployment.yaml

├── README.md

└── screenshots/

&#x20;   ├── 01-minikube-start.png

&#x20;   ├── 02-flask-app.png

&#x20;   ├── 03-dockerfile.png

&#x20;   ├── 04-docker-build.png

&#x20;   ├── 05-image-loaded.png

&#x20;   ├── 06-kubernetes-yaml.png

&#x20;   ├── 07-pod-running.png

&#x20;   ├── 08-flask-logs.png

&#x20;   ├── 09-service.png

&#x20;   └── 10-flask-response.png

```



\## 1. Start Minikube



Start the local Kubernetes cluster:



```cmd

minikube start --driver=docker

```



Verify the cluster:



```cmd

kubectl get nodes

```



The Minikube node should show `Ready`.



\## 2. Create the Flask Application



The `app.py` file contains a simple Flask application that returns a message when accessed.



```python

from flask import Flask



app = Flask(\_\_name\_\_)



@app.route("/")

def home():

&#x20;   return "Hello from Flask on Kubernetes!"



if \_\_name\_\_ == "\_\_main\_\_":

&#x20;   app.run(host="0.0.0.0", port=15000)

```



\## 3. Create the Docker Image



The Dockerfile uses Python 3.8, installs Flask, copies the application, and starts the server on port 15000.



Build the Docker image:



```cmd

docker build -t flask-app:latest .

```



Verify the image:



```cmd

docker images flask-app

```



\## 4. Load the Image into Minikube



Load the locally built image into the Minikube cluster:



```cmd

minikube image load flask-app:latest

```



Verify the available images:



```cmd

minikube image ls

```



\## 5. Deploy the Application



The `flask-deployment.yaml` file defines a Kubernetes Deployment with one replica and a NodePort Service.



Apply the configuration:



```cmd

kubectl apply -f flask-deployment.yaml

```



Check the Deployment:



```cmd

kubectl get deployments

```



Check the Pods:



```cmd

kubectl get pods

```



Check the Service:



```cmd

kubectl get services

```



\## 6. Verify the Application



Check the Flask application logs:



```cmd

kubectl logs -l app=flask-app

```



Get the service URL:



```cmd

minikube service flask-app-service --url

```



Use the URL returned by Minikube to test the application. For this setup, the successful response was verified with:



```cmd

curl http://127.0.0.1:63147

```



Expected response:



```text

Hello from Flask on Kubernetes!

```



Note: The local port returned by Minikube can change. Use the URL printed by the command rather than assuming the same port every time.



\## 7. Screenshots



The `screenshots/` directory contains evidence of the following steps:



1\. Minikube cluster started successfully.

2\. Flask application source code.

3\. Dockerfile configuration.

4\. Docker image build.

5\. Image loaded into Minikube.

6\. Kubernetes Deployment and Service YAML.

7\. Flask Pod running.

8\. Flask application logs.

9\. Kubernetes Service details.

10\. Successful Flask response using curl.



\## Result



The Flask application was successfully containerized using Docker and deployed to a local Kubernetes cluster using Minikube. The Pod reached the `Running` state, the Deployment became available, and the application returned the expected response through the Kubernetes Service.



\## Conclusion



This exercise demonstrates the basic workflow of building a Docker image, loading it into Minikube, deploying a containerized application on Kubernetes, exposing it through a NodePort Service, and verifying the application using curl.

