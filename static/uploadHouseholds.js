let homeButton = document.getElementById('home');
homeButton.addEventListener('click', () => {
  window.location.href = '/homepage';
});

let hshd_num = document.getElementById('hshd_num');
let l = document.getElementById('l');
let age_range = document.getElementById('age_range');
let marital = document.getElementById('marital');
let income_range = document.getElementById('income_range');
let homeowner = document.getElementById('homeowner');
let hshd_composition = document.getElementById('hshd_composition');
let hh_size = document.getElementById('hh_size');
let children = document.getElementById('children');
let uploadButton = document.getElementById('uploadButton');

hshd_num.addEventListener('input', (event) => {
  if (event.target.value == '' || l.value == '' || age_range.value == '' || marital.value == '' || income_range.value == '' || homeowner.value == '' || hshd_composition.value == '' || hh_size.value == '' || children.value == '') {
    uploadButton.style.pointerEvents = 'none';
    uploadButton.style.cursor = 'default';
    uploadButton.style.backgroundColor = 'grey';
  } else {
    uploadButton.style.pointerEvents = 'all';
    uploadButton.style.cursor = 'pointer';
    uploadButton.style.backgroundColor = '#E00122';
  }
});

l.addEventListener('input', (event) => {
  if (hshd_num.value == '' || event.target.value == '' || age_range.value == '' || marital.value == '' || income_range.value == '' || homeowner.value == '' || hshd_composition.value == '' || hh_size.value == '' || children.value == '') {
    uploadButton.style.pointerEvents = 'none';
    uploadButton.style.cursor = 'default';
    uploadButton.style.backgroundColor = 'grey';
  } else {
    uploadButton.style.pointerEvents = 'all';
    uploadButton.style.cursor = 'pointer';
    uploadButton.style.backgroundColor = '#E00122';
  }
});

age_range.addEventListener('input', (event) => {
  if (hshd_num.value == '' || l.value == '' || event.target.value == '' || marital.value == '' || income_range.value == '' || homeowner.value == '' || hshd_composition.value == '' || hh_size.value == '' || children.value == '') {
    uploadButton.style.pointerEvents = 'none';
    uploadButton.style.cursor = 'default';
    uploadButton.style.backgroundColor = 'grey';
  } else {
    uploadButton.style.pointerEvents = 'all';
    uploadButton.style.cursor = 'pointer';
    uploadButton.style.backgroundColor = '#E00122';
  }
});

marital.addEventListener('input', (event) => {
  if (hshd_num.value == '' || l.value == '' || age_range.value == '' || event.target.value == '' || income_range.value == '' || homeowner.value == '' || hshd_composition.value == '' || hh_size.value == '' || children.value == '') {
    uploadButton.style.pointerEvents = 'none';
    uploadButton.style.cursor = 'default';
    uploadButton.style.backgroundColor = 'grey';
  } else {
    uploadButton.style.pointerEvents = 'all';
    uploadButton.style.cursor = 'pointer';
    uploadButton.style.backgroundColor = '#E00122';
  }
});

income_range.addEventListener('input', (event) => {
  if (hshd_num.value == '' || l.value == '' || age_range.value == '' || marital.value == '' || event.target.value == '' || homeowner.value == '' || hshd_composition.value == '' || hh_size.value == '' || children.value == '') {
    uploadButton.style.pointerEvents = 'none';
    uploadButton.style.cursor = 'default';
    uploadButton.style.backgroundColor = 'grey';
  } else {
    uploadButton.style.pointerEvents = 'all';
    uploadButton.style.cursor = 'pointer';
    uploadButton.style.backgroundColor = '#E00122';
  }
});

homeowner.addEventListener('input', (event) => {
  if (hshd_num.value == '' || l.value == '' || age_range.value == '' || marital.value == '' || income_range.value == '' || event.target.value == '' || hshd_composition.value == '' || hh_size.value == '' || children.value == '') {
    uploadButton.style.pointerEvents = 'none';
    uploadButton.style.cursor = 'default';
    uploadButton.style.backgroundColor = 'grey';
  } else {
    uploadButton.style.pointerEvents = 'all';
    uploadButton.style.cursor = 'pointer';
    uploadButton.style.backgroundColor = '#E00122';
  }
});

hshd_composition.addEventListener('input', (event) => {
  if (hshd_num.value == '' || l.value == '' || age_range.value == '' || marital.value == '' || income_range.value == '' || homeowner.value == '' || event.target.value == '' || hh_size.value == '' || children.value == '') {
    uploadButton.style.pointerEvents = 'none';
    uploadButton.style.cursor = 'default';
    uploadButton.style.backgroundColor = 'grey';
  } else {
    uploadButton.style.pointerEvents = 'all';
    uploadButton.style.cursor = 'pointer';
    uploadButton.style.backgroundColor = '#E00122';
  }
});

hh_size.addEventListener('input', (event) => {
  if (hshd_num.value == '' || l.value == '' || age_range.value == '' || marital.value == '' || income_range.value == '' || homeowner.value == '' || hshd_composition.value == '' || event.target.value == '' || children.value == '') {
    uploadButton.style.pointerEvents = 'none';
    uploadButton.style.cursor = 'default';
    uploadButton.style.backgroundColor = 'grey';
  } else {
    uploadButton.style.pointerEvents = 'all';
    uploadButton.style.cursor = 'pointer';
    uploadButton.style.backgroundColor = '#E00122';
  }
});

children.addEventListener('input', (event) => {
  if (hshd_num.value == '' || l.value == '' || age_range.value == '' || marital.value == '' || income_range.value == '' || homeowner.value == '' || hshd_composition.value == '' || hh_size.value == '' || event.target.value == '') {
    uploadButton.style.pointerEvents = 'none';
    uploadButton.style.cursor = 'default';
    uploadButton.style.backgroundColor = 'grey';
  } else {
    uploadButton.style.pointerEvents = 'all';
    uploadButton.style.cursor = 'pointer';
    uploadButton.style.backgroundColor = '#E00122';
  }
});
