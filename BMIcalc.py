from tkinter import *
from tkinter import messagebox


def get_height(): #height will be centimeters
    '''
       This function gets height value from Entry field
    '''
    height = float(ENTRY2.get())
    return height

def get_weight(): #weight will be in kilograms
    '''
       This function gets weight value from Entry field
    '''
    weight = float(ENTRY1.get())
    return weight

def calculate_bmi(a=""):   # "a" is there because the bind function gives an argument to the function....
    print(a)
    '''
      This function calculates the result
    '''
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        if bmi <= 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!" #Removed very severely underweight and severely underwight sections and just made one section for underweight to make it more simple 
            messagebox.showinfo("Result", res)
        elif 18.5 <= bmi <= 24.9:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Normal."
            messagebox.showinfo("Result", res)
        elif 25.0 < bmi <= 29.9:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight!"
            messagebox.showinfo("Result", res)
        elif 30.0 < bmi <= 34.9:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Obese!"
            messagebox.showinfo("Result", res)  
        elif 35.0 < bmi <= 40.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Extremely Obese!" #Removed other obese sections and chanhged the wording but not sure if I have eneded it correctly
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Extremely Obese!" 
            messagebox.showinfo("Result", res)


if __name__ == '__main__':
    TOP = Tk()
    TOP.bind("<Return>", calculate_bmi)
    TOP.geometry("400x400")
    TOP.configure(background="#783230") #changed the color 
    TOP.title("BMI Calculator")
    TOP.resizable(width=False, height=False)
    LABLE = Label(TOP, bg="#783230", text="Welcome to BMI Calculator", font=("Avenir Next Condensed", 15, "bold"), pady=10) #attempted to change the font
    LABLE.place(x=55, y=0)
    LABLE1 = Label(TOP, bg="#cef0f1", text="Enter Weight (in kg):", bd=6,
                   font=("Avenir Next Condensed", 10, "bold"), pady=5)
    LABLE1.place(x=55, y=60)
    ENTRY1 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY1.place(x=240, y=60)
    LABLE2 = Label(TOP, bg="#cef0f1", text="Enter Height (in cm):", bd=6,
                   font=("Avenir Next Condensed", 10, "bold"), pady=5)
    LABLE2.place(x=55, y=121)
    ENTRY2 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY2.place(x=240, y=121)
    BUTTON = Button(bg="#2187e7", bd=12, text="BMI", padx=33, pady=15, command=calculate_bmi,
                    font=("Avenir Next Condensed", 20, "bold"))
    BUTTON.grid(row=3, column=0, sticky=W)
    BUTTON.place(x=115, y=250)
    TOP.mainloop()
