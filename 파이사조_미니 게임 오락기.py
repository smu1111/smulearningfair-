#게임 실행 부분
print("지금부터 미니게임을 시작하겠습니다.")

while True:
    print('')
    print("=" * 52)
    randomgame = int(input("어떤 게임을 선택하시겠습니까? (1: 베스킨라빈스 31 게임(다인용), 2: 배팅 게임, 3: 숫자 맞추기 게임, 0: 게임 종료): "))
    gamelist = {0: '', 1: '베스킨라빈스 31 게임', 2: '배팅 게임', 3: '숫자 맞추기 게임'}

    while randomgame > 3:
        print('')
        print("0~3사이의 값만 입력해주세요.")
        print('')
        randomgame = int(input("어떤 게임을 선택하시겠습니까? (1: 베스킨라빈스 31 게임(다인용), 2: 배팅 게임, 3: 숫자 맞추기 게임, 0: 게임 종료)"))

    print('')
    print(gamelist[randomgame],'을 시작하겠습니다.')
    print("=" * 52)
    print('')

    #게임 종료
    if randomgame == 0:
        print('게임이 종료되었습니다.')
        break


    #베스킨라빈스 31게임 (다인용)
    elif randomgame == 1:
        
        print("다인용 버전 베스킨라빈스 31게임에 오신 것을 환영합니다. \n참가자들은 숫자를 1개 이상 3개 이하로 부를 수 있습니다.")
        print("1부터 31까지의 수를 순차적으로 부르세요. 31을 외치는 사람이 게임에서 집니다.")
        print("=" * 52)
        
        BRpeoplelist = [ ]
        people = int(input("참가자의 수를 입력하세요.(숫자로 입력하세요.): "))

        while people == 1:
            print("다인용 게임입니다. 2 이상 선택해주세요. ")
            people = int(input("참가자의 수를 입력하세요.(숫자로 입력하세요.): "))
            
        for _ in range(1, people+1, 1):
            BRpeoplelist.append(input("참가자의 닉네임을 순서대로 입력하세요.: "))


        게임수 = 0
        while True:   
            for 인원수 in range(people):
                print(BRpeoplelist[인원수], "님,", end='')
                입력값 = int(input(" 숫자 몇 개를 부를 건가요? (1~3) : "))
                
                while 입력값 == 0 or 입력값>3 :
                    print('1~3 사이의 값만 입력하세요.')
                    print(BRpeoplelist[인원수], "님,", end='')
                    입력값 = int(input(" 숫자 몇 개를 부를 건가요? (1~3) : "))
                

                for 숫자 in range(입력값):
                    if 게임수 + 1 + 숫자 <= 31 :
                        print('{}!'.format(게임수 + 1 + 숫자))

                    if 게임수 + 1 + 숫자 == 31 :
                        print ("벌칙에 당첨되었습니다!")
                        break
                            
                게임수 += 입력값

                if 게임수 >= 31 :
                    break
                

            if 게임수 >= 31 :
                break
                                              

        print ('')


    #배팅 게임
    elif randomgame == 2:
        
        import random
        print("배팅 게임에 오신 것을 환영합니다.")
        print("한 레벨을 통과하실 때마다 배팅 금액의 2배를 상금으로 받으실 수 있습니다.")
        print("레벨 통과에 실패하시면 모든 배팅 금액을 잃게 됩니다.")
        print("세 갈래의 길 중 상금이 놓인 길은 단 한 곳입니다.")
        print("=" * 52)
        print()

        bet = int(input("배팅 금액을 입력하세요. (단위 : 원) >>>  "))
        print("총", bet, "원 배팅하셨습니다.")
        level = 1


        while True:
            winning_num = random.randint(1,3)
            print('')
            print(level, "단계 입니다.")
            user_choice = int(input("세 갈래의 길로 나뉘어 있습니다. 어느 길을 선택하시겠습니까? 1,2,3 >>>  "))

            while user_choice < 1 or user_choice > 3:
                print(user_choice, '는 존재하지 않는 길입니다. 1~3번 길 중에서 선택해주세요.')
                print('')
                user_choice = int(input("세 갈래의 길로 나뉘어 있습니다. 어느 길을 선택하시겠습니까? 1,2,3 >>>  "))

            if user_choice == winning_num:
                bet = bet * 2
                print("축하합니다! 2배 획득!! 총 금액은", bet, "원이 되었습니다.")
                next = input("다음 단계로 이동하시겠습니까? 성공시 2배, 실패시 0원. y or n >>> ")
                if next == 'y':
                    level = level + 1           

                else:
                    print("게임을 종료하겠습니다. 얻으신 금액은 총", bet, "원 입니다.")
                    print('')
                    break

            else:
                print("게임이 종료되었습니다. 아쉽지만 배팅하신 금액을 모두 잃었습니다.")
                print("상금은", winning_num, "번 길에 있었습니다.")
                print('')
                break


    #숫자 맞추기 게임
    elif randomgame == 3:
        
        print("숫자 맞추기 게임에 오신 것을 환영합니다.")
        print("맞출 숫자는 1부터 100 사이의 숫자입니다.")
        print("기회는 총 5번입니다.")
        print("")

        import random
        number = random.randint(1,100)
        기회 = 5

        while 기회!=0:       
            guess = int(input("숫자를 입력하세요: "))


            while guess > 100 or guess < 1:
                print("1-100중의 숫자를 입력하세요.")
                guess = int(input("숫자를 입력하세요: "))
                print('')

            
            if guess == number: 
                print("축하합니다. 정답입니다!")
                break
            elif guess > number:
                print("더 작은 수 입니다.")
            else:
                print("더 큰 수 입니다.")

            기회 = 기회 - 1
            print ('남은 기회는', 기회, '번 입니다.')
            print ('')

        if 기회 == 0:
            print("game over")
            print("정답은", number, "입니다.")

        print ('')

        
                
