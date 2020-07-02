##my_name=input()
##print("It's good to meet you"+" "+my_name+".")
##print(len('hello'))
##print('I am '+str(29)+' years old.')
##print("What is your age?")
##my_age=input("Please write down your age.: ") #input의 결과값은 항상 str
##print("You will be "+str(int(my_age)+1)+" in a year.")
##print('My name is ')
##for i in range(5):
##    print('Jimmy Five Times ('+str(i)+')')

##result=0
##for i in range(1,101):
##    result=result+i
##print(result)

##result=0
##i=0
##while i<=100:
##    result=result+i
##    i+=1
##print(result)

#76p
##print('My name is')
##i=1
##while 1<=i<=5:
##    print('Jimmy Five Times ('+str(i)+')')
##    i+=1

##79p
##import sys
##
##while True:
##    print('Type exit to exit.')
##    response=input(':')
##    if response=='exit':
##        sys.exit()
##    print('You typed '+response+'.')

#85
##import random
##def getAnswer(answerNumber):
##    if answerNumber==1:
##        return 'It is certain'
##    elif answerNumber==2:
##        return 'It is decidedly so'
##    elif answerNumber==3:
##        return 'yes'
##    else:
##        return "I'm sorry"
####r=random.randint(1,9)
####print(r)
####fortune=getAnswer(r)
####print(fortune)
###위 세줄을 한줄로 줄이면
##print(getAnswer(random.randint(1,9)))

#88p
##print('cats','dogs','mice',sep=',')

#96 6번 질문 안에 숫자 맞추기
##print("I'm thinking of a number between 1 and 20.")
##import random
##secretNumber=random.randint(1,20)
##guessTimes=0
##while guessTimes<=6:
##    guessTimes+=1
##    print("Take a guess.")
##    guessNumber=int(input(':'))
##    if secretNumber<guessNumber:
##        print("Your guess is too high.")
##    elif secretNumber>guessNumber:
##        print("Your guess is too low.")
##    else:
##        break
##
##if secretNumber==guessNumber:
##    print("Good job! You guessed my number in {} guesses!".format(guessTimes))
##else:
##    print("Nope. The number I was thinking of was {}".format(str(secretNumber)))

#p.109
##catnames=[]
##while True:
##    print("Enter the name of cat"+str(len(catnames)+1)+" (Or nothing to stop.):")
##    name=input()
##    if name=='':
##        break
##    catnames=catnames+[name]
##print('The cat names are: ')
##for name in catnames:
##    print(''+name)

##supplies=['pens','staplers','flame-throwers','binders']
##for i in range(len(supplies)):
##    print("Index"+str(i)+" in supplies is: "+supplies[i])

#p.112
##my_pets=['Zophie','Pooka','Fat-tail']
##print('Enter a pet name: ')
##name=input()
##if name not in my_pets:
##    print("I don't have a pet named "+name)
##else:
##    print(name+" is my pet.")

#p.115
##spam=['cat','dog','bat']
##spam.insert(1,'chicken')
##print(spam)

#117. sort()는 호출한 리스트 자체를 정렬
#따라서 spam.sort()면 됨. spam=spam.sort() 반환값 저장 필요 없음.

#118
##import random
##messages=['good','better','best','bad','worse','worst']
##print(messages[random.randint(0,len(messages)-1)])

##messages=['good','better','best','bad','worse','worst']
##messages=tuple(messages)
##print(type(messages))

#p.134
# spam={'color':'red','age':42}
# print(spam.keys())
# print(list(spam.keys()))

# spam={'color':'red','age':42}
# for k,v in spam.items():
#     print('Key:'+k+' Value:'+str(v))

#p.135
# picnicItems={'apples':5, 'cups':2}
# print('I am bringing '+str(picnicItems.get('cups',0))+' cups.')

#p.136 setdefault(): key값이 존재하지 않을 경우 키 값 설정할 때 사용
#(key값이 이미 있는 경우는 변경되지 않음을 주의!)
# spam={'name':'Pooka','age':5}
# spam.setdefault('color','black')
# print(spam)
# spam.setdefault('color','white')
# print(spam)

#p.142
# theBoard={'top-L':'O','top-M':'O','top-R':'O','mid-L':'X','mid-M':'X','mid-R':' ','low-L':' ','low-M':' ','low-R':'X'}
# def printBoard(board):
#     print(board['top-L']+'l'+board['top-M']+'l'+board['top-R'])
#     print('-+-+-')
#     print(board['mid-L']+'l'+board['mid-M']+'l'+board['mid-R'])
#     print('-+-+-')
#     print(board['low-L']+'l'+board['low-M']+'l'+board['low-R'])
# printBoard(theBoard)

#p.145
# allGuests={'Alice':{'apples':5,'pretzels':12},'Bob':{'ham sandwiches':3,'apples':2},'Carol':{'cups':3,'apple pies':1}}
# def totalBrought(guests,item):
#     numBrought=0
#     for k,v in guests.items():
#         numBrought=numBrought+v.get(item,0)
#     return numBrought
# print('Number of things being brought:')
# print('-Apples '+str(totalBrought(allGuests,'apples')))
# print('-Cups '+str(totalBrought(allGuests,'cups')))
# print('-Cakes '+str(totalBrought(allGuests,'cakes')))
# print('-Ham sandwiches '+str(totalBrought(allGuests,'ham sandwiches')))
# print('-Apple pies '+str(totalBrought(allGuests,'apple pies')))
