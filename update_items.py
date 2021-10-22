from pprint import pprint
import boto3
from scan_all import scan_items

def update_items(test, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://dynamodb.ap-southeast-2.amazonaws.com")
    table = dynamodb.Table('stuff')
    allItems = scan_items()
    updateItems = []
    for item in allItems:
        id = item['id']
        created = item['created']
        # print(id, created)
        key = test
        if key in item:
            print("test attribute exists")
        else:
            response = table.update_item(
                Key={
                    'id': id,
                    'created': created
                },
                UpdateExpression="set test=:t",
                ExpressionAttributeValues={
                    ':t': 1,
                },
                ReturnValues="ALL_NEW"
            )
            updateItems.append(response)

if __name__ == '__main__':
    update_items('test')
    print("Update all items succeeded:")
    # pprint(update_response, sort_dicts=False)
