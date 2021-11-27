searchSql = document.getElementById('searchSql');
searchSql.addEventListener('click', () => {
    hshd = document.getElementById('HSHD_NUM').value;
    sort = document.getElementById('sort').value;
    sortValue = document.getElementById('sortValue').value;
    window.location.href = `results/${hshd}/${sort}/${sortValue}`;
});