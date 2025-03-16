import re;

# Buka dan baca list kata yang ada di dalam dataset
def open_dataset(file_name: str):
    with open(file_name, 'r') as dataset:
        list_kata = dataset.read().split('\n');
    
    return list_kata

# Class yang digunakan untuk algoritma string matching dan dynamic programming
class ListKata:
    def __init__(self, dataset):
        self.dataset = dataset
        # history digunakan untuk menyimpan list kata dari input yang sudah pernah di ketik
        self.history = {}
        # list_lama digunakan untuk menyimpan list kata dari hasil rekomendasi kata sebelumnya
        self.list_lama = []
        self.input_lama = ''

    def update_list(self, input_kata: str):
        # Masukkan input kata ke dalam regex
        prefix = re.compile('^' + input_kata, re.IGNORECASE);
        list_rekomendasi = [];

        # Cek apakah input kata sudah pernah di ketik
        # jika iya, maka ambil list kata dari history
        if (input_kata in self.history): 
            self.list_lama = self.history[input_kata]
            self.input_lama = input_kata
            return self.history[input_kata]
        
        # Cek apakah list_lama ada isinya
        if (len(self.list_lama) == 0): 
            # Cari melalui dataset
            for kata in self.dataset:
                    if prefix.match(kata): list_rekomendasi.append(kata)
        else: 
            # Cari melalui dataset ketika:
            # pengguna tidak menambahkan input di akhir string
            # atau pengguna menghapus huruf dalam input
            if (input_kata[:len(self.input_lama)] != self.input_lama or len(input_kata) < len(self.input_lama)): 
                for kata in self.dataset:
                    if prefix.match(kata): list_rekomendasi.append(kata)
            else:
                # Cari melalui list_lama
                for kata in self.list_lama:
                    if prefix.match(kata): list_rekomendasi.append(kata)

        # Masukkan hasil yang ada di dalam list_rekomendasi ke list_lama
        self.list_lama = list_rekomendasi
        # Ubah input_lama dengan input_kata saat ini
        self.input_lama = input_kata
        # Masukkan hasil list_rekomendasi ke dalam history untuk digunakan kembali
        self.history[input_kata] = list_rekomendasi;

        return list_rekomendasi