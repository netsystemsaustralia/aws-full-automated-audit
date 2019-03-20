import boto3
from botocore.exceptions import ClientError

def get_instances(region):
    client = boto3.client('ec2', region_name=region)
    try:
        result = client.describe_instances()
    except ClientError as e:
        print(e)
        return []
    else:
        if len(result["Reservations"]) > 0:
            instances = instances = [i for r in result["Reservations"] for i in r["Instances"]]
        else:
            instances = []
        return instances

""" def get_instances(region):
    ec2 = boto3.resource('ec2', region_name=region)
    try:
        result = ec2.get_instances()
    except ClientError as e:
        print(e)
        return []
    else:
        instances = [i for bucket in result.result.all():] """

def get_security_groups(region):
    client = boto3.client('ec2', region_name=region)
    try:
        result = client.describe_security_groups()
    except ClientError as e:
        print(e)
        return []
    else:
        security_groups = result["SecurityGroups"]
        return security_groups

def get_vpcs(region):
    client = boto3.client('ec2', region_name=region)
    try:
        result = client.describe_vpcs()
    except ClientError as e:
        print(e)
        return []
    else:
        vpcs = result["Vpcs"]
        return vpcs

def get_elastic_ip_addresses(region):
    client = boto3.client('ec2', region_name=region)
    try:
        result = client.describe_addresses()
    except ClientError as e:
        print(e)
        return []
    else:
        eips = result["Addresses"]
        return eips

# used when calling directly rather than as imported as a module
if __name__ == "__main__":
    #print(get_instances('ap-southeast-2'))
    #print(get_security_groups('ap-southeast-2'))
    #print(get_vpcs('ap-southeast-2'))
    print(get_elastic_ip_addresses('ap-southeast-2'))