#수 - 정수형(int), 실수형(float)
#문자열(string; str; "")
#--> tip! \" 하면 문자열 내에 " 삽입 가능.
#리스트(list; [content1, content2, ...])
#딕셔너리(dict; {key1:value1, key2:value2, ...})
#튜플(tuple; (content1, content2, ...))
#불린(boolean)
#1) cmd -> python 호출
#2) IDLE 실행
#3) cmd -> ~~~.py 파일 실행
#4) Jupyter notebook 등등.
#\n은 줄 넘기기. \t는 들여쓰기.

print("hello \nwolrd")
print("hello \twolrd")

#append(element) = 맨끝에 추가.
#pop(index) = 그 자리에 있는 원소를 출력하고 리스트에서 삭제.
#insert(index, element) = 그 자리에 원소를 추가.
#reverse() = 리스트의 순서를 반대로 바꿈.

lst = [1, 2, 3, 4, 5]
lst.append(6)
print(lst)
lst.pop(-1)
print(lst)
lst.insert(3, 1)
print(lst)
lst.reverse()
print(lst)

# '#'.join(lst)

print('아래는 과제 \n')
num1 = '990101-1234567'
print(num1.split('-'))

num2 = '991212-1231237'
num2_0 = num2.split('-')[0]
print(num2_0[0:2], num2_0[2:4], num2_0[4:6])

tlist = ['Life', 'is', 'too', 'short']
a = ' '.join(tlist) + '.'
print(a)
