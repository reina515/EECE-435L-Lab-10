"""Simple local deployment script for the Jenkins pipeline."""
import os
import runpy
import shutil
from datetime import datetime

DEPLOY_DIR = os.environ.get("DEPLOY_DIR", os.path.join(os.getcwd(), "deploy"))
FILES = ["app.py", "requirements.txt"]


def deploy():
    os.makedirs(DEPLOY_DIR, exist_ok=True)
    for name in FILES:
        shutil.copy(name, DEPLOY_DIR)
        print(f"Copied {name} -> {DEPLOY_DIR}")
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(os.path.join(DEPLOY_DIR, "deploy_log.txt"), "a") as log:
        log.write(f"Deployed at {stamp}\n")
    print("Running deployed app:")
    runpy.run_path(os.path.join(DEPLOY_DIR, "app.py"), run_name="__main__")
    print(f"Deployment successful at {stamp}")


if __name__ == "__main__":
    deploy()
