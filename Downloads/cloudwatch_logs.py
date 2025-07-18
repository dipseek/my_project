import boto3

# Replace with your region
region = 'us-east-1'  # e.g., Mumbai

# Replace with your log group name (as seen in CloudWatch)
log_group = '/ec2/cloud-init-log'  

# Initialize client
client = boto3.client('logs', region_name=region)

# Get list of streams in the log group
streams = client.describe_log_streams(
    logGroupName=log_group,
    orderBy='LastEventTime',
    descending=True,
    limit=1
)

# Get latest stream name
log_stream_name = streams['logStreams'][0]['logStreamName']

# Fetch log events from the latest stream
events = client.get_log_events(
    logGroupName=log_group,
    logStreamName=log_stream_name,
    startFromHead=True  # Change to False to get latest logs first
)

# Print log events
for event in events['events']:
    print(event['timestamp'], event['message'])
