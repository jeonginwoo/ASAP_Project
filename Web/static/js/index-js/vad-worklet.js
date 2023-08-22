class VADWorkletProcessor extends AudioWorkletProcessor {
    constructor() {
        super();

        this.threshold = 0.000001;   // 감지 임계값 설정
        this.isSpeechDetected = false;    // 음성 감지 여부 초기화 설정
    }

    process(inputs, outputs, params) {  // 실시간으로 음성 데이터를 받아 처리함
        const input = inputs[0];
        const channelData = input[0];

        const inputEnergy = this.calculateInputEnergy(channelData); // 음성의 에너지를 계산하는 부분

        console.log(inputEnergy);

        if (inputEnergy <= this.threshold) {    // 음성 감지 안됨
            this.isSpeechDetected = false;
        }
        else {  // 음성 감지됨
            this.isSpeechDetected = true;
        }

        this.port.postMessage({ isSpeechDetected: this.isSpeechDetected});  // 처리 결과를 메인 스크립트로 보냄

        return true;
    }

    calculateInputEnergy(channelData) {
        const squaredSum = channelData.reduce((sum, sample) => sum + sample * sample, 0);
        const energy = squaredSum / channelData.length;

        return energy;
    }
}

registerProcessor('vad-worklet', VADWorkletProcessor);