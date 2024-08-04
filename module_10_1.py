import time
from datetime import datetime


def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='UTF-8') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i}' + '\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_time = datetime.now()

print(wite_words(10, 'example1.txt'))

end_time = datetime.now()
total_time = end_time - start_time
print(total_time)
