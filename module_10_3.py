from random import randint
import time
from threading import Thread, Lock


class Bank:
    balance = 0
    lock = Lock()

    def __init__(self):
        super().__init__()

    def deposit(self):
        for i in range(10):
            a = randint(50, 500)
            Bank.balance += a
            if Bank.balance >= 500 and self.lock.locked():
                self.lock.release()
        print(f"Пополнение: {a}. Баланс: {Bank.balance}")
        time.sleep(0.001)

    def take(self):
        for j in range(10):
            b = randint(50, 500)
            print(f'Запрос на {b}')
            if b <= Bank.balance:
                Bank.balance -= b
                print(f"Снятие: {b}. Баланс: {Bank.balance}")
            elif b > Bank.balance:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
