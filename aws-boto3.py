import boto3

ec2 = boto3.resource('ec2')

# Step 1: Launch the EC2 instance
instance = ec2.create_instances(
    ImageId='ami-0c02fb55956c7d316',  # Amazon Linux 2 AMI (for us-east-1)
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',  # Free tier eligible
    KeyName='my-key-pair',    # Replace with your actual key pair name
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'MyTestInstance'}]
        }
    ]
)[0]

print(f"Launching instance with ID: {instance.id}")
instance.wait_until_running()
instance.reload()
print(f"Instance is now running at: {instance.public_dns_name}")

# Step 2: Wait before terminating
input("Press Enter to terminate the instance...")

# Step 3: Terminate the instance
instance.terminate()
instance.wait_until_terminated()
print("Instance terminated.")
