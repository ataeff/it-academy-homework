"""
Создать приложение из 100 потоков типа сетевой запрос/ответ, 50 запросов и 50 ответов. 
Ну чтобы ответы не перекрывали запросы применить переключатель СЕМАФОР и опционально LOCK. 
Число потоков оформить через range.
"""""
# Atayev Akmuhammet
# Lab 11.1

import threading
import time
class ActivePool:
    start = time.time()

    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()

    def makeRequest(self, name):
        with self.lock:
            self.active.append(name)
            tm = time.time() - self.start
            print(f'Время: {round(tm, 3)} Running: {self.active}')

    def gotRequest(self, name):
        with self.lock:
            self.active.remove(name)
            print(f'{name} получил ответ и удалён из пула')
            tm = time.time() - self.start
            print(f'Время: {round(tm, 3)} ждут ответ: {self.active}')

# -----------------------

def worker(sem, pool):
    with sem:
        th_name = threading.current_thread().name
        print(f'{th_name} ожидает присоединения к пулу')
        pool.makeRequest(th_name)
        time.sleep(0.5)
        pool.gotRequest(th_name)


sem = threading.Semaphore(5)

pool = ActivePool()

for i in range(50):
    t = threading.Thread(
        target=worker,
        args=(sem, pool),
    )
    t.start()


