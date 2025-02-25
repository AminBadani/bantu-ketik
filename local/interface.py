import tkinter

# Window
interface = tkinter.Tk()
interface.title('BantuKetik - Simple Autocomplete'); 
interface.geometry("400x400") # Window size
interface.resizable(0, 0) # Disable maximize and minimize button

# Variables
user_input = tkinter.StringVar();
user_input.set('')

# Functions
# Event callback as observer to input_field
def get_user_input(var, index, mode):
    print(user_input.get());
user_input.trace_add('write', get_user_input)

# Components
label_input = tkinter.Label(interface, text = 'Masukkan input: ', font=('Arial', 12));
input_field = tkinter.Entry(interface, textvariable=user_input);
label_text = tkinter.Label(interface)

# Style
label_input.grid(row=0, pady=(10, 10), padx=(10, 0));
input_field.grid(row=0, column=1);
label_text.grid(row=1)

interface.mainloop()