from tkinter import*
def clickbtn(num):
    global operator
    operator=operator+str(num)
    text_input.set(operator)

def equalbtn():
    try:
        
        global operator
        add=str(eval(operator))
        text_input.set(add)
        operator=""
    except:
        text_input.set("Error")
def clearbtn():
    global operator
    operator=""
    text_input.set("")

win=Tk()
win.title("My Calculator")
operator=""
text_input=StringVar()
txt_display=Entry(win,font=("arial",20,"bold"),textvariable=text_input,bd=30,insertwidth=4,
                  bg="red",justify="left").grid(columnspan=45)
b7=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="7",bg="powder blue",command=lambda:clickbtn(7)).grid(row=1,column=0)

b8=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="8",bg="powder blue",command=lambda:clickbtn(8)).grid(row=1,column=1)

b9=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="9",bg="powder blue",command=lambda:clickbtn(9)).grid(row=1,column=2)

b_plus=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="+",bg="powder blue",command=lambda:clickbtn("+")).grid(row=1,column=3)

b6=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="6",bg="powder blue",command=lambda:clickbtn(6)).grid(row=2,column=0)

b5=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="5",bg="powder blue",command=lambda:clickbtn(5)).grid(row=2,column=1)
b4=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="4",bg="powder blue",command=lambda:clickbtn(4)).grid(row=2,column=2)
b_minus=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="-",bg="powder blue",command=lambda:clickbtn("-")).grid(row=2,column=3)

b3=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="3",bg="powder blue",command=lambda:clickbtn(3)).grid(row=3,column=2)
b2=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="2",bg="powder blue",command=lambda:clickbtn(2)).grid(row=3,column=1)
b1=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="1",bg="powder blue",command=lambda:clickbtn(1)).grid(row=3,column=0)
b_multi=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="*",bg="powder blue",command=lambda:clickbtn("*")).grid(row=3,column=3)

b0=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="0",bg="powder blue",command=lambda:clickbtn(0)).grid(row=4,column=0)

b_clr=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="C",bg="powder blue",command=clearbtn).grid(row=4,column=1)
b_equal=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="=",bg="powder blue",command=equalbtn).grid(row=4,column=2)
b_div=Button(win,padx=16,bd=8,fg="black",font=("arial",20,"bold"),
          text="/",bg="powder blue",command=lambda:clickbtn("/")).grid(row=4,column=3)



win.mainloop()
