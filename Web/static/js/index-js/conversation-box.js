const speak_textarea = document.getElementById('speak');
const answer_div = document.getElementById('answer');

let timeout;

/**
 * 사용자의 음성을 텍스트로 보여주는 메소드
 *
 * @param {*String} speak_text
 */
function speak(speak_text) {
    let temp_speak = "이 부분에 원하는 것을 입력하거나, 음성 인식 버튼을 눌러 원하는 것을 말해주세요.";

    speak_textarea.setAttribute('placeholder', temp_speak);

    if (speak_text === undefined) // Default
        speak_textarea.value = null;
    else
        speak_textarea.value = speak_text;
};

/**
 * GPT의 답변을 div에 띄워주는 메소드
 *
 * @param {*String} answer_text
 */
function answer(answer_text) {
    let temp_answer = answer_text;

    answer_div.innerText = temp_answer;
};

speak(undefined);
answer("GPT 답변");

speak_textarea.addEventListener("keydown", (event) => { // 텍스트 입력 부분의 이벤트 리스너
    // textarea에서 Enter키를 누르면 작성한 내용이 서버로 이동 후, 답변을 받음
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();

        clearTimeout(timeout);

        timeout = setTimeout(() => {
            fetch("http://127.0.0.1:8000/main/textinput/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,   //CSRF 토큰 값을 같이 헤더에 추가해 403 Fobbiden 에러 방지
                },
                body: JSON.stringify({
                    value: event.target.value
                }),
            })
            .then((response) => response.json())
            .then((data) => {
                if (data.status === 400 || data.status === 405)
                    throw Error(data.message);  // 올바른 형식으로 Request를 보내지 않았다면 Error 발생

                const menu_list = [];

                if (data.burger_list) {
                    data.burger_list.forEach(item => {
                        const name = item.fields.menu_name;
                        const img = 'static/img/BURGERKING_MENU/' + item.fields.image;
                        const price = item.fields.price;
                        const etc = item.fields.info;

                        menu_list.push({ name: name, img: img, price: price, etc: etc });
                    });
                }

                if (data.side_list) {
                    data.side_list.forEach(item => {
                        const name = item.fields.menu_name;
                        const img = 'static/img/BURGERKING_MENU/' + item.fields.image;
                        const price = item.fields.price;
                        const etc = item.fields.info;

                        menu_list.push({ name: name, img: img, price: price, etc: etc });
                    });
                }

                if (data.dd_list) {
                    data.dd_list.forEach(item => {
                        const name = item.fields.menu_name;
                        const img = 'static/img/BURGERKING_MENU/' + item.fields.image;
                        const price = item.fields.price;
                        const etc = item.fields.info;

                        menu_list.push({ name: name, img: img, price: price, etc: etc });
                    });
                }

                show_menu_list(menu_list);
                speak(data.speaker);

                if (menu_list.length === 0) {
                    answer(data.error);
                }
                else {
                    answer(data.answer);
                }
            })
            .catch((err) => {
                alert(err);
            });
        }, 50);
    };
});
