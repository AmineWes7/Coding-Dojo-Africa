



function PizzaOven(crustType,sauceType,cheeses,toppings){
    var pizza ={};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;

}

var p = PizzaOven("deep dish","traditional","mozzarella",["pepperoni","sausage"]);
console.log(p)



function PizzaOven(crustType,sauceType,cheeses,toppings){
    var pizza1 ={};
    pizza1.crustType = crustType;
    pizza1.sauceType = sauceType;
    pizza1.cheeses = cheeses;
    pizza1.toppings = toppings;
    return pizza1;

}

var p2 = PizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
console.log(p2)

function PizzaOven(crustType,sauceType,cheeses,toppings){
    var pizza2 ={};
    pizza2.crustType = crustType;
    pizza2.sauceType = sauceType;
    pizza2.cheeses = cheeses;
    pizza2.toppings = toppings;
    return pizza2;

}

var pizza2 = PizzaOven("deep dish", "marinara", "mozzarella", "olives");
console.log(p2)