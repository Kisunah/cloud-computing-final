let sample = document.getElementById('sample');
sample.addEventListener('click', () => {
    window.location.href = '/sample'
});

let search = document.getElementById('search');
search.addEventListener('click', () => {
    window.location.href = '/search'
});

let question1 = document.getElementById('question1');
question1.addEventListener('click', () => {
    window.location.href = 'question1';
});

let question2 = document.getElementById('question2');
question2.addEventListener('click', () => {
    window.location.href = 'question2';
});

let uploadTransactions = document.getElementById('uploadTransactions');
uploadTransactions.addEventListener('click', () => {
    window.location.href = 'uploadTransactions';
});

let uploadProducts = document.getElementById('uploadProducts');
uploadProducts.addEventListener('click', () => {
    window.location.href = 'uploadProducts';
});

let uploadHouseholds = document.getElementById('uploadHouseholds');
uploadHouseholds.addEventListener('click', () => {
    window.location.href = 'uploadHouseholds';
});
