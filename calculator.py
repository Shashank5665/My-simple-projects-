from tkinter import *
a = []

root = Tk()
root.title("Calculator")
root.minsize(340,390)
root.maxsize(340,390)

number = Entry(width=30, font=("Malgun Gothic",15), borderwidth=2)
number.place(x=3,y=3)

def click(num):
	a.append(num)
	no_of_clicks = (len(a))
	number.insert(no_of_clicks, num)

def clear():
	number.delete(0, END)

def solution():
	ans = number.get()
	answer = eval(ans)
	number.delete(0, END)
	number.insert(0, answer)


b7=Button(width=5,height=2,text="7",bg="#FFEDDF",fg="#DE4A00", font=("Malgun Gothic",16), relief="groove", command=lambda: click(7))
b7.place(x=5,y=40)

b8=Button(width=5,height=2,text="8",bg="#FFEDDF",fg="#DE4A00", font=("Malgun Gothic",16), relief="groove", command=lambda: click(8))
b8.place(x=79,y=40)

b9=Button(width=5,height=2,text="9", bg="#FFEDDF",fg="#DE4A00",font=("Malgun Gothic",16), relief="groove", command=lambda: click(9))
b9.place(x=153,y=40)

b4=Button(width=5,height=2,text="4", bg="#FFEDDF",fg="#DE4A00",font=("Malgun Gothic",16), relief="groove", command=lambda: click(4))
b4.place(x=5,y=127)

b5=Button(width=5,height=2,text="5",bg="#FFEDDF",fg="#DE4A00", font=("Malgun Gothic",16), relief="groove", command=lambda: click(5))
b5.place(x=79,y=127)

b6=Button(width=5,height=2,text="6", bg="#FFEDDF",fg="#DE4A00",font=("Malgun Gothic",16), relief="groove", command=lambda: click(6))
b6.place(x=153,y=127)

b1=Button(width=5,height=2,text="1", bg="#FFEDDF",fg="#DE4A00",font=("Malgun Gothic",16), relief="groove", command=lambda: click(1))
b1.place(x=5,y=214)

b2=Button(width=5,height=2,text="2", bg="#FFEDDF",fg="#DE4A00",font=("Malgun Gothic",16), relief="groove", command=lambda: click(2))
b2.place(x=79,y=214)

b3=Button(width=5,height=2,text="3",bg="#FFEDDF",fg="#DE4A00", font=("Malgun Gothic",16), relief="groove", command=lambda: click(3))
b3.place(x=153,y=214)

b0=Button(width=5,height=2,text="0", bg="#FFEDDF",fg="#DE4A00",font=("Malgun Gothic",16), relief="groove", command=lambda: click(0))
b0.place(x=79,y=301)

point=Button(width=5,height=2,text=".", font=("Malgun Gothic",16), relief="groove", command=lambda: click("."))
point.place(x=153,y=301)

clear=Button(width=5,height=2,text="C",fg="#D20000", font=("Malgun Gothic",16), relief="groove", command=clear)
clear.place(x=5,y=301)

add=Button(width=8,height=1,text="+",bg="#E8F1FF", fg="#004AEC", font=("Malgun Gothic",16), relief="groove", command=lambda: click("+"))
add.place(x=228,y=40)

sub=Button(width=8,height=1,text="-",bg="#E8F1FF",fg="#004AEC", font=("Malgun Gothic",16), relief="groove", command=lambda: click("-"))
sub.place(x=228,y=98)

mul=Button(width=8,height=1,text="x",bg="#E8F1FF",fg="#004AEC", font=("Malgun Gothic",16), relief="groove", command=lambda: click("*"))
mul.place(x=228,y=156)

div=Button(width=8,height=1,text="÷",bg="#E8F1FF",fg="#004AEC", font=("Malgun Gothic",16), relief="groove", command=lambda: click("/"))
div.place(x=228,y=214)

result=Button(width=4,height=1,text="=",fg="#FF1555", font=("Malgun Gothic",32), relief="groove", command=solution, pady=6)
result.place(x=228,y=272)

root.mainloop()