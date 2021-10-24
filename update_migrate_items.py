import logging
# from csv import DictReader
import boto3
from pprint import pprint
from scan_all import scan_items
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

allItems = scan_items()

# Comment out if you want to do local test with csv file.
# with open('./results.csv', 'r') as read_obj:
#     dict_reader = DictReader(read_obj)
#     allItems = list(dict_reader)

def update_allItems():
    items_holder =[]
    for item in allItems:
        # item['created'] = int(item['created']) # This is for value format between csv and DynamoDB requirement
        key = 'test'
        value = item.get(key)
        if key in item:
            if value != 1:
                item['test'] = 1
        else:
            item.update({'test': 1})
        items_holder.append(item)
    return items_holder

def migrate_items(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://dynamodb.ap-southeast-2.amazonaws.com")
    table = dynamodb.Table('stuff-new')
    allItems_new = update_allItems()
    try:
        with table.batch_writer() as batch:
            for item in allItems_new:
                batch.put_item(Item=item)
            return allItems
    except ClientError:
        logger.exception("Couldn't load data into table %s.", table.name)
        raise

if __name__ == '__main__':
    migrate_response = migrate_items()
    print("Migrate all items succeeded:")
    pprint(migrate_response, sort_dicts=False)