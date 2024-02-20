// Define a function to create a pizza object
function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {
      crustType: crustType,
      sauceType: sauceType,
      cheeses: cheeses,
      toppings: toppings
    };
    return pizza;
  }
  
  // Create a pizza with: "deep dish", "traditional", ["mozzarella"], and ["pepperoni", "sausage"]
  var pizza1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
  console.log(pizza1);
  
  // Create a pizza with: "hand tossed", "marinara", ["mozzarella", "feta"], and ["mushrooms", "olives", "onions"]
  var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
  console.log(pizza2);
  
  // Create 2 more pizzas with any toppings we like!
  var pizza3 = pizzaOven("thin crust", "alfredo sauce", ["cheddar"], ["ham", "bacon", "pineapple"]);
  console.log(pizza3);
  
  var pizza4 = pizzaOven("gluten free crust", "tomato sauce", ["cheddar", "swiss"], ["peppers", "bell peppers", "jalapenos"]);
  console.log(pizza4);
  
  // Bonus Challenge: Create a function called randomPizza that uses Math.random() to create a random pizza!
  function randomPizza() {
    var crustTypes = ["deep dish", "hand tossed", "thin crust", "gluten free crust"];
    var sauceTypes = ["traditional", "marinara", "alfredo sauce", "tomato sauce"];
    var cheeses = ["mozzarella", "feta", "cheddar", "swiss", "provolone"];
    var toppings = ["pepperoni", "sausage", "ham", "bacon", "pineapple", "mushrooms", "olives", "onions", "peppers", "bell peppers", "jalapenos"];
  
    var randomCrustType = crustTypes[Math.floor(Math.random() * crustTypes.length)];
    var randomSauceType = sauceTypes[Math.floor(Math.random() * sauceTypes.length)];
    var randomCheeses = [];
    var randomToppings = [];
  
    var randomCheeseCount = Math.floor(Math.random() * 3) + 1;
    for (var i = 0; i < randomCheeseCount; i++) {
      randomCheeses.push(cheeses[Math.floor(Math.random() * cheeses.length)]);
    }
  
    var randomToppingCount = Math.floor(Math.random() * 5) + 1;
    for (var i = 0; i < randomToppingCount; i++) {
      randomToppings.push(toppings[Math.floor(Math.random() * toppings.length)]);
    }
  
    var randomPizza = pizzaOven(randomCrustType, randomSauceType, randomCheeses, randomToppings);
    return randomPizza;
  }
  
  var randomPizza1 = randomPizza();
  console.log(randomPizza1);
  
  var randomPizza2 = randomPizza();
  console.log(randomPizza2);