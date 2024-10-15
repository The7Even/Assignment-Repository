import tkinter as tk
import random
import os.path
import tkinter.messagebox

circles = []
colors = ["red","green","blue"]

#Functions
def drawing(data):
    for j in data:
        canvas.create_oval(int(j[0])-int(j[2]),int(j[1])-int(j[2]),int(j[0])+int(j[2]),int(j[1])+int(j[2]),outline=j[3])

def create():
    circles.clear()
    for i in range(int(inputslot.get())):
        x = random.randint(50,550)
        y = random.randint(50,350)
        r = random.randint(10,50)
        c = random.choice(colors)
        circles.append([x,y,r,c])

    canvas.delete("all")

    drawing(circles)

def savefile():
    if os.path.isfile("circles.txt"):
        file = open("circles.txt","w",encoding="UTF-8")
        file.write("")
        for k in circles:
            file.write(f"{k[0]},{k[1]},{k[2]},{k[3]}\n")

    else:
        tk.messagebox.showerror(title="Error",message="file not found")

def delete():
    canvas.delete("all")

def readfile():
    global circles
    if os.path.isfile("circles.txt"):
        file = open("circles.txt","r",encoding="UTF-8")
        circles.clear()
        for line in file:
            line=line.rstrip()
            words=line.split(",")
            circles.append(words)

        drawing(circles)

    else:
        tk.messagebox.showerror(title="Error", message="file not found")

window=tk.Tk()
canvas = tk.Canvas(window, bg="white", width=600, height=400)
canvas.pack(expand=1, fill = tk.BOTH)

frame = tk.Frame(window)
frame.pack(expand = 1, fill = tk.X)
inputslot = tk.Entry(frame)
inputslot.pack(fill = tk.X, side=tk.LEFT,expand=1)
newcir = tk.Button(frame, text="새로운 원 생성", command=create)
newcir.pack(fill=tk.X, side=tk.LEFT,expand=1)
save = tk.Button(frame, text="파일 저장",command=savefile)
save.pack(fill=tk.X, side=tk.LEFT,expand=1)
delall = tk.Button(frame, text="모두 삭제",command=delete)
delall.pack(fill=tk.X, side=tk.LEFT,expand=1)
read = tk.Button(frame, text="파일 읽기", command=readfile)
read.pack(fill=tk.X, side=tk.LEFT,expand=1)

window.mainloop()