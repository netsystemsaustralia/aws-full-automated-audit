import boto3
from botocore.exceptions import ClientError

class ELBHelper:

    def __init__(self, region):
        self.region = region
        self.client = boto3.client('elbv2', region_name=region)

    def get_load_balancers(self):
        try:
            result = self.client.describe_load_balancers()
        except ClientError as e:
            print(e)
            return []
        else:
            elbs = result["LoadBalancers"]
            return elbs

# used when calling directly rather than as imported as a module
if __name__ == "__main__":
    h = ELBHelper("ap-southeast-2")
    print("Getting ELBs")
    print(h.get_load_balancers())