//Code Snippet 1
function hello() {
    console.log('hello');
}
hello();
console.log('Dojo'); /*fun=hello console.log:hello 
 run code = hello Dojo */ 

//Code Snippet 2
function hello() {
    console.log('hello');
    return 15; /*fun=hello console.log:hello ruturn 15 
    hello   result is 15*/
}
var result = hello();
console.log('result is', result);
/*result=hello result is = result   hello result is 15*/
//Code Snippet 3
function hello() {
    console.log('hello');
    return 15;
}
var result = hello();
console.log('result is', result);
//result=hello result is 15
//Code Snippet 4
var num = 15;
console.log(num);
function logAndReturn(num){
   console.log(num);   //num------15
   return num; //console.log-----num
                //function logAndReturn_____________num
}              //15
var result = logAndReturn(10);
console.log(result);
console.log(num); //console.log---------result console.log---------num //10


//Code Snippet 5
var num = 15;
console.log(num);             //num = 15
function timesTwo(num){       //return num*2
   console.log(num);   //15,15
   return num*2;
}
var result = timesTwo(10);
console.log(result);    //timesTwo-------10 / console.log------result / console.log------num
console.log(num);   //10

//Code Snippet 6
function timesTwoAgain(num) {
    console.log('num is', num);
    var y = num*2;   //20     /var y = num*2    /return y //15
    return y;
}
var result = timesTwoAgain(3) + timesTwoAgain(5);
console.log('result is', result);

//Code Snippet 7
function timesTwoAgain(num) {
    console.log('num is', num);
    var y = num*2;
    return y;
}
var result = timesTwoAgain(3) + timesTwoAgain(5);
console.log('result is', result);

//Code Snippet 8
function printSumNums(num1, num2) {
    console.log(num1);   
    return num1+num2;
 }
 console.log(printSumNums(2,3))
 console.log(printSumNums(3,5))
 
//Code Snippet 9
function sumNums(num1, num2) {
    var sum = num1 + num2;
    console.log('sum is', sum);
    return sum;
}
var result = sumNums(2,3) + sumNums(3,5);
console.log('result is', result);

//Code Snippet 10
