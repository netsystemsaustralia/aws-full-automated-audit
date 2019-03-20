import json
import datetime
import ec2_class

# set global parameters
region = "ap-southeast-2"

# define helper functions
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

ec2_helper = ec2_class.Ec2Helper(region)
print("Getting EC2 Instances")
instances = ec2_helper.get_instances()
print(instances)
print(json.dumps(instances, default = myconverter))
