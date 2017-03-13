curl -v -k -X POST -H "Content-Type: application/json" -H "Cache-Control: no-cache"  -d '{
"update_id":10000,
"message":{
"date":1441645532,
"chat":{
   "type": "test",
   "last_name":"Test Lastname",
   "id":1111111,
   "first_name":"Test",
   "username":"Test"
},
"message_id":1365,
"from":{
   "last_name":"Test Lastname",
   "id":1111111,
   "first_name":"Test",
   "username":"Test"
},
"text":"/start"
}
}' $1
