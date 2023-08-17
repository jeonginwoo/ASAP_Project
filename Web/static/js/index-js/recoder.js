const record = document.getElementById('record_button');
const csrfToken = document.getElementById('csrfToken').value;   //Django CSRF 토큰 값
let isRecording = false;    // 녹음 중인지 판별하는 변수

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({audio: true})  // 기기의 마이크 입력을 사용할 수 있게 설정
    .then((stream) => {
        const mediaRecorder = new MediaRecorder(stream);    // 음성 녹음을 위해 MediaRecoder에 마이크 연결

            record.onclick = () => {
                if (!isRecording) {
                    let chunks = [];

                    mediaRecorder.ondataavailable = async (event) => {
                        chunks.push(event.data);
                    };

                    mediaRecorder.onstop = (event) => {
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
                        if (data.status === 400)
                            throw Error(data.message);
                        
                        console.log(data.message);
                    })
                    .catch((err) => {
                        alert(err);
                    });
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
                }, 3000)
            }
        }
    }).catch((err) => {
        alert("음성 녹음 준비 단계에서 오류가 발생했습니다!\n마이크 사용 허용이 되어있지 않다면 마이크 사용을 허용해주세요.");
    });
} else {
    alert("현재 브라우저가 음성 녹음을 지원하지 않습니다!\n(지원 브라우저: Chrome)");
};

// if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
//     navigator.mediaDevices.getUserMedia({audio: true})  // 기기의 마이크 입력을 사용할 수 있게 설정
//     .then((stream) => {
//         const mediaRecorder = new MediaRecorder(stream);    // 음성 녹음을 위해 MediaRecoder에 마이크 연결

//         record.onclick = () => {
//             const audioContext = new (window.AudioContext || window.webkitAudioContext)();  // 오디오 컨텍스트 생성

//             audioContext.audioWorklet.addModule('static/js/index-js/vad-worklet.js')   // 기본 설정이 저장된 vad-worklet.js로 AudioWorklet을 등록시킨다.
//             .then(() => {
//                 const vadNode = new AudioWorkletNode(audioContext, 'vad-worklet');  // 오디오 worklet 노드를 생성한다.
//                 const microphoneSource = audioContext.createMediaStreamSource(stream);

//                 if (!isRecording){
//                     let chunks = [];
    
//                     mediaRecorder.ondataavailable = async (event) => {
//                         chunks.push(event.data);
//                     };
    
//                     mediaRecorder.onstop = (event) => {
//                         const recordData = new Blob(chunks, {"type": "audio/mpeg codecs=opus"});
    
//                         fetch('http://127.0.0.1:8000/main/speechrecognize/', {
//                             method: "POST",
//                             headers: {
//                                 "Content-Type": "audio/mpeg",
//                                 "X-CSRFToken": csrfToken,   //CSRF 토큰 값을 같이 헤더에 추가해 403 Fobbiden 에러 방지
//                             },
//                             body: recordData,   //녹음된 음성 데이터
//                         })
//                         .then((response) => response.json())    //response를 json으로 파싱
//                         .then((data) => {
//                             if (data.status === 400)
//                                 throw Error(data.message);
                            
//                             console.log(data.message);
//                         })
//                         .catch((err) => {
//                             alert(err);
//                         });
//                     };
    
//                     mediaRecorder.start(1000);
//                     microphoneSource.connect(vadNode);  // 음성 녹음중인지 판별하기 위해 오디오 worklet 노드에 마이크를 연결. 실시간으로 음성 데이터를 감지하고 처리한다.
//                     isRecording = true;
    
//                     record.style.background = "red";
//                     record.style.color = "black";

//                     setTimeout(() => {
//                         if (mediaRecorder.state = 'recording') {
//                             mediaRecorder.stop();
    
//                             record.style.background = "";
//                             record.style.color = "";
//                         };
    
//                         isRecording = false;
//                     }, 5000)

//                     setTimeout(() => {
//                         vadNode.port.onmessage = (event) => {   // 처리된 음성 데이터 결과를 바탕으로
//                             if (event.data.hasOwnProperty('isSpeechDetected')) {
//                                 const isSpeechDetected = event.data.isSpeechDetected;
    
//                                 if (isSpeechDetected) {
//                                     isRecording = true;
//                                 }
//                                 else {
//                                     console.log("111111111111111111111111111")
//                                     isRecording = false;
//                                     microphoneSource.disconnect();
//                                     mediaRecorder.stop();
    
//                                     record.style.background = "";
//                                     record.style.color = "";
//                                 }
//                             }
//                         };
//                     }, 1000);
//                 };
//             })
//             .catch((err) => alert(err));
//         };
//     }).catch((err) => {
//         alert("음성 녹음 준비 단계에서 오류가 발생했습니다!\n마이크 사용 허용이 되어있지 않다면 마이크 사용을 허용해주세요.");
//     });
// } else {
//     alert("현재 브라우저가 음성 녹음을 지원하지 않습니다!\n(지원 브라우저: Chrome)");
// };