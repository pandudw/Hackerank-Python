def selamat_pagi():
    return "Selamat pagi"

def selamat_siang():
    print("Selamat siang")

def selamat_malam():
    print("Selamat malam")

selamat_malam()

greeting = ["pagi", "siang", "malam"]
for i in greeting:
    if i == "pagi":  
        greet = selamat_pagi()
        print(greet)

