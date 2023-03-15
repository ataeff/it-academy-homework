"""
Создайте приложение из 100 потоков типа сетевой запрос/ответ, 50 запросов и 50 ответов. 
Ну чтобы ответы не перекрывали запросы примените переключатель СЕМАФОР и опционально LOCK. 
Число потоков оформите через range.
шаблон в папе 11
"""""
# Atayev Akmuhammet
# Lab 11.1

import threading
import time
from tkinter import *
from tkinter import ttk


# Tkinter


class Semaphore:

    def __init__(self, master):
        master.title('Семафор')
        master.geometry('600x400')
        master.resizable(False, False)

        # Задаем число семафор (по умолчанию 5)
        self.var_sem = IntVar()
        Label(master, text="Semaphore:", font=("Arial Bold", 12)).grid(column=0, row=0, pady=20)
        Entry(master, width=10, textvariable=self.var_sem).grid(column=1, row=0, pady=20)

        # Задаем число thread (по умолчанию 50)
        self.var_thr = IntVar()
        Label(master, text="Threads:", font=("Arial Bold", 12)).grid(column=0, row=2, pady=20)
        Entry(master, width=10, textvariable=self.var_thr).grid(column=1, row=2, pady=20)

        # Задаем число time.sleep (по умолчанию 1с)
        self.var_sleep = IntVar()
        Label(master, text="Time.Sleep:", font=("Arial Bold", 12)).grid(column=0, row=4, pady=20)
        Entry(master, width=10, textvariable=self.var_sleep).grid(column=1, row=4, pady=20)

        # label Output
        Label(master, text='OutPut:').grid(column=2, row=0, padx=100)

        self.lbl_in = Label(master, text='asd')  # Output Запросы
        self.lbl_out = Label(master, text='out')  # Output Ответы

        # кнопка
        self.btn = ttk.Button(master, text="Enter", command=self.work)
        self.btn.grid(column=0, row=6, ipadx=10, ipady=5, pady=20)

        # grids (для Запросов и ответов)
        self.lbl_in.grid(column=3, row=0)
        self.lbl_out.grid(column=3, row=1)

        # semaphore and lock
        self.lock = threading.Lock()


    # METHODS
    # функция запроса
    # запросы должны появляться на lbl_in
    def makeActive(self, name):
        with self.lock:
            self.lbl_in["text"] = name

    # функция ответа
    # запросы должны появляться на lbl_out и переименовать lbl_in (удалить запросов написанное в lbl_in)
    def makeInactive(self, name):
        with self.lock:
            self.lbl_in["text"] = "NONE"
            self.lbl_out["text"] = name

    # Главная функция. Семафор
    def worker(self):
        sem = threading.Semaphore(self.var_sem.get())
        with sem:
            th_name = threading.current_thread().name
            self.makeActive(th_name)
            time.sleep(self.var_sleep.get())
            self.makeInactive(th_name)



    # функция threads
    def work(self):
        # for _ in range(self.var_thr.get()):
        #     threading.Thread(target=self.worker).start()
        name = 'hello'
        my = []
        for i in name:
            time.sleep(3)
            my.append(i)
        self.lbl_out["text"] = my



if __name__ == "__main__":
    root = Tk()
    obj = Semaphore(root)
    root.mainloop()

