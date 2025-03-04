import tkinter;
from local.modules import open_dataset, update_list;

WIDTH = 500;
HEIGHT = 400;
PADDING = 10;

app = tkinter.Tk();

screen_resolution = str(WIDTH) + 'x' + str(HEIGHT);
dataset = open_dataset('dataset_eng.txt');

input_word = tkinter.StringVar();
list_words = tkinter.Variable(value=dataset)

def on_change(*args):
    listbox_words.delete(0, 'end');

    new_list = update_list(dataset, input_word.get())
    for word in new_list:
        listbox_words.insert('end', word)

    return True;


app.title("BantuKetik - Simple Autocomplete");
app.geometry(screen_resolution); # Width x height
app.resizable(False,False); # Remove maximize and minimize

input_field = tkinter.Entry(app, textvariable=input_word);
input_word.trace_add(['write'], on_change);

listbox_words = tkinter.Listbox(app, height=HEIGHT, listvariable=list_words)

input_field.pack(fill=tkinter.X, padx=(PADDING), pady=(PADDING, 0))
listbox_words.pack(fill=tkinter.X, padx=(PADDING))


app.mainloop();