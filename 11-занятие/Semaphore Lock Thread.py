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
root = Tk()
root.title('Семафор')
root.geometry('600x400')

# Задаем число семафор (по умолчанию 5)
var_sem = IntVar(root, value=5)
lbl_semaphore = Label(root, text="Semaphore:", font=("Arial Bold", 12))
lbl_semaphore.grid(column=0, row=0, pady=20)
txt_semaphore = Entry(root, width=10, textvariable=var_sem)
txt_semaphore.grid(column=1, row=0, pady=20)

# Задаем число thread (по умолчанию 50)
var_thr = IntVar(root, value=50)
lbl_thread = Label(root, text="Threads:", font=("Arial Bold", 12))
lbl_thread.grid(column=0, row=2, pady=20)
txt_thread = Entry(root, width=10, textvariable=var_thr)      #
txt_thread.grid(column=1, row=2, pady=20)

# Задаем число time.sleep (по умолчанию 1с)
var_sleep = IntVar(root, value=1)
lbl_sleep = Label(root, text="Time.Sleep:", font=("Arial Bold", 12))
lbl_sleep.grid(column=0, row=4, pady=20)
txt_sleep = Entry(root, width=10, textvariable=var_sleep)
txt_sleep.grid(column=1, row=4, pady=20)


# логика
# =======================================================
# определяем семафор и lock
sem = threading.Semaphore(var_sem.get())
lock = threading.Lock()

# функция запроса
# запросы должны появляться на lbl_in
def makeActive(name):
    global lock, lbl_in
    with lock:
        lbl_in["text"] = name

# функция ответа
# запросы должны появляться на lbl_out и переименовать lbl_in (удалить запросов написанное в lbl_in)
def makeInactive(name):
    global lock, lbl_in, lbl_out
    with lock:
        lbl_in["text"] = "NONE"
        lbl_out["text"] = name


# Главная функция. Семафор
def worker():
    global sem, lock
    with sem:
        th_name = threading.current_thread().name
        makeActive(th_name)
        time.sleep(var_sleep.get())
        makeInactive(th_name)

# функция threads
def work():
    for _ in range(var_thr.get()):
        threading.Thread(target=worker()).start()

# ==============================================================

# продолжение Tkinter
# кнопка
btn = ttk.Button(root, text="Enter", command=work())
btn.grid(column=0, row=6, ipadx=10, ipady=5, pady=20)

# label Output
lbl_output = Label(root, text='OutPut:')
lbl_output.grid(column=2, row=0, padx=100)


# в этом label должны появляться Запросы
lbl_in = Label(root, text='asd')
lbl_in.grid(column=3, row=0)

# в этом label должны появляться Ответы
lbl_out = Label(root, text='out')
lbl_out.grid(column=3, row=1)

root.mainloop()

