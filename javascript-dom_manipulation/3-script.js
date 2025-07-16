const toggle_header = document.querySelector('#toggle_header');

toggle_header.addEventListener('click', function () {
    const header = document.querySelector('header');
    switch (header.className) {
        case 'red':
            header.className = 'green';
            break;
        case 'green':
            header.className = 'red';
            break;
        default:
            header.className = 'red';
            break;
    }
});