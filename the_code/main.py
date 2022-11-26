import random
import tkinter as tk

def click():
  gacha = random.uniform(1, 100)
  a = gacha

  if a >= 50:
    outpud.configure(text="ไม่ติด")
  elif a >= 25:
    outpud.configure(text="ไม่มีอาการ")
  else:
    outpud.configure(text="มีอาการ")

window = tk.Tk()
window.title("covid random")
window.minsize(width=300, height=200)

name = tk.Label(master=window, text="จำลองการสุ่มติดโควิด")
button = tk.Button(master=window, text="คลิกเพื่อสุ่ม", comman=click)
outpud = tk.Label(master=window)

name.pack(pady=10)
button.pack(pady=10)
outpud.pack()

window.mainloop()