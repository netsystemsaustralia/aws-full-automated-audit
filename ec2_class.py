import boto3
from botocore.exceptions import ClientError

class Ec2Helper:

    def __init__(self, region):
        self.region = region
        self.client = boto3.client('ec2', region_name=region)

    def get_instances(self):
        try:
            result = self.client.describe_instances()
        except ClientError as e:
            print(e)
            return []
        else:
            if len(result["Reservations"]) > 0:
                instances = instances = [i for r in result["Reservations"] for i in r["Instances"]]
            else:
                instances = []
            return instances
    
    def get_security_groups(self):
        try:
            result = self.client.describe_security_groups()
        except ClientError as e:
            print(e)
            return []
        else:
            security_groups = result["SecurityGroups"]
            return security_groups

    def get_vpcs(self):
        try:
            result = self.client.describe_vpcs()
        except ClientError as e:
            print(e)
            return []
        else:
            vpcs = result["Vpcs"]
            return vpcs

    def get_elastic_ip_addresses(self):
        try:
            result = self.client.describe_addresses()
        except ClientError as e:
            print(e)
            return []
        else:
            eips = result["Addresses"]
            return eips

# used when calling directly rather than as imported as a module
if __name__ == "__main__":
    h = Ec2Helper("ap-southeast-2")
    print("Getting EC2 Instances")
    print(h.get_instances())
    print("Getting Security Groups")
    print(h.get_security_groups())
    print("Getting EIPs")
    print(h.get_elastic_ip_addresses())
    print("Getting VPCs")
    print(h.get_vpcs())