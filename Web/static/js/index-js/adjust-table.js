const menu_burger = document.getElementById('menu_burger');
const menu_side = document.getElementById('menu_side');
const menu_baverage = document.getElementById('menu_baverage');
const menu_recommend = document.getElementById('menu_recommend');
const table = document.getElementById('table');
const table_head = table.querySelector('#table_head');
const table_body = table.querySelector('#table_body');

/**
 * @param {*String} menu_type 
 * @param {*Number} menu_count 
 * @param {*Array} menu_list
 */
function adjust_table(menu_type, menu_count, menu_list) {
    table_head.innerHTML = "<tr>" + "<th colspan='3' scope='col'>" + menu_type + " 메뉴" + "</th>" + "</tr>";
    
    let html_text = '';

    for(let i = 0; i < menu_count; i++){
        if (i % 3 === 0) {
            if (i === 0) {
                html_text += '<tr><td>';
                // html_text += menu_type + menu_list[i];
                html_text += menu_type + String(i + 1);
                html_text += '</td>';
            }
            else {
                html_text += '</tr><tr>';
                html_text += '<td>';
                // html_text += menu_type + menu_list[i];
                html_text += menu_type + String(i + 1);
                html_text += '</td>';
            }
        }
        else {
            html_text += '<td>';
            // html_text += menu_type + menu_list[i];
            html_text += menu_type + String(i + 1);
            html_text += '</td>';
        }

        if (i === menu_count) {
            html_text += '</tr>';
        }
    };

    table_body.innerHTML = html_text;
}

menu_burger.onclick = () => {
    adjust_table('버거', 10, []);
};

menu_side.onclick = () => {
    adjust_table('사이드', 17, []);
};

menu_baverage.onclick = () => {
    adjust_table('음료', 5, []);
};

menu_recommend.onclick = () => {
    adjust_table('추천', 4, []);
};