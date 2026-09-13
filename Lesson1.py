data_dictionary = {
    "nama": 'Maulana',
    "umur": 20,
    "now": "mahasiswa"
}
data_dictionary["nama"] = "Rifai" #mengganti value
data_dictionary["umur"] = 19 #mengganti value yang sudah
data_dictionary["jurusan"] = "TRPL" #menambah key dan value
umur_hapus= data_dictionary.pop("umur")


data = {'nama': 'Budi', 'umur': 25, 'kota': 'Jakarta'}

# Menghapus kunci 'umur'
umur_dihapus = data.pop('umur')
print(umur_dihapus)       # Output: 25
print(data)               # Output: {'nama': 'Budi', 'kota': 'Jakarta'}

# Menghapus kunci yang tidak ada dengan nilai default
hasil = data.pop('email', 'Tidak Ada')
print(hasil)              # Output: Tidak Ada   