import tkinter;
import re;
from local.modules import open_dataset;
from local.modules import ListKata;

# Constant
WIDTH = 500;
HEIGHT = 500;
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
# Dipanggil ketika terjadi perubahan pada input pengguna
def input_on_change(*args):
    listbox_words.delete(0, 'end');

    # Pastikan input yang dimasukkan pengguna adalah alfabet
    if (re.match('^[a-z]+$', input_word.get(), re.IGNORECASE) != None):
        new_list = dataset.update_list(input_word.get())
        for word in new_list:
            listbox_words.insert('end', word)

# Dipanggil ketika listbox di klik menekan enter atau klik kiri pada mouse
def listbox_on_select(event):
    if (listbox_words.index('end') != 0):
        # Mengambil index dari kata yang dipilih
        for i in listbox_words.curselection():
            selected = listbox_words.get(i)
            # Menghapus lalu mengisikan input sesuai dengan kata yang dipilih
            input_field.delete(0, 'end');
            input_field.insert(0, selected)

# Dipanggil ketika tombol pada keyboard ditekan
def keyboard_on_press(event):
    # Cek apakah pengguna menekan keyboard bawah atau escape
    if (event.keysym == 'Down'):
        listbox_words.focus_set();
    elif (event.keysym == 'Escape'):
        input_field.focus_set();


# -- COMPONENTS
# Konfigurasi title, window size, dan disable minimize-maximize
app.title("BantuKetik - Simple Autocomplete");
app.geometry(screen_resolution)
app.resizable(False,False); 
app.bind("<Key>", keyboard_on_press);

# Input yang digunakan pengguna untuk mengetikkan kata
input_field = tkinter.Entry(app, textvariable=input_word, font=('Arial', 20));
input_word.trace_add(['write'], input_on_change);
# List kata yang ditampilakan ke pengguna
listbox_words = tkinter.Listbox(app, height=HEIGHT, font=('Arial', 20))
listbox_words.bind("<Return>", listbox_on_select);
listbox_words.bind("<Button>", listbox_on_select);
# Konfigurasi tata letak
input_field.pack(fill=tkinter.X, padx=(PADDING), pady=(PADDING, 0))
listbox_words.pack(fill=tkinter.X, padx=(PADDING))


app.mainloop();