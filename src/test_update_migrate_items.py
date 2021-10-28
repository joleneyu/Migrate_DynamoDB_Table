import boto3
import unittest
from moto import mock_dynamodb2
from pprint import pprint
from botocore.exceptions import ClientError

@mock_dynamodb2
class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2')
        from create_a_table import create_a_table
        self.table = create_a_table(self.dynamodb)
        pass

    def tearDown(self):
        self.table.delete()
        self.dynamodb=None
        pass

    def test_table_exists(self):
        pprint(self.table)
        self.assertIn('stuff', self.table.name)
        pass

    def test_create_itmes(self):
        from create_items import put_item
        result = put_item("2f7460bb-5e96-4fab-b382-60dbdb9496ee", 1621098536, self.dynamodb)
        self.assertEqual(200, result['ResponseMetadata']['HTTPStatusCode'])
        pass

    def test_scan_table(self):
        from create_items import put_item
        put_item("2f7460bb-5e96-4fab-b382-60dbdb9496ee", 1621098536, self.dynamodb)
        put_item("2f7460bb-5e96-4fab-b382-80dbdb9496ee", 1621098535, self.dynamodb)
        from scan_all import scan_items
        results = scan_items(self.dynamodb)
        # pprint(results)
        self.assertEqual(2, sum(1 for _ in results))
        self.assertEqual('2f7460bb-5e96-4fab-b382-60dbdb9496ee', results[0]['id'])
        self.assertEqual(1621098535, results[1]['created'])
        pass
    


if __name__ == '__main__':
    unittest.main()



# def test_migrate_items():
#     "Test the migrate_items with a valid input data"