// example-1
// ######### MongoDB Aggregation examples to calculate number  of males in all the states and keep their count. ##############

db.contacts.aggregate([
{$match : {gender : "male"}},
{$group : {_id: {state : "$location.state"} , total_males : {$sum : 1} }} ])

// example -2
// ########### MongoDB Aggragation example to find the average of ages of males and females seperatly and storing them in a collection ###########

db.contacts.aggregate([
{$group : {_id : "$gender" , value: {$avg : "$dob.age"} }},
{$out : "aggregation11"}
])
