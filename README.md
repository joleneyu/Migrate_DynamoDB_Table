# Migrate_DynamoDB_Table

This is the sample code I wrote for updating a DymanoDB table. You can either update all items in place with ```update_items_in_place.py```, or migrate all items to a new table with an updated attribute and its new value with ```update_migrate_items```.

As migrate option can leverage batch to write items, it is around 20 times quicker than updating items one by one. Highly recommend it if you need to update a large amount of data. On top of that, leveraging the spot instance or Lambda functions should improve write performance. I will update a spot instance with the required configuration after.

## Usage

1. Use ```dynamodb.yaml``` to create dummy tables to test against. 
2. Use ```create_items.py``` to create a bunch of items to mock real table items. You could change the number of items will be created with setting up ```range```
3. ```scan_all.py``` is using for scan all the items in the table.
4. Use ```update_items_in_place.py``` to update items one by one in the original table.
5. ```update_migrate_items``` is for batch migrating items to a new table with new attributes.
