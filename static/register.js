let registerButton = document.getElementById('registerButton');
let username = document.getElementById('username');
let password = document.getElementById('password');
let verifyPassword = document.getElementById('verifyPassword');
let email = document.getElementById('email');

username.addEventListener('input', (event) => {
    if (event.target.value == '' || password.value == '' || verifyPassword.value == ''  || email.value == '') {
        registerButton.style.pointerEvents = 'none';
        registerButton.style.cursor = 'default';
        registerButton.style.backgroundColor = 'grey';
    } else {
        registerButton.style.pointerEvents = 'all';
        registerButton.style.cursor = 'pointer';
        registerButton.style.backgroundColor = '#E00122';
    }
});

password.addEventListener('input', (event) => {
    if (username.value == '' || event.target.value == '' || verifyPassword.value == ''  || email.value == '') {
        registerButton.style.pointerEvents = 'none';
        registerButton.style.cursor = 'default';
        registerButton.style.backgroundColor = 'grey';
    } else {
        registerButton.style.pointerEvents = 'all';
        registerButton.style.cursor = 'pointer';
        registerButton.style.backgroundColor = '#E00122';
    }

    let passwordError = document.getElementById('passwordError');
    if (verifyPassword.value != event.target.value) {
        passwordError.innerText = 'Passwords do not match!';
    } else {
        passwordError.innerText = '';
    }
});

verifyPassword.addEventListener('input', (event) => {
    if (username.value == '' || password.value == '' || event.target.value == ''  || email.value == '') {
        registerButton.style.pointerEvents = 'none';
        registerButton.style.cursor = 'default';
        registerButton.style.backgroundColor = 'grey';
    } else {
        registerButton.style.pointerEvents = 'all';
        registerButton.style.cursor = 'pointer';
        registerButton.style.backgroundColor = '#E00122';
    }

    let passwordError = document.getElementById('passwordError');
    if (password.value != event.target.value) {
        passwordError.innerText = 'Passwords do not match!';
    } else {
        passwordError.innerText = '';
    }
});

email.addEventListener('input', (event) => {
    if (username.value == '' || password.value == '' || verifyPassword.value == '' || event.target.value == '') {
        registerButton.style.pointerEvents = 'none';
        registerButton.style.cursor = 'default';
        registerButton.style.backgroundColor = 'grey';
    } else {
        registerButton.style.pointerEvents = 'all';
        registerButton.style.cursor = 'pointer';
        registerButton.style.backgroundColor = '#E00122';
    }
});