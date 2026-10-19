\# Exercise 07: Introduction to CI and Jenkins Installation



\## Objective



Understand the purpose of Continuous Integration (CI), learn the basic concepts of Jenkins, and run Jenkins in a Docker container.



\## Introduction to Continuous Integration (CI)



Continuous Integration is a software development practice in which developers frequently integrate code changes into a shared repository. Automated builds and tests help identify integration issues early and provide fast feedback.



\### Key Features and Benefits



\- \*\*Frequent Integration:\*\* Developers regularly commit and push changes to a shared repository.

\- \*\*Automated Builds and Tests:\*\* Automated checks validate application changes.

\- \*\*Fast Feedback:\*\* Build and test results help developers identify problems early.

\- \*\*Improved Collaboration and Code Quality:\*\* Integration issues and regressions can be detected sooner.



\### Typical CI Workflow



1\. A developer commits and pushes a code change.

2\. The CI server detects the change or receives a configured trigger.

3\. The server builds the application and resolves dependencies.

4\. Automated tests are executed.

5\. Results are reported so developers can address failures.



Examples of CI/CD tools include Jenkins, GitHub Actions, GitLab CI/CD, CircleCI, and Azure Pipelines.



\## Introduction to Jenkins



Jenkins is an open-source automation server used to automate software build, test, and delivery tasks. It supports CI/CD workflows and can be extended through plugins.



\### Key Jenkins Concepts



\- \*\*Job:\*\* A configured task that Jenkins executes.

\- \*\*Build:\*\* An execution of a job or pipeline.

\- \*\*Pipeline:\*\* A sequence of automated steps used to build, test, and deliver software.

\- \*\*Plugins:\*\* Extensions that add integrations and capabilities.

\- \*\*Nodes and Agents:\*\* Machines or environments that execute build tasks.



\## Jenkins Installation Using Docker



\### 1. Start the Jenkins Container



Run the following command:



```cmd

docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts

```



The `-d` option runs the container in the background. Port `8080` exposes the Jenkins web interface, while port `50000` is used for inbound agent connections.



Verify that the container is running:



```cmd

docker ps

```



\### 2. Retrieve the Initial Administrator Password



Run the following command in Windows CMD:



```cmd

docker exec jenkins cat /var/jenkins\_home/secrets/initialAdminPassword

```



Copy the displayed password for the Jenkins setup wizard.



\### 3. Unlock Jenkins



Open the following URL in a browser:



http://localhost:8080



Enter the initial administrator password in the \*\*Administrator password\*\* field and select \*\*Continue\*\*.



\### 4. Install Suggested Plugins



Select \*\*Install suggested plugins\*\* and wait for the installation to complete.



\### 5. Create the Administrator User



Complete the \*\*Create First Admin User\*\* form with the required account details and continue.



\### 6. Configure the Jenkins Instance



Complete the instance configuration page when prompted and finish the initial setup.



\### 7. Verify the Jenkins Dashboard



After completing the setup, confirm that the Jenkins dashboard loads successfully.



Jenkins URL:



http://localhost:8080



\## Results



\- Jenkins was started in a Docker container.

\- The initial administrator password was retrieved from the container.

\- Jenkins was unlocked through the browser.

\- The initial setup and plugin installation were completed.

\- The administrator login was completed.

\- The Jenkins dashboard was opened successfully.



\## Screenshots



The `screenshots/` directory contains screenshots documenting the Jenkins container, password retrieval, unlock page, plugin installation, administrator setup, instance configuration, readiness confirmation, dashboard, and version information, where captured.



\## Conclusion



This exercise introduced Continuous Integration and the basic concepts of Jenkins. Jenkins was installed using Docker, configured through the browser, and accessed through its dashboard.



