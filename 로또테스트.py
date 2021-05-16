import random
import time

for try_num in range(30):
    while True:
        print("----------------------------------------------------")
        check_nums = True
        
        lotto_guess = input("번호 5개를 입력하시오 : ")
        lotto_guess = lotto_guess.split()

        if lotto_guess == []:
            print("아무것도 입력하지 않았습니다.")
            continue
        
        if len(lotto_guess) != 5:
            print("입력된 숫자 개수가 5개가 아닙니다.")
            continue

        
        for i in range(len(lotto_guess)):
            try:
                lotto_guess[i] = int(lotto_guess[i])
            except:
                print(lotto_guess[i], "잘못된 수를 입력하였습니다.")
                check_nums = False
                continue
            
            if lotto_guess[i] < 1 or lotto_guess[i] > 45:
                print(lotto_guess[i], "로또 번호는 1~45 사이입니다.")
                check_nums = False
                continue
            
            if lotto_guess.count(lotto_guess[i]) != 1:
                check_nums = False
                print(lotto_guess[i], "중복으로 입력된 수 입니다.")                                

        if check_nums == True:
            #print("로또 번호 5개를 올바르게 입력하였습니다.")
            lotto_guess.sort()
            break

    lotto_nums = []
    cnt = 0
    print("로또번호 추점...")
    while cnt < 5:
        gen_num = random.randint(1, 45)
        if gen_num in lotto_nums:
            continue
        else:
            time.sleep(1)
            lotto_nums.append(gen_num)
            cnt = cnt + 1
            print(gen_num)
            
    lotto_nums.sort()
    print("로또번호 : ", lotto_nums)

    print("결과는....")
    time.sleep(0.5)
    correct_nums = []
    for i in range(5):
        if lotto_guess[i] in lotto_nums:
            correct_nums.append(lotto_guess[i])
            
    print(f"총 {len(correct_nums)}개 맞추었습니다!!")
    print(correct_nums) 
