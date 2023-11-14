from tkinter import*
import random

root=Tk()
root.title("Lucky Friend Wheel")
root.geometry("400x600")

alphabets=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
list=Label(root)
list["text"] = alphabets
alph_1=""
alph_2=""
alph_3=""
alph_4=""
alph_5=""

Word_display=Label(root)

def random1():
    random_number1=random.randint(0,26)
    random_number2=random.randint(0,26)
    random_number3=random.randint(0,26)
    random_number4=random.randint(0,26)
    random_number5=random.randint(0,26)
    alph_1=alphabets[random_number1]
    alph_2=alphabets[random_number2]
    alph_3=alphabets[random_number3]
    alph_4=alphabets[random_number4]
    alph_5=alphabets[random_number5]
    Word_display["text"] = "Your random number is : " + alph_1 + alph_2 + alph_3 + alph_4 + alph_5 + ""
    
btn1=Button(root,text="Click me!",command=random1)
btn1.place(relx="0.5",rely="0.5",anchor=CENTER)

Word_display.place(relx="0.5",rely="0.4",anchor=CENTER)
list.place(relx="0.5",rely="0.3",anchor=CENTER)

root.mainloop()