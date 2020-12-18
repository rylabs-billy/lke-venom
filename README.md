# LKE Venom

Deploy a Kubernetes cluster with the Linode Kubernetes Engine and API.

Put your Linode APIv4 [access token](https://www.linode.com/docs/guides/getting-started-with-the-linode-api/#get-an-access-token) into a `.env` file:
```
echo 'token="<YOUR_API_TOKEN"' > .env
```
Create virtual environment:
```
python3 -m venv env
source env/bin/activate
```
Install requirements:
```
pip install -r requirments.txt
```
Deploy a LKE cluster:
```
lke-venom.py --name=example-cluster --region=toronto --size=2GB --count=3 --version=1.17 --tags=poc
```
Regions:
- mumbai
- toronto
- sydney
- dallas
- fremont
- atlanta
- newark
- london
- frankfurt
- tokyo
- singapore

Sizes (plan type of linodes/worker nodes):
- 2GB
- 4GB
- 8GB
- 16GB
- 32GB
- 64GB
- 96GB
- 128GB
- 192GB

Count (how many worker nodes): 1 - 100 

Versions:
- 1.16
- 1.17
- 1.18

Tags: Anything your heart desires.


