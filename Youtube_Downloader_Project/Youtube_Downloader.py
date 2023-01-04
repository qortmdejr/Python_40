# Youtube Downloader Project
from tkinter import *
from tkinter import messagebox # 다운로드 완료 알림창 메세지박스
from pytube import YouTube # 유뷰브 다운로드 모듈
import os # 윈도우 운영체제 명령어
import shutil # 파일 이동을 위한 라이브러리

import time #시간측정
start = time.time()  # 시작 시간 저장

#다운로더 함수정의
def youtube_download(url):
    Save_Folder = './Download_Folder';
    if not os.path.exists(Save_Folder): # 파일존재 안할시 파일 생성
        os.mkdir(Save_Folder) # mkdir =>  파일 생성
    else:
        pass

    global yt; # 전역변수 선언
    yt = YouTube(url);  # 객체 생성

    print("제목 : ", yt.title)
    print("길이 : ", yt.length)

    Video = yt.streams.get_highest_resolution().download(Save_Folder); # 좋은 퀄리티로 영상 다운

    print(f"---------다운로드 완료---------"); # print(f 서식화된 출력지원)

    global Move_Folder; #전역변수 선언
    windows_user_name = os.path.expanduser('~'); # C:\User\계정ID 경로
    Move_Folder = f'{windows_user_name}\Desktop\Save_Folder' # 파일 이동 경로

    try:
        if not os.path.exists(Move_Folder): # 바탕화면에 폴더 존재 안할시
            os.mkdir(Move_Folder) # 바탕화면에 Download_Folder 폴더 생성
    except:
        print("Failed to create Folder");


    filename = yt.title + '.mp4';
    src = r'.\Download_Folder/' # 'r'은 문자열 가공X (추가 안할시 unicode Error 발생)
    dir = f'{windows_user_name}\Desktop\Save_Folder/'
    shutil.move(src + filename, dir + filename); #Download_Folder로 파일 이동을 위한 shutil 함수
    messagebox.showinfo("알림","   다운로드 완료   ");
    print("time :", time.time() - start) # 시간측정
    os.startfile(f'{dir}');



def Extension_Change(File): # 확장자 mp3 변경 함수
    path = Move_Folder + '/'
    try:
        os.rename(path + File + '.mp4', path + File + '.mp3');
    except:
        print("확장자 변경 오류!");

#main
root = Tk()
root.title("Youtube_Downloader")
root.geometry('480x240')
root.resizable(False,False); #창크기 조절 x

#라벨 제목
lb_title = Label(root, text = "Youtube 다운로더",width = 20);
lb_title.config(font = ("",18,"bold"));
lb_title.grid(row = 0, column = 0);

#링크 삽입 라벨
input_link = Entry(root,width = 50,textvariable = StringVar()); #문자열 변환 함수
input_link.insert(0,"여기에 링크를 입력하세요"); # placehoolder
input_link.grid(row = 1, column = 0, pady= 10, padx = 5);


#유트브 버튼 클릭시 영상 다운이벤트
def button_Click(event):
    ent = input_link.get();
    youtube_download(ent);

#다운로드 버튼 & 이벤트
Bt = Button(root, text = "다운로드");
Bt.bind("<Button-1>", button_Click); # 버튼클릭시 다운로드 함수실행
Bt.grid(row = 1, column = 1, padx= 15);

root.mainloop();

