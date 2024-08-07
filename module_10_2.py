from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали сарацины!')
        enemies = 100
        time_battle = 0
        while enemies > 0:
            time_battle += 1
            enemies -= self.power
            print(f'{self.name} сражается {time_battle} дней..., осталось {enemies} сарацин.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {time_battle} дней(дня)!')

if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print('Атака успешно отражена!!! Ave Maria, Deus vult!!!')