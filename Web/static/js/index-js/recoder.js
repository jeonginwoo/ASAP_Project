const record = document.getElementById('record_button');
const audio = document.getElementById('audioPlayer');
const csrfToken = document.getElementById('csrfToken').value;   //Django CSRF 토큰 값
let isRecording = false;

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {    // 기기의 마이크 지원 여부 판정
    navigator.mediaDevices.getUserMedia({audio: true})  // 기기의 마이크 입력을 사용할 수 있게 설정
    .then((stream) => {
        const mediaRecorder = new MediaRecorder(stream);    // 음성 녹음을 위해 MediaRecoder에 마이크 연결

        record.onclick = () => {
            if (!isRecording) {
                let chunks = [];

                mediaRecorder.ondataavailable = async (event) => {  // 음성 녹음 중 1초 단위로 chunks에 데이터를 push
                    chunks.push(event.data);
                };

                mediaRecorder.onstop = (event) => { // 음성 녹음이 종료되면 실행
                    const recordData = new Blob(chunks, { "type": "audio/mpeg codecs=opus" });

                    fetch('http://127.0.0.1:8000/main/speechrecognize/', {
                        method: "POST",
                        headers: {
                            "Content-Type": "audio/mpeg",
                            "X-CSRFToken": csrfToken,   //CSRF 토큰 값을 같이 헤더에 추가해 403 Fobbiden 에러 방지
                        },
                        body: recordData,   //녹음된 음성 데이터
                    })
                    .then((response) => response.json())    //response를 json으로 파싱
                    .then((data) => {
                        console.log(data.burger_list);
                        console.log(data.side_list);
                        console.log(data.dd_list);
                        console.log(data.speaker);
                        console.log(data.error);
                    })
                    .catch((err) => {
                        location.href = err;
                    });
                };

                mediaRecorder.start(1000);  // 녹음 시작
                isRecording = true;

                record.style.background = "red";
                record.style.color = "black";

                setTimeout(() => {  // 3초 후 녹음 종료
                    if (mediaRecorder.state = 'recording') {
                        mediaRecorder.stop();

                        record.style.background = "";
                        record.style.color = "";
                    };

                isRecording = false;
                }, 3000)
            }
        };
    }).catch((err) => {
        alert("음성 녹음 준비 단계에서 오류가 발생했습니다!\n마이크 사용 허용이 되어있지 않다면 마이크 사용을 허용해주세요.");
    });
} else {
    alert("현재 브라우저가 음성 녹음을 지원하지 않습니다!\n(지원 브라우저: Chrome)");
};
