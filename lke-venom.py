#!/usr/bin/env python3

import json, requests, argparse, os, dotenv

# apiv4 token
dotenv.load_dotenv()
TOKEN = os.environ.get('token')

# other constants
REGIONS = {'mumbai':'ap-west',
           'toronto':'ca-central',
           'sydney':'ap-southeast',
           'dallas':'us-central',
           'fremont':'us-west',
           'atlanta':'us-southeast',
           'newark':'us-east',
           'london':'eu-west',
           'frankfurt':'eu-central',
           'tokyo':'ap-northeast',
           'singapore':'ap-south'}

TYPES = {'2GB':'g6-standard-1',
         '4GB':'g6-standard-2',
         '8GB':'g6-standard-4',
         '16GB':'g6-standard-6',
         '32GB':'g6-standard-8',
         '64GB':'g6-standard-16',
         '96GB':'g6-standard-20',
         '128GB':'g6-standard-24',
         '192GB':'g6-standard-32'}

class LKE_Custer(object):
    '''Create a LKE Cluster Object'''
    def __init__(self, name, region, size, count, version, tags):
        self.name = name 
        self.region = region
        self.size = size 
        self.count = int(count)
        self.version = version
        self.tags = tags

    def new_cluster(self):
        endpoint = "https://api.linode.com/v4/lke/clusters"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        cluster_info = {"label": self.name,
                "region": self.region,
                "k8s_version": self.version,
                "tags": [self.tags],
                "node_pools": [{"type": self.size, "count": self.count}]}
        #response = requests.post(endpoint, headers=headers, json=cluster_info).json()
        #print(json.dumps(response, indent=1)) # pretty json
        response = requests.post(endpoint, headers=headers, json=cluster_info)
        result = json.loads(response.text)
        status_code = response.status_code
        if status_code == 200:
            print('OK')
        else:
            error_message = result['errors'][0]['reason']
            error_field = result['errors'][0]['field']
            print(f'ERROR\n{error_message}: {error_field}')

def main():
    # get args
    parser = argparse.ArgumentParser()
    parser.add_argument('--name=', action ='store', dest='name')
    parser.add_argument('--region=', action='store', dest='region')
    parser.add_argument('--size=', action='store', dest='size')
    parser.add_argument('--count=', action='store', dest='count')
    parser.add_argument('--version=', action='store', dest='version')
    parser.add_argument('--tags=', action='store', dest='tags')
    args = parser.parse_args()

    # substite easier to remember regions and typs with acceptable values 
    if args.region in REGIONS:
        args.region = REGIONS[args.region]

    if args.size in TYPES:
        args.size = TYPES[args.size]
   
    # create lke cluster
    cluster = LKE_Custer(args.name, args.region, args.size, args.count, args.version, args.tags)
    cluster.new_cluster()

# main
if __name__ == '__main__':
    main()