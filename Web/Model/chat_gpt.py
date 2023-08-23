# import openai
# openai.api_key = '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'

# import asyncio

# class GPT():
     
#     # def __init__(self):
#     #     self.model_engine = 'text-davinci-003'
#     #     self.prompt=''
#     #     #self.completion# = openai.Completion.create(engine=model_engine, prompt=self.prompt, max_tokens = 100, n=1, stop=None, temperature=0.7)
#     #     self.message=''# = self.completion.choices[0].text
#     #     print('*******************')
#     #     print('*******************')
#     #     print('GPT가 실행되었습니다')
#     #     print('*******************')
#     #     print('*******************')

#     # def start_gpt(self,text):#gpt에 문장 입력, 출력
#     #     self.prompt = text
#     #     #사용 토큰 100개로 제한
#     #     self.completion = openai.Completion.create(engine=model_engine, prompt=self.prompt, max_tokens = 100, n=1, stop=None, temperature=0.7)
#     #     self.message = self.completion.choices[0].text

#     #     for i in range(len(self.message)):#원하는 답변만 이쁘게 slice하기
#     #         if self.message[i]=='\n':
#     #             a = i
#     #             break
            
#     #     for i in range(len(self.message)-1,0,-1):
#     #         if self.message[i]=='.':
#     #             b = i
#     #             break
            
#     #     c = self.message[a+2:b]
#     #     return c

#     def __init__(self):
#         self.model_engine = 'gpt-3.5-turbo'
#         self.content=''
#         #self.completion# = openai.Completion.create(engine=model_engine, prompt=self.prompt, max_tokens = 100, n=1, stop=None, temperature=0.7)
#         self.messages=[]# = self.completion.choices[0].text
#         self.start_gpt_3_5('몇가지 정보를 알려줄테니까 잘 기억해줘')
#         self.start_gpt_3_5('앞으로 화장실 위치 물어보면 "매장 건물 1층에 있습니다." 라고 해줘')
#         self.start_gpt_3_5('앞으로 빨대 위치 물어보면 "카운터 좌측에 준비되어있습니다." 라고 해줘')
#         self.start_gpt_3_5('와이파이 비밀번호를 물어보면 "와이파이 비밀번호는 : 데청캠1234" 라고해줘')
#         self.start_gpt_3_5('음료 리필 여부를 물어보면 "버거킹에서는 음료리필이 불가능 합니다." 라고 해줘')
#         self.start_gpt_3_5('여기까지 알려준거고 위와 같은 정보를 물어보면 알맞게 대답해줘')
#         print('나는 쥐피티 INIT 입니다!!!!!!')
    
#     def start_gpt_3_5(self,text):
#         self.content = text
#         self.messages.append({"role": "user", "content": self.content})
#         # self.completion = openai.Completion.create(engine = model_engine, prompt = self.prompt , max_tokens = 100, n = 1 ,stop = None, temperature = 0.7)
#         self.completion = openai.ChatCompletion.create(model = self.model_engine,  messages = self.messages , max_tokens = 60)
#         self.chat_response = self.completion.choices[0].message.content

#         c = self.chat_response
#         return c
        
# # class GPT():
# #     def __init__(self):
# #         self.model_engine = 'gpt-3.5-turbo'
# #         self.prompt = ''
# #         self.message = ''
# #         print('나는 쥐피티 INIT 입니다!!!!!!')
    
# #     async def start_gpt_3_5(self, text):
# #         self.prompt = text
        
# #         if self.message:
# #             self.prompt = self.message + "\n" + self.prompt
        
# #         self.completion = openai.Completion.create(engine=self.model_engine, prompt=self.prompt, max_tokens=60, n=1, stop=None, temperature=0.7)
# #         self.message = self.completion.choices[0].text
        
# #         a = self.message.rfind('\n') + 1
# #         b = self.message.rfind('.')
# #         c = self.message[a:b].strip()
        
# #         return c

# # async def main():
# #     gpt_instance = GPT()

# #     while True:
# #         user_input = input("사용자: ")
        
# #         if user_input.lower() == 'exit':
# #             break
        
# #         gpt_response = await gpt_instance.start_gpt_3_5(user_input)
# #         print("쥐피티:", gpt_response)

# # if __name__ == '__main__':
# #     asyncio.run(main())