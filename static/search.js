let searchButton = document.getElementById('searchButton');
searchButton.addEventListener('click', () => {
    hshd = document.getElementById('HSHD_NUM').value;
    sort = document.getElementById('sort').value;
    sortValue = document.getElementById('sortValue').value;
    window.location.href = `/results/${hshd}/${sort}/${sortValue}`;
});

homeButton = document.getElementById('home');
homeButton.addEventListener('click', () => {
    window.location.href = '/homepage';
});

let hshdInput = document.getElementById('HSHD_NUM');
let selectBox = document.getElementById('sort');
let valueInput = document.getElementById('sortValue');
let dateFormat = document.getElementById('dateFormat');

hshdInput.addEventListener('input', (event) => {
    console.log(event.target.value);
    console.log(selectBox.value);
    console.log(valueInput.value);
    
    if (event.target.value == '' || selectBox.value == '' || valueInput.value == '') {
        searchButton.style.pointerEvents = 'none';
        searchButton.style.cursor = 'default';
        searchButton.style.backgroundColor = 'grey';
    } else {
        searchButton.style.pointerEvents = 'all';
        searchButton.style.cursor = 'pointer';
        searchButton.style.backgroundColor = '#E00122';
    }
});

selectBox.addEventListener('change', (event) => {
    sortName = document.getElementById('sortName');

    if (event.target.value == '') {
        sortName.innerText = 'Value';
    } else {
        sortName.innerText = `${event.target.value}:`;
        if (event.target.value === 'DATE') dateFormat.innerText = 'Date Format is YYYY-MM-DD';
        else dateFormat.innerText = '\n';
    }


    if (event.target.value == '' || hshdInput.value == '' || valueInput.value == '') {
        searchButton.style.pointerEvents = 'none';
        searchButton.style.cursor = 'default';
        searchButton.style.backgroundColor = 'grey';
    } else {
        searchButton.style.pointerEvents = 'all';
        searchButton.style.cursor = 'pointer';
        searchButton.style.backgroundColor = '#E00122';
    }
});

valueInput.addEventListener('input', (event) => {
    if (event.target.value == '' || hshdInput.value == '' || selectBox.value == '') {
        searchButton.style.pointerEvents = 'none';
        searchButton.style.cursor = 'default';
        searchButton.style.backgroundColor = 'grey';
    } else {
        searchButton.style.pointerEvents = 'all';
        searchButton.style.cursor = 'pointer';
        searchButton.style.backgroundColor = '#E00122';
    }
});