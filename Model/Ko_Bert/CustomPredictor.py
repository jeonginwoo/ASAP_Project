import torch.nn.functional as F

class CustomPredictor():
    def __init__(self, model, tokenizer, labels: dict, devic):
        self.model = model
        self.tokenizer = tokenizer
        self.labels = labels
        self.device = devic

    def predict(self, sentence):
        # 토큰화 처리
        tokens = self.tokenizer(
            sentence,                # 1개 문장
            return_tensors='pt',     # 텐서로 반환
            truncation=True,         # 잘라내기 적용
            padding='max_length',    # 패딩 적용
            add_special_tokens=True  # 스페셜 토큰 적용
        )
        tokens.to(self.device)
        prediction = self.model(**tokens)
        prediction = F.softmax(prediction, dim=1)
        output = prediction.argmax(dim=1).item()
        return output
        #prob, result = prediction.max(dim=1)[0].item(), self.labels[output]
        #print(f'[{result}]\n확률은: {prob*100:.3f}% 입니다.')
