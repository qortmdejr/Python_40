import qrcode
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)));

file_path = 'QR_Collect.txt';

with open(file_path, 'rt', encoding="UTF8") as f:  # 파일 읽기
    read_lines = f.readlines(); # 줄 별로 리스트 형태로 반환

    for line in read_lines: # 한줄씩 읽기
        line = line.strip(); # 줄 마지막 줄바꿈문자 삭제

        qr_data = line;
        qr_img = qrcode.make(qr_data);

        qr_img.save(qr_data + ".png");

