\# Exercise 08: Jenkins Job Configuration and Build



\## Objective



Create a GitHub repository containing a shell script, configure a Jenkins Freestyle job to retrieve the script from GitHub, and execute it as a Jenkins build.



\## Tools Used



\- Git and GitHub

\- Jenkins

\- Docker Desktop

\- Bash shell



\## Procedure



\### Step 1: Verify Jenkins



Check that the Jenkins Docker container is running.



Jenkins URL: http://localhost:8080



\### Step 2: Create the GitHub Repository



Create a repository named `devops-sample-code` and use its HTTPS URL to connect the local Git repository.



\### Step 3: Create the Shell Script



Create `hello-world.sh` with the following content:



```bash

\#!/bin/bash

echo "Hello, Jenkins!"

```



\### Step 4: Initialize Git and Push the Script



Initialize a Git repository, stage and commit the script, configure the GitHub remote, and push the commit to the `main` branch.



\### Step 5: Create a Jenkins Freestyle Job



Create a Jenkins job named `HelloWorld` and select \*\*Freestyle project\*\*.



\### Step 6: Configure Source Code Management



Configure the job to retrieve the source code from the `devops-sample-code` GitHub repository.



\- \*\*Repository URL:\*\* The HTTPS URL of the repository

\- \*\*Branch Specifier:\*\* `\*/main`

\- \*\*Credentials:\*\* None for a public repository



\### Step 7: Configure the Build Step



Add an \*\*Execute shell\*\* build step with these commands:



```bash

chmod +x hello-world.sh

./hello-world.sh

```



Save the job configuration.



\### Step 8: Execute and Verify the Build



Select \*\*Build Now\*\*, open the build number, and inspect \*\*Console Output\*\*.



The successful build prints:



```text

Hello, Jenkins!

Finished: SUCCESS

```



\## Result



The shell script was pushed to GitHub, retrieved by Jenkins through Source Code Management, and executed successfully as a Jenkins build.



\## Screenshots



The `screenshots/` directory contains the available evidence of the exercise, including Jenkins container verification, repository creation, script creation, Git operations, Jenkins job configuration, and the successful build.



