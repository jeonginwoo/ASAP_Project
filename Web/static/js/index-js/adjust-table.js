const table = document.getElementById('table');
const table_body = table.querySelector('#table_body');
const order_result = document.getElementById('result-price');

window.result_price = 0;   // 총 주문 금액
window.item_list = [];     // 주문 리스트

order_result.innerText = result_price.toLocaleString('ko-KR') + '원';   // 총 결제 금액 보여주기

/**
 * 주문한 메뉴를 테이블에 추가시켜 줌
 * 
 * - object.name(String): 메뉴의 이름
 * - object.img(String): 메뉴 이미지의 저장 위치
 * - object.price(Number): 메뉴 가격
 * - object.etc(String): 메뉴 기타 정보
 * 
 * @param {*object} menu 
 */
function add_table(menu) {
    const row = document.createElement('tr');
    const td = document.createElement('td');
    const span = document.createElement('span');
    const button = document.createElement('button');

    span.textContent = menu.price.toLocaleString('ko-KR') + '원'
    span.style.marginRight = '10px';
    button.textContent = '취소';
    button.classList.add('cancel-button');
    td.textContent = menu.name;

    td.appendChild(span);
    td.appendChild(button);
    row.appendChild(td);

    table_body.appendChild(row);

    window.result_price += menu.price;
    window.item_list.push(menu);

    order_result.innerText = window.result_price.toLocaleString('ko-KR') + '원';

    button.addEventListener('click', () => {
        delete_table(row, menu);
    });
};

/**
 * 선택한 메뉴를 테이블에서 삭제함
 * 
 * @param {*HTMLTableRowElement} row
 * @param {*object} menu 
 */
function delete_table(row, menu) {
    row.remove();

    let index_of_item = item_list.indexOf(menu);
    window.item_list.splice(index_of_item, 1);

    window.result_price -= menu.price;

    order_result.innerText = window.result_price.toLocaleString('ko-KR') + '원';
};

//----- 테스트 -----//

// for (let i = 0; i < 10; i++) {
//     let menu_name = '메뉴' + String(i + 1);
//     let menu_price = Math.floor(Math.random() * 50000);
//     let menu_etc = {};

//     const random_num = Math.floor(Math.random() * 3);

//     if (random_num === 0) {
//         menu_etc = {set: menu_price};
//     }
//     else if (random_num === 1) {
//         menu_etc = {mono: menu_price / 2};
//     }

//     let object = { name: menu_name,  price: menu_price, etc: menu_etc };

//     add_table(object);
// };

// for (let i = 0; i < 7; i++) {
//     let random_object = item_list[Math.floor(Math.random() * item_list.length)];

//     delete_table(random_object);
// };

// function adjust_table(menu_type, menu_count, menu_list) {
//     console.log(menu_type, menu_count, menu_list);

//     table_head.innerHTML = "<tr>" + "<th colspan='3' scope='col'>" + menu_type + " 메뉴" + "</th>" + "</tr>";


//     let html_text = '';


//     for (let i = 0; i < menu_count; i++) {
//         if (i % 3 === 0) {
//             if (i === 0) {
//                 html_text += '<tr><td>';
//                 html_text += menu_list[i][0] + menu_list[i][1] + "<img src=" + "static/img/BURGERKING_MENU/" + menu_list[i][2] + " alt='이미지를 불러오지 못했습니다' height='150px' />";
//                 // html_text += menu_type + String(i + 1);
//                 html_text += '</td>';
//             }
//             else {
//                 html_text += '</tr><tr>';
//                 html_text += '<td>';
//                 html_text += menu_list[i][0] + menu_list[i][1] + "<img src=" + "static/img/BURGERKING_MENU/" + menu_list[i][2] + " alt='이미지를 불러오지 못했습니다' height='150px' />";

//                 //html_text += menu_type + String(i + 1);
//                 html_text += '</td>';
//             }
//         }
//         else {
//             html_text += '<td>';
//             html_text += menu_list[i][0] + menu_list[i][1] + "<img src=" + "static/img/BURGERKING_MENU/" + menu_list[i][2] + " alt='이미지를 불러오지 못했습니다' height='150px' />";
//             //html_text += menu_type + String(i + 1);
//             html_text += '</td>';
//         }

//         if (i === menu_count) {
//             html_text += '</tr>';
//         }
//     };

//     table_body.innerHTML = html_text;
// }

// menu_side.onclick = () => {
//     adjust_table('사이드', 17, []);
// };

// menu_baverage.onclick = () => {
//     adjust_table('음료', 5, []);
// };

// menu_recommend.onclick = () => {
//     adjust_table('추천', 4, []);
// };