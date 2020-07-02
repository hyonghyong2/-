##print(round(2.345,2))
##while True:
##    print('Who are you?')
##    name=input(':')
##    if name!='joe':
##        continue
##    print('Hello, joe. What is the password? (It is a fish.)')
##    password=input(':')
##    if password=='swordfish':
##        break
##print('Access granted')

##name=''
##while not name:
##    print('Enter your name: ')
##    name=input()
##print('How many guest will you have?')
##num_guests=int(input(':'))
##if num_guests:
##    print('Be sure to have enough room for all your guests.')
##print('Done')

#80p
#Q9.
##spam=[3,6,7]
##if spam==1:
##    print('Hello')
##elif spam==2:
##    print('Howdy')
##else:
##    print('Greetings!')

#Q11.
#break: 실행을 바깥쪽, 루프 다음으로 옮김(while문 밖으로)
#continue: 실행을 루프의 시작 지점으로 옮김(while문 안으로)

#Q13.
##for i in range(1,11):
##    print(i)
##
##i=1
##while i<=10:
##    print(i)
##    i+=1

#Q14.
##import spam
##spam.bacon()

#100p
#연습 프로젝트#콜라츠 수열 만들기
##def collatz(number):
##    if number%2==0:
##        result=number//2
##        return result
##    else:
##        result=(number*3)+1
##        return result
##
##while True:
##    try:
##        number=int(input("콜라츠 수열에 넣을 숫자를 적어주세요.: "))
##        while number!=1:
##            number=collatz(number)
##            print(number)
##        break
##    except ValueError:
##        print('ValueError입니다. 정수를 입력해주세요.')

##p.129
##spam=['apples','bananas','tofu','cats']
##animal=['cat','goat','dog','horse']
##def edit_list(list):
##    for i in range(0,len(list)-1):
##        print(str(list[i]),end=',')
##    print(str(list[i+1]))
##edit_list(animal)

#p.147
Inventory={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
# def displayInventory(Inventory):
#     print("Inventory:")
#     totalNum=0
#     for tools,num in Inventory.items():
#         print(str(num)+" "+tools)
#         totalNum+=num
#     print("Total number of items:"+str(totalNum))
# displayInventory(Inventory)

#p.149미완성본
# dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby']
# def addTolinventory(inventory,addedItems):
#     dragonLoot_Dic={}
#     for addedItems in dragonLoot:
#         dragonLoot_Dic[addedItems]=0
#     for inventory in dragonLoot:
#         dragonLoot[inventory]=dragonLoot[inventory]+1
#     print(dragonLoot_Dic)
# addTolinventory(inventory,addedItems)

#참고: list -> dic변환 코드
# list_example = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'a', 'b', 'a']
# remove_overlap = list(set(list_example))
# dic = {}
# for list_name in remove_overlap:
#     dic[list_name] = 0
# for list_count in list_example:
#     dic[list_count] = dic[list_count] + 1
# print(dic)
