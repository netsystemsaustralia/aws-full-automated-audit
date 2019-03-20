import boto3
from botocore.exceptions import ClientError

def get_load_balancers(region):
    client = boto3.client('elbv2', region_name=region)
    try:
        result = client.describe_load_balancers()
    except ClientError as e:
        print(e)
        return []
    else:
        elbs = result["LoadBalancers"]
        return elbs

# used when calling directly rather than as imported as a module
if __name__ == "__main__":
    print(get_load_balancers('ap-southeast-2'))