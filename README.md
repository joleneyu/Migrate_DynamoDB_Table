# Migrate_DynamoDB_Table

This is the sample code I wrote for updating a DymanoDB table. You can either update all items in place with ```update_items_in_place.py```, or migrate all items to a new table with an updated attribute and its new value with ```update_migrate_items```.

As migrate option can leverage batch to write items, it is around 20 times quicker than updating items one by one. Highly recommend it if you need to update a large amount of data. On top of that, leveraging the spot instance or Lambda functions should improve write performance. I will update a spot instance with the required configuration after.
