
import docker

client = docker.from_env()

print("Docker connection successful.")
print("Docker security options:", client.info().get("SecurityOptions", []))

try:
    client.images.get("flask-apparmor")
    print("Image flask-apparmor exists.")
except docker.errors.ImageNotFound:
    print("Image not found. Build it first with: docker build -t flask-apparmor .")
