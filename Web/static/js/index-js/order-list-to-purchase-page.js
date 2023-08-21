const purchase_button = document.getElementById("purchase");

let itemsParam = '';    // URL에 주문 아이템들을 쿼리 스트링으로 넣기 위한 변수

purchase_button.onclick = () => {
    window.item_list.forEach(item => {
        itemsParam += item.name;
        // if (Object.keys(item.etc).length !== 0){
        //     itemsParam += ',' + item.price + ';'
        // }
        itemsParam += ',' + item.price + ';'
    }); // order-list.js의 item_list 변수에 저장된 주문한 item들 중 주문 item 이름과 가격만 가져와 쿼리 스트링을 구성한다.

    window.location.href = 'http://127.0.0.1:8000/main/purchase/?result_price=' + window.result_price + '&item_list=' + itemsParam;
};  // 결제 페이지로 이동하면서 총 주문 금액과 주문 list를 쿼리 스트링으로 보낸다.
