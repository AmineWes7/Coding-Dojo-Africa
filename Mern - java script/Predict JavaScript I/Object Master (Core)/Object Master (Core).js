const pokemon = Object.freeze([
    { "id": 1,   "name": "Bulbasaur",  "types": ["poison", "grass"] },
    { "id": 5,   "name": "Charmeleon", "types": ["fire"] },
    { "id": 9,   "name": "Blastoise",  "types": ["water"] },
    { "id": 12,  "name": "Butterfree", "types": ["bug", "flying"] },
    { "id": 16,  "name": "Pidgey",     "types": ["normal", "flying"] },
    { "id": 23,  "name": "Ekans",      "types": ["poison"] },
    { "id": 24,  "name": "Arbok",      "types": ["poison"] },
    { "id": 25,  "name": "Pikachu",    "types": ["electric"] },
    { "id": 35,  "name": "Clefairy",   "types": ["normal"] },
    { "id": 37,  "name": "Vulpix",     "types": ["fire"] },
    { "id": 52,  "name": "Meowth",     "types": ["normal"] },
    { "id": 63,  "name": "Abra",       "types": ["psychic"] },
    { "id": 67,  "name": "Machamp",    "types": ["fighting"] },
    { "id": 72,  "name": "Tentacool",  "types": ["water", "poison"] },
    { "id": 74,  "name": "Geodude",    "types": ["rock", "ground"] },
    { "id": 87,  "name": "Dewgong",    "types": ["water", "ice"] },
    { "id": 98,  "name": "Krabby",     "types": ["water"] },
    { "id": 115, "name": "Kangaskhan", "types": ["normal"] },
    { "id": 122, "name": "Mr. Mime",   "types": ["psychic"] },
    { "id": 133, "name": "Eevee",      "types": ["normal"] },
    { "id": 144, "name": "Articuno",   "types": ["ice", "flying"] },
    { "id": 145, "name": "Zapdos",     "types": ["electric", "flying"] },
    { "id": 146, "name": "Moltres",    "types": ["fire", "flying"] },
    { "id": 148, "name": "Dragonair",  "types": ["dragon"] }
]);

// 1. An array of Pokémon objects where the id is evenly divisible by 3
const divisibleBy3 = pokemon.filter(p => p.id % 3 === 0);

// 2. An array of Pokémon objects that are "fire" type
const fireTypePokemons = pokemon.filter(p => p.types.includes("fire"));

// 3. An array of Pokémon objects that have more than one type
const multiTypePokemons = pokemon.filter(p => p.types.length > 1);

// 4. An array with just the names of the Pokémon
const pokemonNames = pokemon.map(p => p.name);

// 5. An array with just the names of Pokémon with an id greater than 99
const namesWithIdGreaterThan99 = pokemon.filter(p => p.id > 99).map(p => p.name);

// 6. An array with just the names of the Pokémon whose only type is poison
const poisonOnlyNames = pokemon.filter(p => p.types.length === 1 && p.types[0] === "poison").map(p => p.name);

// 7. An array containing just the first type of all the Pokémon whose second type is "flying"
const firstTypeOfFlying = pokemon.filter(p => p.types[1] === "flying").map(p => p.types[0]);

// 8. A count of the number of Pokémon that are "normal" type
const normalTypeCount = pokemon.filter(p => p.types.includes("normal")).length;

// 9. An array with all Pokémon except the Pokémon with the id of 148
const withoutDragonair = pokemon.filter(p => p.id !== 148);

// 10. An array with all Pokémon and for Pokémon id: 35 replacing "normal" with "fairy"
const pokemonWithFairyType = pokemon.map(p => {
    if (p.id === 35) {
        p.types[0] = "fairy";
    }
    return p;
});