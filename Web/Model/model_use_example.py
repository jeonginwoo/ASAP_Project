from Leven import Leven
from chat_gpt import GPT


#Leven 사용 예시
text = '이날이우스 아퍼 주세요'
L = Leven(text)
result = L.start_leven()
print(result)

#gpt 사용 예시
gpt = GPT()
text = '주차장이 어디야'
result = gpt.start_gpt(text)
print(result)
