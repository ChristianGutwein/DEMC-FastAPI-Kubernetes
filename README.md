# DEMC-FastAPI-Kubernetes
This is the repo for our Data Engineering Master Class - FastAPI &amp; Kubernetes


# FastAPI Setup

We use a very standard python setup, combining venv and pip. 

Python Version: >3.9 & <3.13

⚠️ **MHP VPN Connection Required for Service Operation** ⚠️

⚠️ Prerequisite: Python and pip are already installed on your local machine.⚠️ 


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






