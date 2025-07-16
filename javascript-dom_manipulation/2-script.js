const red_header = document.querySelector('#red_header');

red_header.addEventListener('click', function () {
    document.querySelector('header').classList.add('red');
});