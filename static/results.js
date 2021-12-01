let newSearch = document.getElementById('newSearch');
newSearch.addEventListener('click', () => {
    window.location.href = '/search';
});

let homeButton = document.getElementById('home');
homeButton.addEventListener('click', () => {
    window.location.href = '/';
})