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