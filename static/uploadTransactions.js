let basket_num = document.getElementById('basket_num');
let hshd_num = document.getElementById('hshd_num');
let purchase_ = document.getElementById('purchase_');
let product_num = document.getElementById('product_num');
let spend = document.getElementById('spend');
let units = document.getElementById('units');
let store_r = document.getElementById('store_r');
let week_num = document.getElementById('week_num');
let year = document.getElementById('year');
let uploadButton = document.getElementById('uploadButton');

basket_num.addEventListener('input', (event) => {
    if (event.target.value == '' || hshd_num.value == '' || purchase_.value == ''  || product_num.value == '' || spend.value == '' || units.value == '' || store_r.value == '' || week_num.value == '' || year.value == '') {
        uploadButton.style.pointerEvents = 'none';
        uploadButton.style.cursor = 'default';
        uploadButton.style.backgroundColor = 'grey';
    } else {
        uploadButton.style.pointerEvents = 'all';
        uploadButton.style.cursor = 'pointer';
        uploadButton.style.backgroundColor = '#E00122';
    }
});

hshd_num.addEventListener('input', (event) => {
    if (basket_num.value == '' || event.target.value == '' || purchase_.value == ''  || product_num.value == '' || spend.value == '' || units.value == '' || store_r.value == '' || week_num.value == '' || year.value == '') {
        uploadButton.style.pointerEvents = 'none';
        uploadButton.style.cursor = 'default';
        uploadButton.style.backgroundColor = 'grey';
    } else {
        uploadButton.style.pointerEvents = 'all';
        uploadButton.style.cursor = 'pointer';
        uploadButton.style.backgroundColor = '#E00122';
    }
})

purchase_.addEventListener('input', (event) => {
    if (basket_num.value == '' || hshd_num.value == '' || event.target.value == ''  || product_num.value == '' || spend.value == '' || units.value == '' || store_r.value == '' || week_num.value == '' || year.value == '') {
        uploadButton.style.pointerEvents = 'none';
        uploadButton.style.cursor = 'default';
        uploadButton.style.backgroundColor = 'grey';
    } else {
        uploadButton.style.pointerEvents = 'all';
        uploadButton.style.cursor = 'pointer';
        uploadButton.style.backgroundColor = '#E00122';
    }
});

product_num.addEventListener('input', (event) => {
    if (basket_num.value == '' || hshd_num.value == '' || purchase_.value == ''  || event.target.value == '' || spend.value == '' || units.value == '' || store_r.value == '' || week_num.value == '' || year.value == '') {
        uploadButton.style.pointerEvents = 'none';
        uploadButton.style.cursor = 'default';
        uploadButton.style.backgroundColor = 'grey';
    } else {
        uploadButton.style.pointerEvents = 'all';
        uploadButton.style.cursor = 'pointer';
        uploadButton.style.backgroundColor = '#E00122';
    }
});

spend.addEventListener('input', (event) => {
    if (basket_num.value == '' || hshd_num.value == '' || purchase_.value == ''  || product_num.value == '' || event.target.value == '' || units.value == '' || store_r.value == '' || week_num.value == '' || year.value == '') {
        uploadButton.style.pointerEvents = 'none';
        uploadButton.style.cursor = 'default';
        uploadButton.style.backgroundColor = 'grey';
    } else {
        uploadButton.style.pointerEvents = 'all';
        uploadButton.style.cursor = 'pointer';
        uploadButton.style.backgroundColor = '#E00122';
    }
});

units.addEventListener('input', (event) => {
    if (basket_num.value == '' || hshd_num.value == '' || purchase_.value == ''  || product_num.value == '' || spend.value == '' || event.target.value == '' || store_r.value == '' || week_num.value == '' || year.value == '') {
        uploadButton.style.pointerEvents = 'none';
        uploadButton.style.cursor = 'default';
        uploadButton.style.backgroundColor = 'grey';
    } else {
        uploadButton.style.pointerEvents = 'all';
        uploadButton.style.cursor = 'pointer';
        uploadButton.style.backgroundColor = '#E00122';
    }
});

store_r.addEventListener('input', (event) => {
    if (basket_num.value == '' || hshd_num.value == '' || purchase_.value == ''  || product_num.value == '' || spend.value == '' || units.value == '' || event.target.value == '' || week_num.value == '' || year.value == '') {
        uploadButton.style.pointerEvents = 'none';
        uploadButton.style.cursor = 'default';
        uploadButton.style.backgroundColor = 'grey';
    } else {
        uploadButton.style.pointerEvents = 'all';
        uploadButton.style.cursor = 'pointer';
        uploadButton.style.backgroundColor = '#E00122';
    }
});

week_num.addEventListener('input', (event) => {
    if (basket_num.value == '' || hshd_num.value == '' || purchase_.value == ''  || product_num.value == '' || spend.value == '' || units.value == '' || store_r.value == '' || event.target.value == '' || year.value == '') {
        uploadButton.style.pointerEvents = 'none';
        uploadButton.style.cursor = 'default';
        uploadButton.style.backgroundColor = 'grey';
    } else {
        uploadButton.style.pointerEvents = 'all';
        uploadButton.style.cursor = 'pointer';
        uploadButton.style.backgroundColor = '#E00122';
    }
});

year.addEventListener('input', (event) => {
    if (basket_num.value == '' || hshd_num.value == '' || purchase_.value == ''  || product_num.value == '' || spend.value == '' || units.value == '' || store_r.value == '' || week_num.value == '' || event.target.value == '') {
        uploadButton.style.pointerEvents = 'none';
        uploadButton.style.cursor = 'default';
        uploadButton.style.backgroundColor = 'grey';
    } else {
        uploadButton.style.pointerEvents = 'all';
        uploadButton.style.cursor = 'pointer';
        uploadButton.style.backgroundColor = '#E00122';
    }
});
