class mulai:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def tampil(self, fungsi):
        print("ini di fungsi kedua : {}".format(fungsi.nama))
        print("ini adalah nama sebenarnya : {} dengan umur {}".format(
            self.nama, self.umur))


area = mulai("Diana", 12)
area.tampil(mulai("anton", 13))
