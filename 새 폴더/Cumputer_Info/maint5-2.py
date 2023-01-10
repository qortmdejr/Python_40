import psutil

#CPU 속도 측정
cpu = psutil.cpu_freq();
cpu_current_ghz = round(cpu.current / 1000, 2);
print(f"cpu 속도 : {cpu_current_ghz}GHz");

#CPU 물리코어 수 측정
cpu_cores = psutil.cpu_count(logical=False);
print(f"코어 수: {cpu_cores}");

#메모리 크기 측정
memory = psutil.virtual_memory();
memory_total = round(memory.total / 1024 **3);
print(f"메모리 : {memory_total}GB");

#디스크 크기 출력(디스크 수 만큼)
disk = psutil.disk_partitions();
for p in disk:
    print(p.mountpoint, p.fstype, end = ' ');
    du = psutil.disk_usage(p.mountpoint);
    disk_total = round(du.total / 1024**3);
    print(f"디스크 크기: {disk_total}GB");

#네트워크를 통해 보내고 받은 데이터 크기 측정(누적 데이터값)
net = psutil.net_io_counters();
sent = round(net.bytes_sent/1024 ** 2, 1);
recv = round(net.bytes_recv/1024 **2, 1);
print(f"보내기 : {sent}MB 받기 : {recv}MB");

