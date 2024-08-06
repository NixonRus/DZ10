import time
from datetime import datetime
from threading import Thread

def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='UTF-8') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i}' + '\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_time = datetime.now()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

end_time = datetime.now()
total_time = end_time - start_time
print(f'Время работы функций {total_time}')
print('\n')

print('Начата запись с помощью потоков')
start_time_thr = datetime.now()

thr_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

end_time_thr = datetime.now()
total_time_thr = end_time_thr - start_time_thr
print(f'Время работы потоков {total_time_thr}')


