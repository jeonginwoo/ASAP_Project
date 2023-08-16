from transformers import BertConfig, BertTokenizer,BertModel
import torch
from CustomBertModel import CustomBertModel
from CustomPredictor import CustomPredictor

CHECKPOINT_NAME = 'chaimag/Bert_3'

device = torch.device('cpu')

config = BertConfig.from_pretrained(CHECKPOINT_NAME)
model_bert = BertModel.from_pretrained(CHECKPOINT_NAME).to(device)
tokenizer = BertTokenizer.from_pretrained(CHECKPOINT_NAME)

bert = CustomBertModel(CHECKPOINT_NAME).to(device)
bert.load_state_dict(torch.load('C:/Users/tkdal/Desktop/바트/bert-kor-base.pth',map_location=torch.device('cpu')))

labels = {
    0: '추천 입니다',
    1: '남성 입니다',
    2 : '여성 입니다',
    3 : '젊은남성 입니다',
    4 : '젊은여성 입니다',
    5 : '노인남성 입니다',
    6 : '노인여성 입니다',
    7 : '젊은이 입니다',
    8 : '어르신 입니다',
    9 : '여름이었다',
    10 : '겨울입니다',
    11 : '기타'
}

# CustomPredictor 인스턴스를 생성합니다.
predictor = CustomPredictor(bert, tokenizer, labels,device)

# 사용자 입력에 대하여 예측 후 출력을 낼 수 있는 간단한 함수를 생성합니다.
def predict_sentence(predictor):
    input_sentence = input('문장을 입력해 주세요: ')
    predictor.predict(input_sentence)
predict_sentence(predictor)