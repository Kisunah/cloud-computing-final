let username = document.getElementById('username');
let password = document.getElementById('password');
let signInButton = document.getElementById('signInButton');

username.addEventListener('input', (event) => {
    if (event.target.value == '' || password.value == '') {
        signInButton.style.pointerEvents = 'none';
        signInButton.style.cursor = 'default';
        signInButton.style.backgroundColor = 'grey';
    } else {
        signInButton.style.pointerEvents = 'all';
        signInButton.style.cursor = 'pointer';
        signInButton.style.backgroundColor = '#E00122';
    }
});

password.addEventListener('input', (event) => {
    if (event.target.value == '' || username.value == '') {
        signInButton.style.pointerEvents = 'none';
        signInButton.style.cursor = 'default';
        signInButton.style.backgroundColor = 'grey';
    } else {
        signInButton.style.pointerEvents = 'all';
        signInButton.style.cursor = 'pointer';
        signInButton.style.backgroundColor = '#E00122';
    }
});