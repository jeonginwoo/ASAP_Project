const order_list = document.querySelector('.list-group');
const order_result = document.getElementById('result-price');
const ordered_item = document.importNode(document.querySelector('#temp').content, true);

item_list.forEach((item) => {
    ordered_item.querySelector('.list-group-item').textContent = item.name + '    ' + item.price.toLocaleString('ko-KR') + ' 원';
    order_list.append(ordered_item);
});

order_result.innerText = result_price.toLocaleString('ko-KR') + '원';