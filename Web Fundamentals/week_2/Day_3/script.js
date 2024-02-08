const textElement = document.querySelector('#myText');

textElement.addEventListener('click', () => {
alert('Loading weather report..');
});
const box = document.querySelector('#myBox');
box.addEventListener('click', () => {
box.remove();
});
document.getElementById('degree').addEventListener('change', function() {
    const degreeElements = document.querySelectorAll('.degree span');
    const selectedOption = this.value;

    // Assuming you have an array of temperatures for both C and F
    const temperatures = {
        C: [24, 18, 27, 19, 21, 16, 26, 21],
        F: [75, 65, 80, 66, 69, 61, 78, 70]
    };

    // Loop through each degree element and update its text
    degreeElements.forEach((degreeElement, index) => {
        degreeElement.textContent = temperatures[selectedOption][index] + '°';
    });
});