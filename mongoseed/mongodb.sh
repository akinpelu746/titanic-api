#!/bin/bash
mongoimport -h mongodb -u $MONGODB_USERNAME  -p $MONGODB_PASSWORD   --authenticationDatabase admin  -c Passeneger -d $MONGODB_DB --fields=survived,passengerClass,name,sex,age,parentsOrChildrenAboard,siblingsOrSpousesAboard,fare --type csv --drop --file /mongoseed/titanic.csv



