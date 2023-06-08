# =======================
# without __init__
#========================
class mahasiswa():
    def belajar(self, kondisi):
        print(self.nama, "sedang belajar", kondisi)
    def tidur(self, kondisi):
        print(self.nama, "tidur di kamar", kondisi)

nasrul = mahasiswa()
nadia  = mahasiswa()

nasrul.nama = "Nasrullah Pandu Dewantara"
nadia.nama  = "Nadia Wartiningrum"

nasrul.belajar("Python")
nadia.tidur("bersama pampam")

# =======================
# with __init__
#========================
class mahasiswa():
    def __init__(self, input_nama, input_kondisi):
        self.nama       = input_nama
        self.kondisi    = input_kondisi

nasrul = mahasiswa("Nasrullah Pandu Dewantara", "Sedang Belajar Python")
print(nasrul.nama, nasrul.kondisi)
nadia  = mahasiswa("Nadia Wartiningrum", "Sedang Tidur Bersama pampam")
print(nadia.nama, nadia.kondisi)