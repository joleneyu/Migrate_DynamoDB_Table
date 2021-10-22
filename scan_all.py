from pprint import pprint
import boto3

def scan_items(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://dynamodb.ap-southeast-2.amazonaws.com")

    table = dynamodb.Table('stuff')
    response = table.scan()
    data = response['Items']

    if response.get('LastEvaluatedKey'):
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    else:
        return data


if __name__ == '__main__':
    allItems = scan_items()
    print(f"Scanning for all items:")
    pprint(allItems, sort_dicts=False)
