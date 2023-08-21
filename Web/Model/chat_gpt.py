import openai
openai.api_key = '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'
model_engine = 'text-davinci-003'
        


class GPT():
    def __init__(self):
        self.model_engine = 'text-davinci-003'
        self.prompt=''
        #self.completion# = openai.Completion.create(engine=model_engine, prompt=self.prompt, max_tokens = 100, n=1, stop=None, temperature=0.7)
        self.message=''# = self.completion.choices[0].text

    def start_gpt(self,text):#gpt에 문장 입력, 출력
        self.prompt = text
        #사용 토큰 100개로 제한
        self.completion = openai.Completion.create(engine=model_engine, prompt=self.prompt, max_tokens = 100, n=1, stop=None, temperature=0.7)
        self.message = self.completion.choices[0].text

        for i in range(len(self.message)):#원하는 답변만 이쁘게 slice하기
            if self.message[i]=='\n':
                a = i
                break
            
        for i in range(len(self.message)-1,0,-1):
            if self.message[i]=='.':
                b = i
                break
            
        c = self.message[a+2:b]
        return c