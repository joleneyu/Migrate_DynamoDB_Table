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
        value = item.get(key)
        if key in item:
            if value != 1:
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
                print(response)
                updateItems.append(response)
            else:
                print("test value exist")
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
            print(response)
            updateItems.append(response)
            print(updateItems)
    return updateItems

if __name__ == '__main__':
    update_response = update_items('test')
    print("Update all items succeeded:")
    pprint(update_response, sort_dicts=False)
