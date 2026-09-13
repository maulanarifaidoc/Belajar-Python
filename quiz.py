data_mahasiswa= {
    'Nama' : "Budi",
    'Umur' : 20,
    'Jurusan': "Informatika",
    'Semester': 3
}
print(data_mahasiswa['Nama'])
print(data_mahasiswa['Jurusan'])

data_mahasiswa['Umur'] = 21 #mengganti value
data_mahasiswa['IPK'] = 3.75 #Menambah Key
print(data_mahasiswa['Umur'])
print(data_mahasiswa['IPK'])
