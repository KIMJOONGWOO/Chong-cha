from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
import tkinter.messagebox
from tkinter import *
import tkinter as tk


def spawn2():
    global image1

    top2 = tk.Toplevel(window)
    top2.title("콩차 결제 창")
    top2['bg'] = 'white'
    top2.geometry("540x400")
    label10 = tk.Label(top2, image=image1)
    label10.place(x=0, y=0)

    a = select()
    b = select2()
    c = a+b

    fin = "결제금액은" + str(c)+"원입니다."

    fin = tk.Label(top2, text=fin, font=("맑은 고딕", 20), fg="black", bg="white")
    fin.place(x=100, y=210)

    btn3 = Button(top2, text="결제 진행", command=info)
    btn3.place(x=180, y=350)


def info():
    msg = tkinter.messagebox.askokcancel("결제 완료창", "결제가 정상적으로 처리되었습니다.")

    if msg == 'yes':
        window.destroy()
    else:
        window.destroy()


def spawn():
    global image1, lmage8, image9, radio

    top = tk.Toplevel(window)
    top.title("콩차 펄 추가 주문")
    top['bg'] = 'white'
    top.geometry("540x400")
    #image7 = tk.PhotoImage(file="콩차.png")
    label9 = tk.Label(top, image=image9)
    label8 = tk.Label(top, image=image8)
    label7 = tk.Label(top, image=image1)
    label9.place(x=300, y=120)
    label8.place(x=30, y=120)
    label7.place(x=0, y=0)

    r6 = Radiobutton(top, text="블랙펄\n300원", variable=radio, value="300",
                     fg="black", bg="white")
    r6.place(x=85, y=250)

    r7 = Radiobutton(top, text="화이트펄\n500원", variable=radio, value="500",
                     fg="black", bg="white")
    r7.place(x=355, y=250)

    btn2 = Button(top, text="결제", command=spawn2)
    btn2.place(x=180, y=350)

    quitButton2 = Button(top, text='주문취소 및 종료', command=exist)
    quitButton2.place(x=300, y=350)


def select():
    if r.get() == 3500:
        select = "패션후르츠가 선택되었습니다."
    if r.get() == 4000:
        select = "타로밀크티가 선택되었습니다."
    if r.get() == 5000:
        select = "딸기요거트크러쉬가 선택되었습니다."
    if r.get() == 4300:
        select = "민트초코가 선택되었습니다."
    if r.get() == 5200:
        select = "망고요구르트가 선택되었습니다."
    show.config(text=select)
    a = r.get()
    return a


def select2():
    b = radio.get()
    return b


def exist():
    window.destroy()


window = tk.Tk()
window.title("콩차 음료 주문")
window['bg'] = 'white'
window.geometry("540x400")

radio = IntVar()

image8 = PhotoImage(file="블랙펄.png")
image9 = PhotoImage(file="화이트펄.png")
quitButton = Button(window, text='주문취소 및 종료', command=exist)


btn1 = Button(window, text="펄추가", command=spawn)
label = Label(window, text="메뉴를 선택해주세요.", font=("맑은 고딕", 20),
              fg="black", bg="white", width="20", height="5")
image1 = PhotoImage(file="콩차.png")
label1 = Label(window, image=image1)

r = IntVar()

image2 = PhotoImage(file="콩차패션후르츠.png")
label2 = Label(window, image=image2)
r1 = Radiobutton(window, text="패션후르츠\n3500원", variable=r, value="3500",
                 fg="black", bg="white", command=select)
r1.place(x=10, y=210)

image3 = PhotoImage(file="콩차타로밀크티.png")
label3 = Label(window, image=image3)
r2 = Radiobutton(window, text="타로밀크티\n4000원", variable=r, value="4000",
                 fg="black", bg="white", command=select)
r2.place(x=110, y=210)

image4 = PhotoImage(file="콩차딸기요거트크러쉬.png")
label4 = Label(window, image=image4)
r3 = Radiobutton(window, text="딸기요거트\n크러쉬\n5000원", variable=r,
                 value="5000", fg="black", bg="white", command=select)
r3.place(x=210, y=210)

image5 = PhotoImage(file="콩차민트초코.png")
label5 = Label(window, image=image5)
r4 = Radiobutton(window, text="민트초코\n4300원", variable=r, value="4300",
                 fg="black", bg="white", command=select)
r4.place(x=310, y=210)

image6 = PhotoImage(file="콩차망고요구르트.png")
label6 = Label(window, image=image6)
r5 = Radiobutton(window, text="망고요구르트\n5200원", variable=r, value="5200",
                 fg="black", bg="white", command=select)
r5.place(x=410, y=210)

btn1.place(x=160, y=350)
label1.place(x=0, y=0)
label2.place(x=30, y=140)
label3.place(x=130, y=140)
label4.place(x=230, y=140)
label5.place(x=330, y=140)
label6.place(x=430, y=140)
quitButton.place(x=250, y=350)

show = Label(window, font=("맑은 고딕", 10), fg="black", bg="white")
show.place(x=150, y=280)

window.mainloop()
