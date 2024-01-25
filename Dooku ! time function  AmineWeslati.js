/*For example, when calling the function like this: greet("Anakin") 
it would log to the console, Good day, Anakin!

Level 2: Further customize your function by including the time of day in your greeting. 
Hint: can functions only take one parameter?

Level 3: You and Count Dooku are enemies. Further customize your code to say, 
"I'm coming for you, Dooku!" if your function is called with "Count Dooku"*/
function greetPerson(Amine){console.log(`Goodday `+"Amine")}//lvl1
greetPerson("Amine")
function getCurrentTime() {//lvl 2
    var now = new Date();
    var hours = now.getHours();     
    var minutes = now.getMinutes();
    minutes=(minutes < 10)? '0' + minutes : minutes;
    return hours +`H `+minutes +`Min`;
  }console.log(getCurrentTime());
  function CountDooku(Duku){
    console.log(`I'm coming for you, Dooku!`)}//lvl1
CountDooku("I'm coming for you, Dooku!")
/*var now = new Date();
var hours = now.getHours();   ==========>>> i found this code form W3schools
var minutes = now.getMinutes();*/
  