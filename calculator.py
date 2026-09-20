import tkinter as tk


def press_button(char):
    current = display_var.get()
    
    if char == "C":
    
        display_var.set("")
    elif char == "=":
        try:
            
            result = str(eval(current))
            display_var.set(result)
        except Exception as e:
            
            display_var.set("Error")
    else:
        
        display_var.set(current + str(char))


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x450")
root.configure(bg="#202020") 


display_var = tk.StringVar()


display = tk.Entry(
    root, 
    textvariable=display_var, 
    font=("Arial", 24), 
    bd=10, 
    insertwidth=4, 
    width=14, 
    borderwidth=0, 
    justify="right", 
    bg="#333333", 
    fg="white"
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

# बटन्स का लेआउट (Grid)
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]


for row_idx, row in enumerate(buttons):
    for col_idx, text in enumerate(row):
        
    
        if text == "=":
            bg_color = "#ff9500"  
            fg_color = "white"
        elif text in ["/", "*", "-", "+"]:
            bg_color = "#f1a33c"  
            fg_color = "white"
        elif text == "C":
            bg_color = "#d4d4d2" 
            fg_color = "black"
        else:
            bg_color = "#505050" 
            fg_color = "white"

       
        btn = tk.Button(
            root, 
            text=text, 
            padx=20, 
            pady=20, 
            font=("Arial", 16, "bold"),
            bg=bg_color, 
            fg=fg_color, 
            borderwidth=0,
            activebackground="#777777",
            command=lambda t=text: press_button(t) 
        )
        
         
        btn.grid(row=row_idx + 1, column=col_idx, padx=5, pady=5, sticky="nsew")

for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(5):
    root.rowconfigure(i, weight=1)
