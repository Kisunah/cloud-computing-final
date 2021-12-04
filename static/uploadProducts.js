let product_num = document.getElementById('product_num');
let department = document.getElementById('department');
let commodity = document.getElementById('commodity');
let brand_ty = document.getElementById('brand_ty');
let natural_organic_flag = document.getElementById('natural_organic_flag');
let uploadButton = document.getElementById('uploadButton');

product_num.addEventListener('input', (event) => {
    if (event.target.value == ''  || department.value == '' || commodity.value == '' || brand_ty.value == '' || natural_organic_flag.value == '') {
        uploadButton.style.pointerEvents = 'none';
        uploadButton.style.cursor = 'default';
        uploadButton.style.backgroundColor = 'grey';
    } else {
        uploadButton.style.pointerEvents = 'all';
        uploadButton.style.cursor = 'pointer';
        uploadButton.style.backgroundColor = '#E00122';
    }
});

department.addEventListener('input', (event) => {
    if (product_num.value == ''  || event.target.value == '' || commodity.value == '' || brand_ty.value == '' || natural_organic_flag.value == '') {
        uploadButton.style.pointerEvents = 'none';
        uploadButton.style.cursor = 'default';
        uploadButton.style.backgroundColor = 'grey';
    } else {
        uploadButton.style.pointerEvents = 'all';
        uploadButton.style.cursor = 'pointer';
        uploadButton.style.backgroundColor = '#E00122';
    }
});

commodity.addEventListener('input', (event) => {
    if (product_num.value == ''  || department.value == '' || event.target.value == '' || brand_ty.value == '' || natural_organic_flag.value == '') {
        uploadButton.style.pointerEvents = 'none';
        uploadButton.style.cursor = 'default';
        uploadButton.style.backgroundColor = 'grey';
    } else {
        uploadButton.style.pointerEvents = 'all';
        uploadButton.style.cursor = 'pointer';
        uploadButton.style.backgroundColor = '#E00122';
    }
});

brand_ty.addEventListener('input', (event) => {
    if (product_num.value == ''  || department.value == '' || commodity.value == '' || event.target.value == '' || natural_organic_flag.value == '') {
        uploadButton.style.pointerEvents = 'none';
        uploadButton.style.cursor = 'default';
        uploadButton.style.backgroundColor = 'grey';
    } else {
        uploadButton.style.pointerEvents = 'all';
        uploadButton.style.cursor = 'pointer';
        uploadButton.style.backgroundColor = '#E00122';
    }
});

natural_organic_flag.addEventListener('input', (event) => {
    if (product_num.value == ''  || department.value == '' || commodity.value == '' || brand_ty.value == '' || event.target.value == '') {
        uploadButton.style.pointerEvents = 'none';
        uploadButton.style.cursor = 'default';
        uploadButton.style.backgroundColor = 'grey';
    } else {
        uploadButton.style.pointerEvents = 'all';
        uploadButton.style.cursor = 'pointer';
        uploadButton.style.backgroundColor = '#E00122';
    }
});
