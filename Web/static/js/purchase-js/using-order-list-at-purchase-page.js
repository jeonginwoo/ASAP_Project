const total_price = document.getElementById('result-price');    // 총 주문 금액
const urlParmas = new URLSearchParams(window.location.search);  // URL 쿼리 스트링
const resultPrice = Number(urlParmas.get('result_price'));  // 쿼리 스트링의 총 주문 금액 부분
const itemList = urlParmas.get('item_list');    // 쿼리 스트링의 주문 list 부분

const item_list = itemList.split(';');  // 주문 list의 각 item을 ; 단위로 나눔
item_list.splice(-1, 1);    // 마지막 item(NaN)는 제외

item_list.forEach((item) => {
    const item_info = item.split(",");
    const item_name = item_info[0]; // item 이름
    const item_price = Number(item_info[1]);    // item 가격
    const list_group = document.importNode(document.querySelector('#temp').content, true);
    const list_group_item = list_group.querySelector('.list-group-item');

    list_group_item.querySelector(".menu-name").innerText = item_name;
    list_group_item.querySelector(".menu-price").innerText = item_price.toLocaleString('ko-KR') + '원';

    document.querySelector('.list-group').appendChild(list_group);
});

total_price.innerText = '총 주문 금액: ' + resultPrice.toLocaleString('ko-KR') + '원';