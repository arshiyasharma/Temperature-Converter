from tkinter import *
from tkinter import ttk

def find_res():
    l4 = Label(main, bg='black', fg='grey', textvariable=result_var,
               font=("Times New Roman", 15))
    l4.grid(row=4, column=1, padx=5, pady=5)

    mes_value = measurement.get()
    mes_nm = names.get()
    if mes_nm == 'F-C':
        result = (mes_value - 32) * (5 / 9)
        sort_val = str('%0.2f' % result)
        result_var.set(str(mes_value) + " F to C is " + sort_val)
    elif mes_nm == 'C-F':
        result = (mes_value * (9 / 5)) + 32
        sort_val = str('%0.2f' % result)
        result_var.set(str(mes_value) + " C to F is " + sort_val)
    elif mes_nm == 'KM-M':
        result = (mes_value*1000)
        result_var.set(str(mes_value) + " KM to M is " + str(result))
    elif mes_nm == 'M-KM':
        result = (mes_value/1000)
        result_var.set(str(mes_value) + " M to KM is " + str(result))
    else:
        result_var.set('Wrong Option Selected.')


main = Tk()
main.title('Multi Converter App')
main.geometry('500x200')
main.config(background="black")

result_var = StringVar()
measurement = DoubleVar()
names = StringVar()

l1 = Label(main, text='Multi Converter', bg= 'black' ,fg='lightblue', font=("Ariel", 30))
l1.grid(row=0, column=1,padx=5,pady=5)


l2 = Label(main, text='Select measurement option:', bg='black', font=("Ariel", 15))
l2.grid(row=1, column=0, padx=5, pady=5)
d1 = ttk.Combobox(main, values=('F-C', 'C-F', 'KM-M', 'M-KM'), textvariable=names)
d1.set('F-C')
d1.grid(row=1, column=1, padx=5, pady=5)


l3 = Label(main, text='Enter Value:', bg='black', font=("Ariel", 15))
l3.grid(row=2, column=0, padx=5, pady=5)
E1 = Entry(main, textvariable=measurement)
E1.grid(row=2, column=1, padx=5, pady=5)

b1 = Button(main, text="Convert", command=find_res, bd=5)
b1.grid(row=3, column=1)

main.mainloop()
