function speak() {
    const speak_div = document.getElementById('speak');

    let temp_speak = "사용자 입력 테스트 부분";

    speak_div.innerText = temp_speak;
};

function answer() {
    const answer_div = document.getElementById('answer');

    let temp_answer = "GPT 답변 테스트 부분";

    answer_div.innerText = temp_answer;
};

speak();
answer();
