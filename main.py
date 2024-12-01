import tkinter as tk


window = tk.Tk()
window.geometry("360x600")
window.title("Calculator App")


num1 = 0
num2 = 0
cal_str_var = tk.StringVar()


screen = tk.Frame(window)
output = tk.Label(
    master=screen,
    textvariable=cal_str_var,
    font=('Segoe UI', 36)
)

screen.pack(expand=True, fill=tk.X)
output.pack(side=tk.RIGHT, padx=(0, 20))


btn_screen = tk.Frame(window, bg='#333333')
button_list = {
    "numbers": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'],
    "operators": ['+', '-', '*', '/', '='],
    "special": ['AC', 'C', '%']
}

number_btns_frame = tk.Frame(btn_screen)
operators_btns_frame = tk.Frame(btn_screen)
special_btns_frame = tk.Frame(btn_screen)

def button_click(btn_name: str):
    if btn_name == '=':
        val = eval(cal_str_var.get())
        cal_str_var.set(val)
    elif btn_name == 'AC':
        cal_str_var.set("")
    elif btn_name == 'C':
        cal_str_var.set(cal_str_var.get()[:-1])
    else:
        cal_str_var.set(cal_str_var.get() + btn_name)



def create_buttons(btn_name: str, btn_root):
    return tk.Button(
        master = btn_root,
        command= lambda: button_click(btn_name),
        text=btn_name,
        font=('Segoe UI', 12),
        fg='white',
        bg='#333333',
        padx=5,
        pady=5,
        relief=tk.FLAT,
        width=8,
        height=3,
    )


for key, value in button_list.items():
    btn_row = 0
    btn_column = 0
    for btn in value:
        if key == "numbers":

            if btn_column <= 2:
                create_buttons(btn, number_btns_frame).grid(
                    row=btn_row,
                    column=btn_column,
                    sticky="nsew"
                )
                btn_column += 1
            else:
                btn_row += 1
                btn_column = 0
                if btn == '0':
                    create_buttons(btn, number_btns_frame).grid(
                    row=btn_row,
                    column=btn_column,
                    columnspan=2,
                    sticky="nsew"
                    )
                    btn_column += 2
                else:
                    create_buttons(btn, number_btns_frame).grid(
                        row=btn_row,
                        column=btn_column,
                        sticky="nsew"
                    )
                    btn_column += 1
               

        elif key == "operators":
            create_buttons(btn, operators_btns_frame).pack()

        elif key == 'special':
            create_buttons(btn, special_btns_frame).pack(side=tk.LEFT)
        

btn_screen.pack(expand=True, fill=tk.BOTH)
special_btns_frame.grid(row = 0, column= 0)
number_btns_frame.grid(row = 1, column= 0, rowspan=4,)
operators_btns_frame.grid(row = 0, column = 1, rowspan=5,)

window.mainloop()
