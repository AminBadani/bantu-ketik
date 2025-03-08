import tkinter;
from local.modules import open_dataset, update_list;
from local.modules import ListKata;

# Constant
WIDTH = 500;
HEIGHT = 400;
PADDING = 10;


# Insialisasi tkinter
app = tkinter.Tk();

# -- VARIABLES
# Untuk menentukan lebar dan tinggi window
screen_resolution = str(WIDTH) + 'x' + str(HEIGHT);
# Untuk menyimpan list kata yang ada di dalam dataset
dataset = ListKata(open_dataset('dataset_eng.txt'));
# Untuk menyimpan input pengguna
input_word = tkinter.StringVar();


# -- Functions
# Mengecek jika terjadi perubahan pada input pengguna secara realtime
def on_change(*args):
    listbox_words.delete(0, 'end');

    new_list = dataset.update_list(input_word.get())
    # new_list = update_list(dataset, input_word.get())
    for word in new_list:
        listbox_words.insert('end', word)

    return True;


# -- COMPONENTS
# Konfigurasi title, window size, dan disable minimize-maximize
app.title("BantuKetik - Simple Autocomplete");
app.geometry(screen_resolution)
app.resizable(False,False); 

# Input yang digunakan pengguna untuk mengetikkan kata
input_field = tkinter.Entry(app, textvariable=input_word);
input_word.trace_add(['write'], on_change);
# List kata yang ditampilakan ke pengguna
listbox_words = tkinter.Listbox(app, height=HEIGHT,)
# Konfigurasi tata letak
input_field.pack(fill=tkinter.X, padx=(PADDING), pady=(PADDING, 0))
listbox_words.pack(fill=tkinter.X, padx=(PADDING))


app.mainloop();