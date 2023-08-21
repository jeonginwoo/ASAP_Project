const table = document.getElementById('table');
const table_body = table.querySelector('#table_body');
const order_result = document.getElementById('result-price');

window.result_price = 0;   // 총 주문 금액
window.item_list = [];     // 주문 리스트

order_result.innerText = result_price.toLocaleString('ko-KR') + '원';

/**
 * 주문한 메뉴를 테이블에 추가시켜 줌
 * 
 * @param {*object} menu 
 */
function add_table(menu) {
    // if (Object.keys(menu.etc)[0] === 'set'){
    //     table_body.innerHTML += '<tr id="menu_' + menu.name + '"><td>' + menu.name + "<br>-&nbsp세트" + "<span>" + menu.price.toLocaleString('ko-KR') + '원' + '&nbsp;&nbsp;&nbsp;</span></td></tr>';
    //     window.result_price += menu.price;
    // }
    // else if (Object.keys(menu.etc)[0] === 'mono') {
    //     table_body.innerHTML += '<tr id="menu_' + menu.name + '"><td>' + menu.name + "<br>-&nbsp단품" + "<span>" + menu.etc.mono.toLocaleString('ko-KR') + '원' + '&nbsp;&nbsp;&nbsp;</span></td></tr>';
    //     window.result_price += menu.etc.mono;
    // }
    // else {
    //     table_body.innerHTML += '<tr id="menu_' + menu.name + '"><td>' + menu.name + "<span>" + menu.price.toLocaleString('ko-KR') + '원' + '&nbsp;&nbsp;&nbsp;</span></td></tr>';
    //     window.result_price += menu.price;
    // }


    table_body.innerHTML += '<tr id="menu_' + menu.name + '"><td>' + menu.name + "<span>" + menu.price.toLocaleString('ko-KR') + '원' + '&nbsp;&nbsp;&nbsp;</span></td></tr>';
    window.result_price += menu.price;
    window.item_list.push(menu);

    order_result.innerText = window.result_price.toLocaleString('ko-KR') + '원';
};

/**
 * 선택한 메뉴를 테이블에서 삭제함
 * 
 * @param {*object} menu 
 */
function delete_table(menu) {
    let index_of_item = item_list.indexOf(menu);
    const item = document.getElementById('menu_' + menu.name);

    item.remove();
    window.item_list.splice(index_of_item, 1);

    // if (Object.keys(menu.etc)[0] === 'set' || Object.keys(menu.etc)[0] === undefined)   window.result_price -= menu.price;
    // else window.result_price -= menu.etc.mono;

    window.result_price -= menu.price;

    order_result.innerText = window.result_price.toLocaleString('ko-KR') + '원';
};

//----- 테스트 -----//

for (let i = 0; i < 10; i++) {
    let menu_name = '메뉴' + String(i + 1);
    let menu_price = Math.floor(Math.random() * 50000);
    let menu_etc = {};

    const random_num = Math.floor(Math.random() * 3);

    if (random_num === 0) {
        menu_etc = {set: menu_price};
    }
    else if (random_num === 1) {
        menu_etc = {mono: menu_price / 2};
    }

    let object = { name: menu_name,  price: menu_price, etc: menu_etc };

    add_table(object);
};

for (let i = 0; i < 7; i++) {
    let random_object = item_list[Math.floor(Math.random() * item_list.length)];

    delete_table(random_object);
};

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