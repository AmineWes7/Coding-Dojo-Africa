
  /*  const counterButton = document.querySelector('#counterButton');
    const counterText = document.querySelector('#counterText');
    let count = 314;

    counterButton.addEventListener('click', () => {
    count++;
    counterText.textContent = count;
});*/
//==============================Alert========================================
/*const buttonContainer = document.querySelector('#buttonContainer');
const newButton = document.createElement('button');
newButton.textContent = 'Click me!';
newButton.id = 'newButton';
buttonContainer.appendChild(newButton);

newButton.addEventListener('click', () => {
    alert('Button clicked!');
});*/
//=================================change buttom======================================
/*const myButton = document.querySelector('#myButton');

myButton.addEventListener('click', () => {
    if (myButton.textContent === 'like 1') {
        myButton.textContent = 'like 2';
    }});*/
//==================================change and change==================================================
/*const myButton = document.querySelector('#myButton');

myButton.addEventListener('click', () => {
    if (myButton.textContent === 'Example 1') {
        myButton.textContent = 'Example 2';
    } else {
        myButton.textContent = 'Example 1';
    }
});*/
//----------------------------------------------------button change text--------------------------------------------------------
const myButton = document.querySelector('#myButton');
const myText = document.querySelector('#myText');

myButton.addEventListener('click', () => {
    myText.textContent = 'New Text';
});
//---------------------------------------------select change text-------------------------------------------------------------
/*const mySelect = document.querySelector('#mySelect');
const myText = document.querySelector('#myText');

mySelect.addEventListener('change', () => {
    if (mySelect.value === 'option1') {
        myText.textContent = 'New Text 1';
    } else if (mySelect.value === 'option2') {
        myText.textContent = 'New Text 2';
    } else if (mySelect.value === 'option3') {
        myText.textContent = 'New Text 3';
    }
});*/
//-----------------------------------------------------------------------------------------------------------
/*const image1 = document.querySelector('#image1');
const image2 = document.querySelector('#image2');

image1.addEventListener('mouseover', () => {
    image1.style.display = 'none';
    image2.style.display = 'block';
});

image2.addEventListener('mouseout', () => {
    image1.style.display = 'block';
    image2.style.display = 'none';
});*/
