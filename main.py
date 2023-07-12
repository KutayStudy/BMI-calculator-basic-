import tkinter

window = tkinter.Tk()
window.title("BMI calculator")
window.minsize(width=500,height=300)

def button_clicked():
    try:
        num = (float(my_entry.get()) / float(my_entry2.get()) ** 2)
        num2 = round(num,2)
        if num < 18.5:
            my_label3.config(text=f"your BMI is {num2}. You are underweight.")
        elif num >= 18.5 and num < 25:
            my_label3.config(text=f"your BMI is {num2}. You are normal weight.")
        elif num >= 25 and num < 30:
            my_label3.config(text=f"your BMI is {num2}. You are overweight")
        elif num >= 30 and num < 35:
            my_label3.config(text=f"your BMI is {num2}. You are obesity")
        elif num >= 35:
            my_label3.config(text=f"your BMI is {num2}. You are extreme obesity")
    except:
        my_label3.config(text="I need the numbers for this calculator.")

my_label = tkinter.Label(text="Enter your weight(kg)")
my_label.place(x=190,y=60)

my_label2 = tkinter.Label(text="Enter your height(m)")
my_label2.place(x=190,y=120)

my_entry = tkinter.Entry(width=12)
my_entry.place(x=210,y=85)

my_entry2 = tkinter.Entry(width=12)
my_entry2.place(x=210,y=145)

my_button = tkinter.Button(text="calculate",command=button_clicked)
my_button.place(x=217,y=180)

my_label3 = tkinter.Label()
my_label3.place(x=145,y=240)

window.mainloop()