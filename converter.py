from tkinter import *
from tkinter import ttk

def find_res():
    l4 = Label(main, bg='black', fg='lightpink', textvariable=result_var,
               font=("Times New Roman", 15))
    l4.grid(row=4, column=1, padx=5, pady=5)

    mes_value = measurement.get()
    mes_nm = names.get()
    if mes_nm == 'F-C':
        result = (mes_value - 32) * (5 / 9)
        sort_val = str('%0.3f' % result)
        result_var.set(str(mes_value) + " °F to °C is " + sort_val)
    elif mes_nm == 'C-F':
        result = (mes_value * (9 / 5)) + 32
        sort_val = str('%0.3f' % result)
        result_var.set(str(mes_value) + " °C to °F is " + sort_val)
    elif mes_nm == 'F-K':
        result = ((mes_value - 32) * (5/9)) + 273.15
        sort_val = str('%0.3f' % result)
        result_var.set(str(mes_value) + " °F to K is " + sort_val)
    elif mes_nm == 'K-F':
        result = ((mes_value-(273.15)) * (9/5)) + 32
        sort_val = str('%0.3f' % result)
        result_var.set(str(mes_value) + " K  to °F is " + sort_val)
    elif mes_nm == 'C-K':
        result = mes_value + 273.15
        result_var.set(str(mes_value) + " °C to K is " + str(result))
    elif mes_nm == 'K-C':
        result = mes_value - 273.15
        result_var.set(str(mes_value) + " K to °C is " + str(result))
    else:
        result_var.set('Wrong Option Selected.')


main = Tk()
main.title('Temp Converter App')
main.geometry('580x200')
main.config(background="black")

result_var = StringVar()
measurement = DoubleVar()
names = StringVar()

l1 = Label(main, text='Temperature Converter', bg= 'black' ,fg='lightblue', font=("Ariel", 30))
l1.grid(row=0, column=1)


l2 = Label(main, text='Select measurement option:', bg='black', font=("Ariel", 15))
l2.grid(row=1, column=0, padx=2, pady=2)
d1 = ttk.Combobox(main, values=('F-C', 'C-F', 'F-K', 'K-F','C-K','K-C'), textvariable=names)
d1.set('F-K')
d1.grid(row=1, column=1, padx=2, pady=2)


l3 = Label(main, text='Enter Value:', bg='black', font=("Ariel", 15))
l3.grid(row=2, column=0)
E1 = Entry(main, textvariable=measurement)
E1.grid(row=2, column=1,pady=5)

b1 = Button(main, text="Convert", command=find_res, bd=5)
b1.grid(row=3, column=1)

l4 = Label(main, text="**digits are rounded upto 3 decimal places", bg='black', fg='lightgrey', font=("Times New Roman", 13))
l4.grid(row=4,column=0,padx=10)

main.mainloop()
