
// #### This is Mapper and Reducer program to calculate average of male and female average age and store results to a collection ##########

var mapfun = function() {
emit(this.gender , this.dob.age);
};

var reducefun = function(gneder , age) {
return Array.avg(age);
};

db.contacts.mapReduce(
mapfun,
reducefun,
{out : "map_reduce11"}
)
