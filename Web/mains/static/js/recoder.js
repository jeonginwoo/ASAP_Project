const record = document.getElementById('record_button');
const audio = document.getElementById('audioPlayer');
const csrfToken = document.getElementById('csrfToken').value;   //Django CSRF 토큰 값
let isRecording = false;

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({audio: true})
    .then((stream) => {
        const mediaRecorder = new MediaRecorder(stream);

        record.onclick = () => {
            if (!isRecording){
                let chunks = [];

                mediaRecorder.ondataavailable = async (event) => {
                    chunks.push(event.data);
                };

                mediaRecorder.onstop = (event) => {
                    // chunks.forEach(async (data) => {
                    //     // console.log(data);
                    //     let temp = await data.text();
                    //     console.log(temp);
                    // });

                    fetch('http://127.0.0.1:8000/speechrecognize/', {
                        method: "POST",
                        headers: {
                            "Content-Type": "audio/mpeg",
                            "X-CSRFToken": csrfToken,   //CSRF 토큰 값을 같이 헤더에 추가해 403 Fobbiden 에러 방지
                        },
                        body: recordData,   //녹음된 음성 데이터
                    })
                    .then((response) => response.json())    //response를 json으로 파싱
                    .then((data) => {
                        console.log(data.message);
                    })
                    .catch((err) => {
                        location.href = err;
                    });

                    chunks.splice(0);

                    const recordURL = window.URL.createObjectURL(recordData);

                    audio.src = recordURL;
                    audio.play();
                };

                mediaRecorder.start(1000);
                isRecording = true;

                record.style.background = "red";
                record.style.color = "black";

                setTimeout(() => {
                    if (mediaRecorder.state = 'recording') {
                        mediaRecorder.stop();

                        record.style.background = "";
                        record.style.color = "";
                    };

                    isRecording = false;
                }, 8000)
            };
        };
    }).catch((err) => {
        alert("음성 녹음 준비 단계에서 오류가 발생했습니다!\n마이크 사용 허용이 되어있지 않다면 마이크 사용을 허용해주세요.");
    });
} else {
    alert("현재 브라우저가 음성 녹음을 지원하지 않습니다!\n(지원 브라우저: Chrome)");
};