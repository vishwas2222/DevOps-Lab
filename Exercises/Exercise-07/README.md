# Exercise 06: Real-Time Operations Monitoring and Alerting

## Objective

Build a real-time delivery operations monitoring system using Python, Docker, Prometheus, Grafana, and Jenkins to monitor delivery activity, collect metrics, visualize operational data, and define alerts.

## Tools Used

- Python
- Docker Desktop
- Prometheus
- Grafana
- Jenkins Pipeline

## Project Structure

```text
Exercise_06/
├── delivery_metrics.py
├── requirements.txt
├── Dockerfile
├── prometheus.yml
├── alert_rules.yml
├── Jenkinsfile
├── README.md
└── screenshots/
```

## Step 1: Python Application

The Python application simulates delivery activity and exposes Prometheus metrics.

**Metrics endpoint:** http://localhost:8000/metrics

### Metrics Collected

- `total_deliveries` — total number of deliveries processed.
- `pending_deliveries` — current number of pending deliveries.
- `on_the_way_deliveries` — number of deliveries currently on the way.
- `average_delivery_time` — histogram of delivery processing times.

### Install Dependencies

Run these commands from the `Exercise_06` directory:

```cmd
python -m pip install -r requirements.txt
```

### Run the Application Locally

```cmd
python delivery_metrics.py
```

Verify the application:

```cmd
curl.exe http://localhost:8000/
curl.exe http://localhost:8000/metrics
```

## Step 2: Docker Container

The Dockerfile packages the Python application and its dependencies into a Docker image.

### Build the Image

```cmd
docker build -t delivery-metrics .
```

### Run the Container

```cmd
docker run -d --name delivery-metrics -p 8000:8000 delivery-metrics
```

### Verify the Metrics Endpoint

```cmd
curl.exe http://localhost:8000/metrics
```

The response should contain the application metrics.

## Step 3: Prometheus Monitoring

Prometheus collects delivery metrics at five-second intervals. Its configuration is stored in `prometheus.yml`.

### Start Prometheus

Run this command from the `Exercise_06` directory:

```cmd
docker run -d --name prometheus -p 9090:9090 -v "%cd%\prometheus.yml:/etc/prometheus/prometheus.yml:ro" -v "%cd%\alert_rules.yml:/etc/prometheus/alert_rules.yml:ro" prom/prometheus
```

### Access Prometheus

http://localhost:9090

Open **Status → Targets** to check whether the delivery metrics target is being scraped successfully.

## Step 4: Alert Rules

The `alert_rules.yml` file defines alerts for delivery operations.

### HighPendingDeliveries

Triggers when `pending_deliveries` remains above 10 for 30 seconds.

### NoDeliveriesProcessed

Triggers when the increase in `total_deliveries` over a one-minute window is zero for one minute.

Alert rules can be inspected on the Prometheus Alerts page.

## Step 5: Grafana Dashboard

Grafana visualizes the metrics collected by Prometheus.

### Start Grafana

```cmd
docker run -d --name grafana -p 3000:3000 grafana/grafana
```

### Access Grafana

http://localhost:3000

Configure Prometheus as a data source using this URL when Grafana runs in Docker Desktop:

```text
http://host.docker.internal:9090
```

### Dashboard Configuration

Create a dashboard named **Delivery Operations Monitoring** with four Stat panels.

| Panel | Prometheus query |
|---|---|
| Total Deliveries | `total_deliveries` |
| Pending Deliveries | `pending_deliveries` |
| On the Way Deliveries | `on_the_way_deliveries` |
| Average Delivery Time | `average_delivery_time_sum / average_delivery_time_count` |

The average delivery time query returns the average observed processing time in seconds, provided at least one observation has been recorded.

## Step 6: Jenkins Pipeline

The `Jenkinsfile` defines a CI validation pipeline with the following stages:

1. Checkout/start message.
2. Required project file validation.
3. Python syntax validation.
4. Pipeline completion message.

The pipeline requires a Jenkins agent with a POSIX-compatible shell and Python 3 installed.

**Status:** The Jenkinsfile has been created, but the pipeline has not yet been executed or verified in Jenkins.

## Results

This exercise demonstrates:

- A Python application exposing delivery metrics.
- Application containerization using Docker.
- Prometheus metric collection and alert rule configuration.
- Grafana visualization of delivery operations.
- A Jenkins pipeline definition for project validation.

The Jenkins pipeline remains unverified until it is executed in a suitable Jenkins environment.

## Screenshots

The `screenshots/` directory contains evidence captured during the exercise, including application execution, dependency installation, Docker image and container verification, Prometheus configuration and targets, alert rules, Grafana dashboard creation, the Jenkinsfile, and this README.
