# Migrate_DynamoDB_Table

This is the sample code I wrote for updating a DymanoDB table. 
You can either update all items in place with ```update_items_in_place.py```,
or migrate all itmes to a new table with updated attribute and its new value
with ```update_migrate_items```.

As migrate option can leverage batch to write items, it is around 20 times quicker than
update items one by one. Highly recommend if you need to update a large amount of data.
On top of that, leverage the spot instance or Lambda functions should improve write perfomance. I will update a spot instance with required configuraition after.