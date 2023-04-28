python
import boto3
import json

# set up a connection to the Kinesis stream
kinesis = boto3.client('kinesis')

def put_record(data):
    """
    Put a record into the Kinesis stream
    """
    # convert data to JSON string
    data_str = json.dumps(data)

    # put the record into the Kinesis stream
    kinesis.put_record(
        StreamName='my-kinesis-stream',
        Data=data_str,
        PartitionKey='partition-key'
    )

# example usage
data = {'some_key': 'some_value'}
put_record(data)
