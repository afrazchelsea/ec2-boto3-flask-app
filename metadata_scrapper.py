import boto3
from config import ACCESS_KEY, SECRET_ACCESS_KEY

ec2_client = boto3.client(
    'ec2',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_ACCESS_KEY
    )

def get_metadata(ins_id):
    data_list = []
    instances = ec2_client.describe_instances()
    for instance in instances['Reservations']:
        if ins_id == instance['Instances'][0]['InstanceId']:
            ami_id = instance['Instances'][0]['ImageId']
            subnet = instance['Instances'][0]['SubnetId']
            ip_addr = instance['Instances'][0]['PrivateIpAddress']
            hostname = instance['Instances'][0]['PrivateDnsName']
            data_list.append(ins_id)
            data_list.append(hostname)
            data_list.append(subnet)
            data_list.append(ip_addr)
            data_list.append(ami_id)
            return data_list
        else:
            return "Please cross-check Instance ID. Instance could be terminated or not exist at all."

    