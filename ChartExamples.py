# Примеры построения графиков

import tkinter as tk

# Создание главного окна
window = tk.Tk()
window.geometry("450x450")
window.title("Примеры построения графиков")

# Добавление кнопки закрытия программы
btnClose = tk.Button(window, text="Закрыть", font = ('Helvetica', 10, 'bold'))
btnClose.place(x=330, y=400, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()
