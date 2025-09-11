# DEMC-FastAPI-Kubernetes
This is the repo for our Data Engineering Master Class - FastAPI &amp; Kubernetes

# Environments
- Virtual Machine (bevorzugt)
- Local Setup


## Following software tools are necessary (for VM):
- Remote Desktop (for Windows User)
- Windows App (for Mac users)
- Github Account

## Following software tools are necessary (for local setup):
- Python 3.10
- VSCode
- VScode Plugins: Python Debugger & Python language support
- Git 
- Github Account
- Zscaler Zugriffspaket (ZScaler-MHP-CS-Demo-90d) beantragen 
- azure-cli: https://learn.microsoft.com/de-de/cli/azure/install-azure-cli?view=azure-cli-latest
- helm: https://helm.sh/docs/helm/helm_install/
- docker/podman: https://podman.io/ (Für Docker Desktop Nutzung ist ein MHP Docker Enterprise Account notwendig!)
- kubectl: https://kubernetes.io/docs/tasks/tools/
- Bruno (https://www.usebruno.com/) oder Postman


# FastAPI Setup

We use a very standard python setup, combining venv and pip. 

Python Version: 3.10

⚠️ **MHP VPN Connection Required for Service Operation** ⚠️

⚠️ Prerequisite: Python 3.10 and pip are already installed on your local machine.⚠️ 



## Following steps are necessary:
1. Initialize venv with
```sh
python3 -m venv venv  
```  
When it's not working directly, maybe you have to install the following package before: 
```sh
sudo apt install python3.10-venv 
```  

2. Actrivate the virtual python environment source venv/bin/activate: 
```sh
source venv/bin/activate  
```  

3. Install all relevant python packages from requirements.txt file: 
```sh
pip install -r requirements.txt (pip install)
```

4. Verify successful installation of dependencies by checking installed lib packages in venv folder

5. Start FastAPI App/Service by starting the uvicorn server
```sh
uvicorn app.main:app --reload
```  



## Further (optional) VSCode Plugins

- ....
- ....



# Kubernetes Setup
....






