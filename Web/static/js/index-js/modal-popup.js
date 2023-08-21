const modal_info = document.getElementById('modal-info');
const scribe_button = document.getElementById('scribe');
const modal_info_close_button_up = modal_info.querySelector('.btn-close');
const modal_info_close_button_down = modal_info.querySelector('.btn-secondary');
const modal_info_image = modal_info.querySelector('.image');
const modal_info_content = modal_info.querySelector('.content');

const modal_select_set = document.getElementById('modal-select');
const select_set_button = document.getElementById('select-set');
const modal_select_set_close_button = modal_select_set.querySelector('.btn-secondary');
const modal_select_title = modal_select_set.querySelector('.modal-title');
const modal_select_set_btn = modal_select_set.querySelector('.set-btn');
const modal_select_mono_btn = modal_select_set.querySelector('.mono-btn');

let isScribe = false;
let isSelect = false;

let selected_menu = {name: '메뉴1', img: "static/img/BURGERKING_MENU/Burger/와퍼.png", price: 9000, etc: {set: 9000, mono: 4500}};

scribe_button.onclick = () => {
    if (!isScribe) isScribe = true;

    if (isScribe) {
        modal_info.style.display = "flex";
        image = "static/img/pubao_1.webp";

        modal_info_image.innerHTML = "<img src='" + selected_menu.img + "' style='display: block; margin: 0px auto;' width='300' height='200'/>";
        modal_info_content.innerHTML = "<h2 style='margin-top: 1.2rem'>" + selected_menu.name + "</h2><hr><p>" + selected_menu.price.toLocaleString('ko-KR') + "원 <br> 테스트 테스트 <br> 테스트 테스트" + "</p>";
    };
};

// select_set_button.onclick = () => {
//     selected_menu = {name: '메뉴1', img: "static/img/BURGERKING_MENU/Burger/와퍼.png", price: 9000, etc: {set: 9000, mono: 4500}};

//     if (!isSelect) isSelect = true;

//     if (isSelect) {
//         modal_select_set.style.display = "flex";

//         modal_select_title.innerText = selected_menu.name;
//         modal_select_set_btn.innerText = '세트 ' + selected_menu.etc.set.toLocaleString('ko-KR') + '원';
//         modal_select_mono_btn.innerText = '단품 ' + selected_menu.etc.mono.toLocaleString('ko-KR') + '원';
//     };
// };

modal_info_close_button_up.addEventListener("click", () => {
    if (isScribe) isScribe = false;

    if (!isScribe) {
        modal_info.style.display = "none";

        modal_info_image.innerHTML = "";
        modal_info_content.innerHTML = "";
    }
});

modal_info_close_button_down.addEventListener("click", () => {
    if (isScribe) isScribe = false;

    if (!isScribe) {
        modal_info.style.display = "none";

        modal_info_image.innerHTML = "";
        modal_info_content.innerHTML = "";
    }
});

// modal_select_set_close_button.addEventListener("click", () => {
//     if (isSelect) isSelect = false;

//     if (!isSelect) {
//         modal_select_set.style.display = "none";

//         modal_select_title.innerText = "";
//         modal_select_mono_btn.innerText = "";
//         modal_select_set_btn.innerText = "";
//     }
// });

// modal_select_set_btn.onclick = () => {
//     const event = new Event('click');
//     modal_select_set_close_button.dispatchEvent(event);

//     selected_menu.etc = Object.keys(selected_menu.etc).reduce((result, key) => {
//         if (key !== 'mono') {
//             result[key] = selected_menu.etc[key];
//         }

//         return result;
//     }, {});

//     add_table(selected_menu);
// };

// modal_select_mono_btn.onclick = () => {
//     const event = new Event('click');
//     modal_select_set_close_button.dispatchEvent(event);

//     selected_menu.etc = Object.keys(selected_menu.etc).reduce((result, key) => {
//         if (key !== 'set') {
//             result[key] = selected_menu.etc[key];
//         }

//         return result;
//     }, {});

//     add_table(selected_menu);
// };