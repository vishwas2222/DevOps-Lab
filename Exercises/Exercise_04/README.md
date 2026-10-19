# Exercise 04: Docker Networking

## Objective

Build and verify a Flask REST API, MySQL database, and Redis cache connected through a custom Docker bridge network.

## Technologies Used

- Docker
- Python
- Flask
- MySQL
- Redis
- Windows CMD

## Project Structure

```text
Exercise_04/
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── screenshots/
```

## Docker Network

- **Network name:** `my-bridge-net`
- **Network driver:** `bridge`
- **Containers:** `flask`, `mysql`, and `redis`

## Flask API

The Flask API runs on port `5001`.

**Endpoint:** `http://localhost:5001/about`

**Method:** `GET`

Example response:

```json
{
  "description": "This is a simple REST API built with Flask.",
  "name": "Simple REST API",
  "version": "1.0"
}
```

## Docker Networking Demonstrations

### 1. Create the Network

```cmd
docker network create --driver bridge my-bridge-net
```

### 2. Build the Flask Image

```cmd
docker build -t flask-api .
```

### 3. Run MySQL

```cmd
docker run -d --name mysql --network my-bridge-net -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=devopsdb mysql:latest
```

### 4. Run Redis

```cmd
docker run -d --name redis --network my-bridge-net redis:latest
```

### 5. Run Flask

```cmd
docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api
```

### 6. Test the API

```cmd
curl.exe http://localhost:5001/about
```

### 7. Verify Service Discovery

```cmd
docker exec flask getent hosts mysql
docker exec flask getent hosts redis
```

### 8. Verify Redis

```cmd
docker exec -it redis redis-cli ping
```

Expected output: `PONG`

### 9. Verify MySQL

```cmd
docker exec -it mysql mysql -uroot -prootpass -e "SHOW DATABASES;"
```

The database list should include `devopsdb`.

## Key Learnings

- Created a custom Docker bridge network.
- Used Docker DNS to resolve container names.
- Published a container port using `-p 5001:5001`.
- Verified Flask, MySQL, and Redis.
- Demonstrated container name resolution on a shared Docker network.
- Learned the difference between host port publishing and internal container communication.

## Screenshots

The `screenshots/` folder contains evidence of network creation, image building, container execution, API testing, port mapping, and service discovery.
