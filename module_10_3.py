from random import randint
import time
from threading import Thread, Lock


class Bank:
    balance = 0
    lock = Lock()

    def __init__(self, lock=True):
        super().__init__()

    def deposit(self):
        global balance
        for i in range(10):
            a = randint(50, 500)
            balance += a
            if balance >= 500 and lock.locked():
                lock.release()
        print(f"Пополнение: {a}. Баланс: {balance}")
        time.sleep(0.001)

    def take(self):
        global balance
        for j in range(10):
            b = randint(50, 500)
            print(f'Запрос на {b}')
            if b <= balance:
                balance -= b
                print(f"Снятие: {b}. Баланс: {balance}")
            elif b > balance:
                print("Запрос отклонён, недостаточно средств")
                lock.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
