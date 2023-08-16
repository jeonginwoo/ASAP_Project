
const order_list = document.querySelector('.ordered-list');
const order_result = document.getElementById('result-price');

window.result_price = 0;   // 총 주문 금액
window.item_list = [];     // 주문 리스트


order_result.innerText = result_price.toLocaleString('ko-KR') + '원';

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

    result_price += menu_price;

    const ordered_item = document.importNode(document.querySelector('#temp').content, true);

    ordered_item.querySelector('.ordered-item').setAttribute('id', menu_name);
    ordered_item.querySelector('.menu-name').textContent = menu_name;
    ordered_item.getElementById('menu-img').setAttribute('src', menu_img);
    ordered_item.querySelector('#menu-price').textContent = menu_price.toLocaleString('ko-KR') + ' 원';
    ordered_item.getElementById('menu-etc').innerText = menu_etc;

    order_list.append(ordered_item);
    order_result.innerText = result_price.toLocaleString('ko-KR') + '원';
};

/**
 * object 정보에 해당하는 주문 item을 html 문서에서 삭제
 * 
 * delete_item 메소드에서 사용
 * 
 * @param {*} object 
 */
function delete_item_html(object) {
    const menu_name = object.name;
    const menu_price = object.price;

    const item = document.getElementById(menu_name);
    item.remove();
    item_list
    result_price -= menu_price;
    order_result.innerText = result_price.toLocaleString('ko-KR') + '원';
};

/**
 * object에 해당하는 주문 item을 추가
 * 
 * @param {*} object -
 * - object.name(String): 메뉴의 이름
 * - object.img(String): 메뉴 이미지의 저장 위치
 * - object.price(Number): 메뉴 가격
 * - object.etc(String): 메뉴 세부 정보 (ex. 단품/세트, 치즈 추가, 토마토 제외 등...)
 */
function add_item(object) {
    add_item_html(object);
    item_list.push(object);
};

/**
 * object에 해당하는 주문 item을 삭제
 * 
 * @param {*} object -
 * - object.name(String): 메뉴의 이름
 * - object.img(String): 메뉴 이미지의 저장 위치
 * - object.price(Number): 메뉴 가격
 * - object.etc(String): 메뉴 세부 정보 (ex. 단품/세트, 치즈 추가, 토마토 제외 등...)
 */
function delete_item(object) {
    let index_of_item = item_list.indexOf(object);

    delete_item_html(object);
    item_list.splice(index_of_item, 1);
};

//----- add_item 테스트 -----//


for (let i = 0; i < 10; i++) {

    const img_list = ["static/img/BURGERKING_MENU/Burger/와퍼.png", "static/img/BURGERKING_MENU/Burger/갈릭불고기와퍼.png", "static/img/BURGERKING_MENU/Burger/몬스터와퍼.png", "static/img/BURGERKING_MENU/Burger/와퍼주니어.png", "static/img/BURGERKING_MENU/Burger/블랙바비큐와퍼.png", "static/img/BURGERKING_MENU/Burger/비프&슈림프버거.png", "static/img/BURGERKING_MENU/Burger/헬로_디아블로_와퍼.png", "static/img/BURGERKING_MENU/Burger/치즈와퍼.png", "static/img/BURGERKING_MENU/Burger/통새우와퍼.png", "static/img/BURGERKING_MENU/Burger/치킨킹.png"];
    let menu_name = '메뉴' + String(i + 1);
    let menu_img = img_list[i];

    let menu_price = Math.floor(Math.random() * 50000);
    let menu_etc = '테스트 테스트 테스트';

    // // 현재 스크립트 파일의 경로 가져오기
    // const scriptElement = document.currentScript;
    // const scriptSrc = scriptElement.src;

    // // 스크립트 파일의 경로에서 이미지 폴더의 경로 계산
    // const scriptFolderPath = scriptSrc.substring(0, scriptSrc.lastIndexOf('/'));


    // console.log("Image Folder Path:", scriptFolderPath);



    let object = { name: menu_name, img: menu_img, price: menu_price, etc: menu_etc };

    add_item(object);
};

for (let i = 0; i < 4; i++) {
    let random_object = item_list[Math.floor(Math.random() * item_list.length)];

    delete_item(random_object);
};

