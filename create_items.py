from pprint import pprint
import boto3
import uuid
import random

# dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2', endpoint_url="http://localhost:8000")
# table = dynamodb.Table('stuff')

# for x in range(10):
#     id = uuid.uuid4()
#     timestamp = random.randrange(1571626141, 1634792207)
#     print("Adding items:", id)
#     table.put_item(
#         Item={
#             'id': id,
#             'created': timestamp
#         }
#     )

def put_item(id, created, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://dynamodb.ap-southeast-2.amazonaws.com")

    table = dynamodb.Table('stuff')
    response = table.put_item(
       Item={
            'id': id,
            'created': created,
        }
    )
    return response

# id = str(uuid.uuid4())
# timestamp = random.randrange(1571626141, 1634792207)

if __name__ == '__main__':
    for x in range(20):
        id = str(uuid.uuid4())
        timestamp = random.randrange(1571626141, 1634792207)
        body = put_item(id, timestamp)
        print("Put item succeeded:")
        pprint(body, sort_dicts=False)
