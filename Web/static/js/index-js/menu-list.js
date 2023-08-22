const menu_list = document.querySelector('.ordered-list');

let item_list = [];     // 주문 리스트
let active_item = null;

/**
 * item_list가 비어있으면 menu list를 감추고, 있으면 표시해줌
 */
function is_box_visible() {
    if(item_list.length !== 0) {
        menu_list.setAttribute('style', 'display: visible;');
    }
    else {
        menu_list.setAttribute('style', 'display: none;');
    }
}

is_box_visible();

/**
 * object 정보에 해당하는 주문 item을 html 문서에 추가
 *
 * add_item 메소드에서 사용
 *
 * @param {*} object
 */
function add_item_html(object) {
    const menu_name = object.name;
    const menu_img = object.img;
    const menu_price = object.price;
    const menu_etc = object.etc;

    const menu_item = document.importNode(document.querySelector('#temp').content, true);

    menu_item.querySelector('.ordered-item').setAttribute('id', menu_name);
    menu_item.querySelector('.menu-name').textContent = menu_name;
    menu_item.getElementById('menu-img').setAttribute('src', menu_img);
    menu_item.querySelector('#menu-price').textContent = menu_price.toLocaleString('ko-KR') + ' 원';

    const ordered_item = menu_item.querySelector('.ordered-item');

    ordered_item.addEventListener('click', () => {
        add_table({name: menu_name, img: menu_img, price: menu_price, etc: menu_etc});
    });

    menu_list.append(menu_item);
};

/**
 * object 정보에 해당하는 주문 item을 html 문서에서 삭제
 *
 * delete_item 메소드에서 사용
 *
 * @param {*} object
 */
function delete_item_html(object) {
    object.remove();
};

/**
 * object에 해당하는 주문 item을 추가
 * 
 * - object.name(String): 메뉴의 이름
 * - object.img(String): 메뉴 이미지의 저장 위치
 * - object.price(Number): 메뉴 가격
 * - object.etc(String): 메뉴 기타 정보
 *
 * @param {*object} object
 */
function add_item(object) {
    add_item_html(object);
    item_list.push(object);
};

/**
 * 모든 메뉴 item을 삭제
 */
function delete_items() {
    const menu_list = document.querySelector('.ordered-list');
    const menu_list_length = menu_list.children.length

    if (menu_list_length !== 1) {
        for(let i = 1; i < menu_list_length; i++) {
            delete_item_html(menu_list.children[1]);
            item_list.pop();
        }
    }
};

/**
 * list에 저장된 item들을 모두 보여줌
 * 
 * 이때, list의 원소 item의 구성은 다음과 같음
 * 
 * - item.name(String): 메뉴의 이름
 * - item.img(String): 메뉴 이미지의 저장 위치
 * - item.price(Number): 메뉴 가격
 * - item.etc(String): 메뉴 기타 정보
 * 
 * @param {*Array} list 
 */
function show_menu_list(list) {
    delete_items();

    list.forEach((item) => {
        add_item(item);
    });

    is_box_visible();
};



//----- 테스트 -----//

// const img_list = ["static/img/BURGERKING_MENU/Burger/와퍼.png", "static/img/BURGERKING_MENU/Burger/갈릭불고기와퍼.png", "static/img/BURGERKING_MENU/Burger/몬스터와퍼.png", "static/img/BURGERKING_MENU/Burger/와퍼주니어.png", "static/img/BURGERKING_MENU/Burger/블랙바비큐와퍼.png", "static/img/BURGERKING_MENU/Burger/비프&슈림프버거.png", "static/img/BURGERKING_MENU/Burger/헬로_디아블로_와퍼.png", "static/img/BURGERKING_MENU/Burger/치즈와퍼.png", "static/img/BURGERKING_MENU/Burger/통새우와퍼.png", "static/img/BURGERKING_MENU/Burger/치킨킹.png"];

// for (let i = 0; i < 4; i++) {
//     let menu_name = '메뉴' + String(i + 1);
//     let menu_img = img_list[i];
//     let menu_price = Math.floor(Math.random() * 50000);
//     let menu_etc = {};

    // const random_num = Math.floor(Math.random() * 2);
    // if (random_num === 0) {
    //     menu_etc = {set: menu_price, mono: menu_price / 2};
    // }

//     let object = { name: menu_name, img: menu_img, price: menu_price};

//     item_list.push(object);
// };

// show_menu_list(item_list);

// item_list = [];

// for (let i = 0; i < 4; i++) {
//     let menu_name = '메뉴' + String(i + 1);
//     let menu_img = img_list[i];
//     let menu_price = Math.floor(Math.random() * 50000);
//     let menu_etc = {};

//     // const random_num = Math.floor(Math.random() * 2);
//     // if (random_num === 0) {
//     //     menu_etc = {set: menu_price, mono: menu_price / 2};
//     // }

//     let object = { name: menu_name, img: menu_img, price: menu_price };

//     item_list.push(object);
// };

// show_menu_list(item_list);

// for (let i = 0; i < 6; i++) {
//     let random_object = item_list[Math.floor(Math.random() * item_list.length)];

//     delete_item(random_object);
// };
