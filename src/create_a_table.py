from pprint import pprint
import boto3

def create_a_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

    table = dynamodb.create_table(
        TableName='stuff',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'created',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'created',
                'AttributeType': 'N'
            }
        ],
        BillingMode='PAY_PER_REQUEST',
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='stuff')
    assert table.table_status == 'ACTIVE'

    return table

if __name__ == '__main__':
    dummy_table = create_a_table()
    print("Table status:", dummy_table.table_status)