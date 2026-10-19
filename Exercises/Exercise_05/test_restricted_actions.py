
import docker

client = docker.from_env()
container = None

try:
    container = client.containers.run(
        "flask-apparmor",
        detach=True,
        name="apparmor-action-test"
    )

    print("Container started:", container.short_id)

    result = container.exec_run(
        ["python", "-c", "print(open('/etc/passwd').read())"]
    )
    print("Read /etc/passwd exit code:", result.exit_code)
    print(result.output.decode(errors="replace"))

    result = container.exec_run(
        ["/bin/bash", "-c", "echo Bash executed"]
    )
    print("Execute Bash exit code:", result.exit_code)
    print(result.output.decode(errors="replace"))

except docker.errors.APIError as e:
    print("Docker API error:", e)

finally:
    if container is not None:
        container.remove(force=True)
        print("Container removed.")
