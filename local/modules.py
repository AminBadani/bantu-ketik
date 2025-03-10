import re;

# Buka dan baca list kata yang ada di dalam dataset
def open_dataset(file_name: str):
    with open(file_name, 'r') as dataset:
        words = dataset.read().split('\n');
    
    return words

# Class yang digunakan untuk algoritma string matching dan dynamic programming
class ListKata:
    def __init__(self, dataset):
        self.dataset = dataset
        # cache digunakan untuk menyimpan list kata dari input yang sudah pernah di ketik
        self.cache = {}
        # list_lama digunakan untuk menyimpan list kata dari hasil rekomendasi kata sebelumnya
        self.list_lama = {}
        self.input_lama = ''

    def update_list(self, input_kata: str):
        # Masukkan input kata ke dalam regex
        prefix = re.compile('^' + input_kata, re.IGNORECASE);
        list_rekomendasi = {};

        # Cek apakah input kata sudah pernah di ketik
        # jika iya, maka ambil dari list kata dari cache
        if (input_kata in self.cache): 
            return self.cache[input_kata]
        
        '''
        Cek apakah input kata saat ini kurang dari input kata lama
        ini digunakan untuk mengecek jika user menghapus salah satu huruf dari input kata
        '''
        '''
        Cek apakah n huruf pertama dari input kata tidak sama dengan input lama
        ini digunakan untuk mengecek apakah pengguna menambahkan huruf baru bukan di akhir kata
        '''
        if (len(input_kata) < len(self.input_lama) or 
                input_kata[:len(self.input_lama)] != self.input_lama): 
            self.list_lama = {}

        # Cek isi dari list_lama
        # jika tidak ada isinya, maka filter kata dari dataset
        # jika ada isinya, maka filter kata dari list_lama
        if (len(self.list_lama) == 0): 
            list_rekomendasi = [word for word in self.dataset if prefix.match(word)]
        else: 
            list_rekomendasi = [word for word in self.list_lama if prefix.match(word)]

        # Masukkan hasil filter kata yang ada di dalam list_rekomendasi ke list_lama
        self.list_lama = list_rekomendasi
        # Ubah input_lama dengan input_kata saat ini
        self.input_lama = input_kata
        # Masukkan hasil list_rekomendasi ke dalam cache untuk digunakan kembali
        self.cache[input_kata] = list_rekomendasi;

        return list_rekomendasi