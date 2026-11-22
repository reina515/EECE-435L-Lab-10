# EECE 435L – Lab 10: Jenkins CI/CD Pipeline for Python

**Author:** Reina Hani

A simple Python project with a Jenkins pipeline that automatically sets up the environment, lints, tests, measures code coverage, runs a security scan, and deploys the application.

## Project Structure

```
EECE-435L-Lab-10/
├── app.py                   # Application: greet() function
├── deploy.py                # Local deployment script
├── tests/
│   └── test_app.py          # Unit test for greet()
├── requirements.txt         # flake8, pytest, coverage, bandit
├── Jenkinsfile_Reina_Hani   # Jenkins pipeline definition
└── .gitignore
```

## Pipeline Stages

| Stage | Tool | What it does |
|---|---|---|
| Setup | venv, pip | Creates a virtual environment and installs `requirements.txt` |
| Lint | flake8 | Checks `app.py` and `deploy.py` for PEP 8 style issues |
| Test | pytest | Runs the unit tests in `tests/` |
| Coverage | coverage.py | Measures test coverage of `app.py`, prints a report, and generates an HTML report (`htmlcov/`) |
| Security Scan | bandit | Scans `app.py` and `deploy.py` for security vulnerabilities and saves `bandit_report.txt` |
| Deploy | deploy.py | Copies the app to `C:\jenkins_deploy`, logs a timestamp in `deploy_log.txt`, and runs the deployed app |

After every build, the coverage HTML report and `bandit_report.txt` are archived as **build artifacts**, then the workspace is cleaned.

> **Note:** The pipeline is written for a **Windows** Jenkins agent, so it uses `bat` and `venv\Scripts\activate.bat` instead of the Linux `sh` / `source venv/bin/activate` commands from the lab handout.

## Running Locally

```bash
pip install -r requirements.txt
python app.py                         # Hello, World from Reina Hani!
flake8 app.py deploy.py               # lint
python -m pytest                      # tests
coverage run --source=app -m pytest   # coverage
coverage report -m
bandit app.py deploy.py               # security scan
python deploy.py                      # local deployment
```

## Jenkins Setup

1. Install the **Git**, **Pipeline**, and **SSH Agent** plugins.
2. Create a **Pipeline** job named `Python-CI-CD`.
3. Under **Pipeline**, choose **Pipeline script from SCM**:
   - SCM: **Git**
   - Repository URL: `https://github.com/reina515/EECE-435L-Lab-10.git`
   - Branch: `*/main`
   - Script Path: `Jenkinsfile_Reina_Hani`
4. Click **Build Now** (or enable **Poll SCM** with `H/2 * * * *` to build automatically on push).

## Requirements

- Jenkins 2.580+ with Java 21
- Python 3.10+
- Git
