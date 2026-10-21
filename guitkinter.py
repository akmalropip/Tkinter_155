import tkinter as tk

top = tk.Tk()
top.title("Prediksi Prodi Pilihan")

L1 = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
L1.pack()

L2 = tk.Label(top, text="Masukkan Nilai Mata Pelajaran")
L2.pack()

L3 = tk.Label(top, text="Matematika")
L3.pack()
E1 = tk.Entry(top, bd=3)
E1.pack()

L4 = tk.Label(top, text="Bahasa Indonesia")
L4.pack()
E2 = tk.Entry(top, bd=3)
E2.pack()

L5 = tk.Label(top, text="Bahasa Inggris")
L5.pack()
E3 = tk.Entry(top, bd=3)
E3.pack()

L6 = tk.Label(top, text="Fisika")
L6.pack()
E4 = tk.Entry(top, bd=3)
E4.pack()

L7 = tk.Label(top, text="Kimia")
L7.pack()
E5 = tk.Entry(top, bd=3)
E5.pack()

L8 = tk.Label(top, text="Biologi")
L8.pack()
E6 = tk.Entry(top, bd=3)
E6.pack()

L9 = tk.Label(top, text="Sejarah")
L9.pack()
E7 = tk.Entry(top, bd=3)
E7.pack()

L10 = tk.Label(top, text="Ekonomi")
L10.pack()
E8 = tk.Entry(top, bd=3)
E8.pack()

L11 = tk.Label(top, text="Geografi")
L11.pack()
E9 = tk.Entry(top, bd=3)
E9.pack()

L12 = tk.Label(top, text="Informatika")
L12.pack()
E10 = tk.Entry(top, bd=3)
E10.pack()

def hasilPrediksi():
    L13.config(text="Hasil Prediksi: Teknologi Informasi") #mengubah tulisan pada label hasil

L13 = tk.Label(top, text="Hasil Prediksi: ")
L13.pack()

B1 = tk.Button(top, text="Hasil Prediksi", command=hasilPrediksi) #saat tombol diklik, fungsi hasilPrediksi dijalankan
B1.pack()

L13 = tk.Label(top, text="Hasil Prediksi: -")
L13.pack()

top.mainloop()
