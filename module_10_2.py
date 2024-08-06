from threading import Thread
import time

class Knight(Thread):
    name = True
    power = True
    enemys = 100
    def run(self):
        print(f'Сир {self.name}, на нас напали сарацины, количеством {self.enemys}!')
        time_battle = 0
        while self.enemys > 0:
            total_enemys = self.enemys - self.power
            time.sleep(1)
            time_battle += 1
            print(f'Сир {self.name} сражается {time_battle} дней..., осталось {total_enemys} сарацин.')
            if self.enemys == 0:
                print(f'Сир {self.name} одержал победу спустя {time_battle} дней(дня)! Ave Maria, Deus vult!!!')


threads = []

thread = Knight()
thread.start()
threads.append(thread)

for thread in threads:
    thread.join()

first_knight = Knight('Sir Lancelot', 10)
first_knight.run()
