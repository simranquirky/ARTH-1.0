
// ################# This is a Mapper and Reducer program to calculate total number of different genders in a state and then store their count to collection "map_reduce22" #####

var mapfun22 = function() { 
emit(this.location.state , this.gender); 
};


var reducerfun22 = function(state ,gender){ 
var result = {male : 0 , female : 0}; 
for (var idx =0 ; idx < gender.length ; ++idx){ 
if(gender[idx] == "male")  result.male++; 
else  result.female++ ; 
} 
return result; 
};

> db.contacts.mapReduce( 
mapfun22, 
reducerfun22, 
{out : "map_reduce22"} 
)
