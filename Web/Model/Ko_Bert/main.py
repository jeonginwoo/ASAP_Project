from transformers import BertConfig, BertTokenizer,BertModel
import torch
from Model.Ko_Bert.CustomBertModel import CustomBertModel
from Model.Ko_Bert.CustomPredictor import CustomPredictor

CHECKPOINT_NAME = 'chaimag/Bert_3'

class Ko_Bert():
    def __init__(self):
        self.device = torch.device('cpu')
        self.config = BertConfig.from_pretrained(CHECKPOINT_NAME)
        self.model_bert = BertModel.from_pretrained(CHECKPOINT_NAME).to(self.device)
        self.tokenizer = BertTokenizer.from_pretrained(CHECKPOINT_NAME)
        self.bert = CustomBertModel(CHECKPOINT_NAME).to(self.device)
        self.bert.load_state_dict(torch.load('C:/Users/joung/Visual_Studio_Code_Workspace/repos/ASAP_Project/Web/Model/Ko_Bert/bert-kor-base.pth',map_location=torch.device('cpu')))
        '''self.labels = labels = {
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
}''' 
        self.pre = CustomPredictor(self.bert, self.tokenizer, self.device)# self.labels,self.device)
        


    # 사용자 입력에 대하여 예측 후 출력을 낼 수 있는 간단한 함수를 생성합니다.
    def predict_sentence(self,pre,text):
        input_sentence = text#input('문장을 입력해 주세요: ')
        return pre.predict(input_sentence)
    
    def start(self,text):
        return self.predict_sentence(self.pre, text)

K=Ko_Bert()
K.start('할아버지가 좋아할 버거 추천해주세요')
