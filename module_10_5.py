import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, mode='r') as f:
        while True:
            line = f.readline().rstrip()
            all_data.append(line)
            if not line:
                break
    #print(all_data)


#0:00:12.721019 - время выполнения 4х функций в линейном режиме
# 0:00:05.055984 - время выполнения функции в многопроцессном режиме
filenames = [f'./file {number}.txt' for number in range(1, 5)]
# print(filenames)
# start_time = datetime.datetime.now()
# read_info('./file 1.txt')
# read_info('./file 2.txt')
# read_info('./file 3.txt')
# read_info('./file 4.txt')
# end_time = datetime.datetime.now()
# working_time = end_time - start_time
# print(working_time)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    working_time = end - start
    print(working_time)
