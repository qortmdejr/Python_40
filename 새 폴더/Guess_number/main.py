from random import *

random_number = randint(1,100);
game_count = 1;

while True:
    try:
        mynumber = int(input("1~100 사이의 숫자를 입력하세요 : "));

        if mynumber == random_number:
            print(f"축하합니다.{game_count}회 만에 맞췄습니다.");
            break;

        elif mynumber > random_number:
            print("다운");
        elif mynumber < random_number:
            print("업");

        game_count = game_count + 1;
    except:
        print("에러가 발생했습니다. 다시 입력해주세요.");


