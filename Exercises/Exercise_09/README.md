# Exercise 09: Jenkins Multi-Stage Pipeline for a Flask Application

## Objective

To implement a Jenkins Declarative Pipeline that automates the build, testing, deployment preparation, and execution of a Flask web application through multiple stages.

## Technologies Used

- Jenkins
- Python 3
- Flask
- Git and GitHub
- Jenkins Declarative Pipeline
- Windows CMD for local testing

## Project Structure

```text
Exercise-09/
├── app.py
├── requirements.txt
├── test_app.py
├── Jenkinsfile
├── README.md
└── screenshots/
```

## Application Details

The Flask application exposes a `/` endpoint that returns the following message:

```text
Hello, Jenkins Multi-Stage Pipeline!
```

### Dependencies

The `requirements.txt` file contains the following dependencies:

- `Flask==2.1.2`
- `Werkzeug==2.1.2`

## Pipeline Stages

The Jenkins pipeline consists of five stages:

1. **Build:** Creates a Python virtual environment and installs the required dependencies.
2. **Test:** Executes the unit tests using Python's `unittest` framework.
3. **Deploy:** Creates a deployment directory named `python-app-deploy` and copies the application files into it.
4. **Run Application:** Starts the Flask application in the background and checks whether the process is running.
5. **Test Application:** Executes the unit tests again to verify the application's behavior.

## Local Testing

Run the following commands from the `Exercise-09` directory.

### 1. Run Unit Tests

```cmd
python -m unittest -v test_app.py
```

The tests verify that the `/` endpoint returns HTTP status code `200` and the expected response message.

### 2. Start the Flask Application

```cmd
python app.py
```

The local application uses port `5002` to avoid conflicts with existing services.

### 3. Test the Application Endpoint

Open another CMD window and execute:

```cmd
curl.exe http://localhost:5002/
```

Expected response:

```text
Hello, Jenkins Multi-Stage Pipeline!
```

## Jenkins Configuration

Create a new Pipeline job in Jenkins and configure the following settings:

- **Definition:** Pipeline script from SCM
- **SCM:** Git
- **Repository URL:** Your DevOps-Lab GitHub repository URL
- **Branch Specifier:** `*/main`
- **Script Path:** `Exercises/Exercise-09/Jenkinsfile`

Save the configuration and trigger a build using **Build Now**.

Verify the console output and confirm that all five pipeline stages complete successfully.

## Expected Result

The pipeline should successfully install the required dependencies, execute the unit tests, prepare the deployment directory, start the Flask application, and execute the tests again.

A successful execution should show that all five stages have completed without errors.

## Screenshots

Store the actual screenshots in the `screenshots/` directory. Include evidence of:

- Application files and project structure
- Successful local unit tests
- Local application execution and endpoint testing
- Jenkinsfile creation
- Git commit and push
- Jenkins pipeline configuration
- Successful Jenkins pipeline execution

## Conclusion

This exercise demonstrates how Jenkins Declarative Pipelines can automate the build, testing, deployment preparation, and execution of a Flask application. It provides practical experience with continuous integration and basic continuous delivery workflows.
