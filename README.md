# Azure Python

Public cloud computing on Microsoft Azure with Python

# Objective

Minimize cost by using [always free services](https://azure.microsoft.com/en-us/free).

# Requirements

This code calls the Azure API and to run it successfully you need the following Azure resources.

1) Microsoft Azure account to authenticate yourself
2) Subscription to associate your resources
3) App registration to assign permissions
4) Custom role with permission `Microsoft.Resources/subscriptions/locations/read` to read locations
5) Role assignment of the custom role to the app registration

# Develop

1) Clone with `git clone https://github.com/gerald-scharitzer/azure-python.git`
2) Install `pip` with `python -m ensurepip --upgrade`
3) Install packages with `python -m pip install -r requirements.txt`
4) Run with `python azure_python.py <stdin.yaml`
