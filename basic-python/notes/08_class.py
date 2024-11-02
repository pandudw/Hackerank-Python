class greeting():
    def selamat_pagi(self):
        print("hai selamat pagi")

    def selamat_malam(self, name):
        return (f"Hello, {name}")
    
    def selamat_siang(self):
        print(self.pandu, "Hai!")

greet = greeting()
greet.selamat_pagi()

night = greet.selamat_malam("pandu")
print(night)

greet.pandu = "selamat siang pandu!"
greet.selamat_siang()