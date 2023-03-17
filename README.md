# Learn Apache Airflow 2023

Apache Airflow is an open-source workflow management platform for data engineering pipelines. It started at [Airbnb](https://www.airbnb.com/) in October 2014 as a solution to manage the company's increasingly complex workflows. Creating Airflow allowed Airbnb to programmatically author and schedule their workflows and monitor them via the built-in Airflow user interface. From the beginning, the project was made open source, becoming an [Apache Incubator](https://incubator.apache.org/) project in March 2016 and a top-level [Apache Software Foundation project](https://projects.apache.org/) in January 2019.

## Setup

The development setup of this repository comprises of multiple steps that need to be executed _IN ORDER_.

### Pre-Requisite

1. __Python Version:__ 3.9
2. __Shell:__ BASH (GitBASH in Windows)

### Environment Setup

This is the part where we set up the python development environment.

1. `python -m venv env` to create a new virtual environment.
2. `source env/bin/activate` to activate the virtual environment.
   1. `source env/Scripts/activate` in Windows.
3. `python -m pip install pip-tools` to install setup tools for the next step.
4. `pip-compile` to generate a platform-dependent list of dependencies.
5. `python -m pip install -r requirements.txt` to install all the required dependencies.
6. `sh install_airflow.sh` to install the pip-version of `airflow`
   1. Stricly speaking, this step is absolutely not necessary, but makes code completion in an IDE possible and does not hamper the actual airflow DAGs.

### Docker Setup

This is the part where we install and set up `docker` to run Airflow.

1. Install `docker` and `docker-compose` in your system with the instructions given [here](https://docs.docker.com/engine/install/). Alternately, you can also install the `Docker Desktop` if your system supports it.
   1. If you are running a Windows machine, you will need to [install `WSL/2`](https://learn.microsoft.com/en-us/windows/wsl/install) and select it as the backend when installing `docker`.
2. `mkdir dags plugins logs` to create the __mandatory__ directories if they were not already created.
3. `echo -e "AIRFLOW_UID=$(id -u)" > .env` to set the `User ID` in the `.env` file.
   1. Follow the instructions provided [here](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) to set up the container to run `docker`.
   2. Do __NOT__ change or redownload the `YML` file.
4. `docker-compose up airflow-init` to initialize the airflow database(s).
5. `docker-compose up -d` to run the airflow webserver and the miscellaneous services in `detached` mode.
   1. `docker-compose down` to stop the containers.
   2. `docker-compose down -v` to stop the containers and destroy all created volumes.
