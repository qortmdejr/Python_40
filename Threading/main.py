import threading
import time


def thread_1():
    while True:
        print("쓰레드1동작");
        time.sleep(1.0);


t1 = threading.Thread(target = thread_1); # 쓰레드 설정

# 데몬쓰레드 주 스레드의 작업을 돕는 보조적인 역할을 수행하는 스레드
t1.daemon = True; # 주 스레드가 종료되면 데몬 스레드는 강제적으로 자동 종료된다.
t1.start() # 쓰레드 시작

while True:
    print("메인동작");
    time.sleep(2.0);