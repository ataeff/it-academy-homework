""""
Оформить приложение в ткинтере. АЭРОДИНАМИЧЕСКИЕ ХАРАКТЕРИСТИКИ БПЛА:
~~~~~~~~~~~~ПОТРЕБНАЯ ТЯГА СИЛОВОЙ УСТАНОВКИ БПЛА~~~~~~~~~~~
--------------------- Tkinter App -----------------
"""""

from tkinter import *
import math as mt


class Aero:

    # Лошадиная сила (735,49875 Вт)
    # лошадиная сила определяется как 75 кгс·м/с

    def __init__(self, master):
        # ===== TK.INPUTS =====
        self.geom = master.geometry('600x400')
        master.resizable(False, False)

        # title_text
        Label(master, text='Аэродинамические Характеристики БЛА', font=('Montserrat Bold', 11)).grid()

        # input_weight
        self.w = IntVar()
        Label(master, text='Укажите вес Л/А(gramm): ', font=('Arial', 10)).grid(column=0, row=1, pady=10, sticky='w')
        Entry(master, width=5, textvariable=self.w).grid(column=1, row=1, pady=10)

        # input_S
        self.s = IntVar()
        Label(master, text='Укажите площадь крыла Л/А(dm2):', font=('Arial', 10)).grid(column=0, row=2, pady=10,
                                                                                       sticky='w')
        Entry(master, width=5, textvariable=self.s).grid(column=1, row=2, pady=10)

        # input_Cx
        self.cx = IntVar()
        Label(master, text='Укажите коэффициент сопротивления(Cx): ', font=('Arial', 10)) \
            .grid(column=0, row=3, pady=10, sticky='w')
        Entry(master, width=5, textvariable=self.cx).grid(column=1, row=3, pady=10)



        # ===== TK.OUTPUTS =====

        # line and title
        Label(master, text='================================').grid(column=0, row=5, columnspan=2)
        Label(master, text='Изменение от потребной тяги силовой установки при заданном (Cx): ') \
            .grid(column=0, row=6, columnspan=2)

        # results
        self.out_forceGauge = Label(master)
        self.out_h_p = Label(master)
        self.out_w_t = Label(master)
        self.out_r_wt = Label(master)

        # button
        self.but = Button(master, text="GO", width=60, height=2, command=self.main_func)
        self.but.grid(column=0, row=4, pady=10, columnspan=2, sticky='w')

        # grids (for results)
        self.out_forceGauge.grid(column=0, row=7, pady=5)
        self.out_h_p.grid(column=0, row=8, pady=5)
        self.out_w_t.grid(column=0, row=9, pady=5)
        self.out_r_wt.grid(column=0, row=10, pady=5)



    # ==== METHODS ====
    def forceGauge(self):
        # p = 1.23  # ПЛОТНОСТЬ ВОЗДУХА В ТРОПОСФЕРЕ НА УРОВНЕ МОРЯ
        self.res_f_g = round(mt.sqrt(2 * self.w.get() / self.cx.get() * 1.23 * self.s.get()), 2)
        self.out_forceGauge["text"] = str(self.res_f_g) + '\tkg/sec'

    def h_p(self):
        self.res_h_p = round(self.res_f_g / 75, 2)
        self.out_h_p["text"] = str(self.res_h_p) + '\th/p'

    def w_t(self):
        self.res_w_t = round(self.res_h_p * 735.5, 2)
        self.out_w_t["text"] = str(self.res_w_t) + '\tWt'

    def r_wt(self):
        self.res_r_wt = round(self.res_w_t / 1000, 2)
        self.out_r_wt["text"] = str(self.res_r_wt) + '\tkWt'

    # MAIN_FUNC for Button
    def main_func(self):
        self.forceGauge()
        self.h_p()
        self.w_t()
        self.r_wt()


if __name__ == "__main__":
    root = Tk()
    obj = Aero(root)
    root.mainloop()
