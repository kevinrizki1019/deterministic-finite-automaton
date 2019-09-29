from State import hygiene, energy, fun, state 

def status():
    print(state[hygiene//5][energy//5][fun//5])

def CekStatusLebih(tambah_kebersihan = 0, tambah_energi = 0, tambah_kesenangan = 0):
    if ((hygiene + tambah_kebersihan > 15) or (energy + tambah_energi > 15) or (fun + tambah_kesenangan > 15)):
        print('Aksi tidak valid.')
        return True
    else:
        return False

def CekStatusKurang(kurang_kebersihan = 0, kurang_energi = 0, kurang_kesenangan = 0):
    if ((hygiene - kurang_kebersihan < 0) or (energy - kurang_energi < 0) or (fun - kurang_kesenangan < 0)):
        print('Aksi tidak valid.')
        return True
    else:
        return False

def TidurSiang():
    global energy
    if not CekStatusLebih(tambah_energi = 10):
        energy += 10


def TidurMalam():
    global energy
    if (not CekStatusLebih(tambah_energi = 15)):
        energy += 15

def MakanHamburger():
    global energy
    if (not CekStatusLebih(tambah_energi = 5)):
        energy += 5

def MakanPizza():
    global energy
    if (not CekStatusLebih(tambah_energi = 10)):
        energy += 10

def MakanSteakAndBans():
    global energy
    if (not CekStatusLebih(tambah_energi = 15)):
        energy += 15

def MinumAir():
    global hygiene
    if (not CekStatusLebih(tambah_kebersihan = 10)):
        hygiene -= 5

def MinumKopi():
    global energy, hygiene
    if (not CekStatusLebih(tambah_energy = 5) and not CekStatusKurang(kurang_kebersihan = 10)):
        energy += 5
        hygiene -= 10

def MinumJus():
    global energy, hygiene
    if (not CekStatusLebih(tambah_energy = 5) and not CekStatusKurang(kurang_kebersihan = 5)):
        energy += 10
        hygiene -= 5

def BuangAirKecil():
    global hygiene
    if (not CekStatusLebih(tambah_kebersihan = 5)):
        hygiene += 5

def BuangAirBesar():
    global hygiene
    if (not CekStatusLebih(tambah_kebersihan = 10)):
        hygiene += 10

def BersosialisasiKeKafe():
    global hygiene, fun, energy
    if (not CekStatusLebih(tambah_kesenangan = 15) and not CekStatusKurang(kurang_kebersihan = 5, kurang_energi = 5)):
        hygiene -= 5
        fun += 15
        energy -= 5

def BermainMediaSosial():
    global fun, energy
    if (not CekStatusLebih(tambah_kesenangan = 10) and not CekStatusKurang(kurang_energi = 10)):
        fun += 10
        energy -= 10

def BermainKomputer():
    global fun, energy
    if (not CekStatusLebih(tambah_kesenangan = 15) and not CekStatusKurang(kurang_energi = 10)):
        fun += 15
        energy -= 10

def Mandi():
    global energy, hygiene
    if (not CekStatusLebih(tambah_kebersihan= = 15) and not CekStatusKurang(kurang_energi = 5)):
        hygiene += 15
        energy -= 5

def CuciTangan():
    global hygiene
    if (not CekStatusLebih(tambah_kebersihan = 15)):
        hygiene += 5

def MendengarkanMusikDiRadio():
    global energy, fun
    if (not CekStatusLebih(tambah_kesenangan = 10) and not CekStatusKurang(kurang_energi = 5)):
        fun += 10
        energy -= 5

def MembacaKoran():
    global energy, fun
    if (not CekStatusLebih(tambah_kesenangan = 5) and not CekStatusKurang(kurang_energi = 5)):
        fun += 5
        energy -= 5

def MembacaNovel():   
    global fun, energy 
    if (not CekStatusLebih(tambah_kesenangan = 10) and not CekStatusKurang(kurang_energi = 5)):
        fun += 10
        energy -= 5