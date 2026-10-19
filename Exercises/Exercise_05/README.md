# Exercise 05: Docker Security with AppArmor and Python

## Objective

Build a Flask application in Docker, use the Docker SDK for Python, inspect container security options, and test restricted actions.

## Technologies Used

- Docker Desktop
- Python
- Flask
- Docker SDK for Python
- AppArmor (environment compatibility assessed)

## Project Structure

```text
Exercise_05/
├── app.py
├── Dockerfile
├── apply_apparmor.py
├── test_restricted_actions.py
├── README.md
└── screenshots/
```

## Flask Application

The Flask application listens on port `5000` and returns a greeting at `/`.

Test the application using:

```cmd
curl.exe http://localhost:5000/
```

## Build the Docker Image

```cmd
docker build -t flask-apparmor .
```

## Docker SDK for Python

Install the SDK:

```cmd
python -m pip install docker
```

Run the SDK verification script:

```cmd
python apply_apparmor.py
```

The script connects to Docker, displays the engine's security options, and checks whether the image exists.

## AppArmor Environment Check

The Docker engine reported these security options:

```text
name=seccomp,profile=builtin
name=cgroupns
```

The AppArmor kernel check returned `N`. Therefore, custom AppArmor enforcement could not be verified in this Docker Desktop environment.

## Restricted-Action Baseline Test

Run:

```cmd
python test_restricted_actions.py
```

### Observed Results

- Reading `/etc/passwd`: exit code `0` — succeeded.
- Executing `/bin/bash`: exit code `0` — succeeded.
- The test container was removed after testing.

These results represent baseline behavior without an enforced custom AppArmor profile. They do not demonstrate successful AppArmor restrictions.

## Key Learnings

- Built a Flask application and packaged it into a Docker image.
- Ran and tested the Flask application inside a container.
- Connected to Docker using the Python SDK.
- Inspected Docker engine security options.
- Tested file access and binary execution inside a container.
- Identified the AppArmor compatibility limitation in the current environment.

## Screenshots

The `screenshots/` directory contains evidence of the exercise setup, Docker image build, Flask application testing, Docker SDK verification, and restricted-action baseline testing.

## Conclusion

The Flask application and Docker SDK tests completed successfully. Custom AppArmor enforcement remains unverified because AppArmor was not enabled in the current Docker environment. A compatible Linux environment with AppArmor enabled is required to demonstrate the intended profile restrictions.
