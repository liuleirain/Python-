import time

def core_loop():
    limit = 10 ** 8
    while limit > 0:
        limit -= 1

def other_loop1():
    time.sleep(0.2)

def other_loop2():
    time.sleep(0.4)

def main():
    start_time = time.localtime()
    print('程序开始时间：',time.strftime('%Y-%m-%d %H:%M:%S', start_time))
    start_perf_counter = time.perf_counter()
    other_loop1()
    other_loop1_perf_counter = time.perf_counter()
    other_loop1_perf = other_loop1_perf_counter - start_perf_counter
    core_loop()
    core_loop_perf_counter = time.perf_counter()
    core_loop_perf = core_loop_perf_counter - other_loop1_perf_counter
    other_loop2()
    other_loop2_perf_counter = time.perf_counter()
    other_loop2_perf = other_loop2_perf_counter - core_loop_perf_counter
    end_perf_counter = time.perf_counter()
    total_perf = end_perf_counter - start_perf_counter
    endtime = time.localtime()
    print('模块1运行时间是：{}秒'.format(other_loop1_perf))
    print('核心模块运行时间是：{}秒'.format(core_loop_perf))
    print('模块2运行时间是：{}秒'.format(other_loop2_perf))
    print('程序运行总时间是：{}秒'.format(total_perf))
    print('程序结束时间：',time.strftime('%Y-%m-%d %H:%M:%S', endtime))

if __name__ == '__main__':
    main()
