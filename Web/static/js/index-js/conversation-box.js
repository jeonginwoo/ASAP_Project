const speak_textarea = document.getElementById('speak');
const answer_div = document.getElementById('answer');

function speak() {
    let temp_speak = "이 부분에 원하는 것을 입력하거나, 음성 인식 버튼을 눌러 원하는 것을 말해주세요.";

    speak_textarea.value = null;
    speak_textarea.setAttribute('placeholder', temp_speak);
};

function answer(answer_text) {
    let temp_answer = answer_text;

    answer_div.innerText = temp_answer;
};

speak(); 
answer("GPT 답변");

speak_textarea.addEventListener("keydown", (event) => { // 텍스트 입력 부분의 이벤트 리스너
    // textarea에서 Enter키를 누르면 작성한 내용이 서버로 이동 후, 답변을 받음
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();

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
            speak(); 

            if (data.status === 400 || data.status === 405)
                throw Error(data.message);  // 올바른 형식으로 Request를 보내지 않았다면 Error 발생

            // data에 받은 메뉴 정보 혹은 리스트를 통해 해당 정보 기반으로 테이블을 업데이트하거나 팝업을 띄울 예정

            answer(data.message);
        })
        .catch((err) => {
            alert(err);
        });
    };
});

/**
 * 서버에서 Response로 받을 때
 * data의 message 부분은 GPT의 답변 부분이며
 * data의 이외 메뉴 정보 혹은 리스트 정보를 받아 테이블을 업데이트하거나 팝업을 띄우는 형식으로 동작시킬 예정
 */