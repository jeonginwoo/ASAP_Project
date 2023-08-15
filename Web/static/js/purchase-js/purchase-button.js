const button_card = document.querySelector('.btn-outline-primary');
const button_cache = document.querySelector('.btn-outline-success');

button_card.onclick = () => {
    alert(button_card.textContent + '로 결제합니다.');
    window.location.href = 'http://127.0.0.1:8000/';
};

button_cache.onclick = () => {
    alert(button_cache.textContent + '으로 결제합니다.');
    window.location.href = 'http://127.0.0.1:8000/';
};