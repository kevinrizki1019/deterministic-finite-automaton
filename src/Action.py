# file: Action.py, tempat menyimpan struktur data dari aksi DFA yang diberikan
# @Sholeh To The Max : Fabian Zhafransyah - 13518022, Kevin Rizki Mohammad - 13518100
# 30 Sep 2019
# TUGAS BESAR TEORI BAHASA FORMAL DAN AUTOMATA 1
# THE SIMS SIMULATOR, Link: https://docs.google.com/document/d/1Te3TjxvMsjGSek1sFNQm1gMwnQhB4o2JZIFb8brC_KQ/edit

from State import hygiene, energy, fun

def TunjukkanStatus():
    """
    Mencetak ke layar status state saat ini direpresentasikan dengan nilai atribut hygiene, energy, dan fun
    """
    print(" STATE SAAT INI ")
    print(" ______________ ")
    print(" ")
    print(" Hygiene =", hygiene)
    print(" Energy  =", energy)
    print(" Fun     =", fun)
    print(" ______________ ")

def CekStatusLebih(tambah_kebersihan = 0, tambah_energi = 0, tambah_kesenangan = 0):
    """
    Mengvalidasi apakah proses penambahan atribut dapat dilakukan
    """
    if ((hygiene + tambah_kebersihan > 15) or (energy + tambah_energi > 15) or (fun + tambah_kesenangan > 15)):
        print('Aksi tidak valid.')
        return True
    else:
        return False

def CekStatusKurang(kurang_kebersihan = 0, kurang_energi = 0, kurang_kesenangan = 0):
    """
    Mengvalidasi apakah proses pengurangan atribut dapat dilakukan
    """
    if ((hygiene - kurang_kebersihan < 0) or (energy - kurang_energi < 0) or (fun - kurang_kesenangan < 0)):
        print('Aksi tidak valid.')
        return True
    else:
        return False

def TidurSiang():
    """
    Menambahkan atribut energy sejumlah 10 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    """
    global energy
    if not CekStatusLebih(tambah_energi = 10):
        energy += 10

def TidurMalam():
    """
    Menambahkan atribut energy sejumlah 15 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    """
    global energy
    if (not CekStatusLebih(tambah_energi = 15)):
        energy += 15

def MakanHamburger():
    """
    Menambahkan atribut energy sejumlah 5 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    """
    global energy
    if (not CekStatusLebih(tambah_energi = 5)):
        energy += 5

def MakanPizza():
    """
    Menambahkan atribut energy sejumlah 10 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    """
    global energy
    if (not CekStatusLebih(tambah_energi = 10)):
        energy += 10

def MakanSteakAndBeans():
    """
    Menambahkan atribut energy sejumlah 15 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    """
    global energy
    if (not CekStatusLebih(tambah_energi = 15)):
        energy += 15

def MinumAir():
    """
    Mengurangkan atribut hygiene sejumlah 5 nilai
    tidak dilakukan proses jika pengurangan nilai kurang dari nilai minimum  
    """
    global hygiene
    if (not CekStatusKurang(kurang_kebersihan = 5)):
        hygiene -= 5

def MinumKopi():
    """
    Menambahkan atribut energy sejumlah 5 nilai
    Mengurangkan atribut hygiene sejumlah 10 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    tidak dilakukan proses jika pengurangan nilai kurang dari nilai minimum  
    """
    global energy, hygiene
    if (not CekStatusLebih(tambah_energi = 5) and not CekStatusKurang(kurang_kebersihan = 10)):
        energy += 5
        hygiene -= 10

def MinumJus():
    """
    Menambahkan atribut energy sejumlah 10 nilai
    Mengurangkan atribut hygiene sejumlah 5 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    tidak dilakukan proses jika pengurangan nilai kurang dari nilai minimum  
    """
    global energy, hygiene
    if (not CekStatusLebih(tambah_energi = 10) and not CekStatusKurang(kurang_kebersihan = 5)):
        energy += 10
        hygiene -= 5

def BuangAirKecil():
    """
    Menambahkan atribut hygiene sejumlah 5 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    """
    global hygiene
    if (not CekStatusLebih(tambah_kebersihan = 5)):
        hygiene += 5

def BuangAirBesar():
    """
    Menambahkan atribut hygiene sejumlah 10 nilai
    Mengurangkan atribut energy sejumlah 5 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    tidak dilakukan proses jika pengurangan nilai kurang dari nilai minimum  
    """
    global hygiene, energy
    if (not CekStatusLebih(tambah_kebersihan = 10) and not CekStatusKurang(kurang_energi = 5)):
        hygiene += 10
        energy -= 5

def BersosialisasiKeKafe():
    """
    Menambahkan atribut fun sejumlah 15 nilai
    Mengurangkan atribut energy sejumlah 10 nilai
    Mengurangkan atribut hygiene sejumlah 5 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    tidak dilakukan proses jika pengurangan nilai kurang dari nilai minimum  
    """
    global hygiene, fun, energy
    if (not CekStatusLebih(tambah_kesenangan = 15) and not CekStatusKurang(kurang_kebersihan = 5, kurang_energi = 10)):
        hygiene -= 5
        fun += 15
        energy -= 10

def BermainMediaSosial():
    """
    Menambahkan atribut fun sejumlah 10 nilai
    Mengurangkan atribut energy sejumlah 10 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    tidak dilakukan proses jika pengurangan nilai kurang dari nilai minimum  
    """
    global fun, energy
    if (not CekStatusLebih(tambah_kesenangan = 10) and not CekStatusKurang(kurang_energi = 10)):
        fun += 10
        energy -= 10

def BermainKomputer():
    """
    Menambahkan atribut fun sejumlah 15 nilai
    Mengurangkan atribut energy sejumlah 10 nilai  
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    tidak dilakukan proses jika pengurangan nilai kurang dari nilai minimum   
    """
    global fun, energy
    if (not CekStatusLebih(tambah_kesenangan = 15) and not CekStatusKurang(kurang_energi = 10)):
        fun += 15
        energy -= 10

def Mandi():
    """
    Menambahkan atribut fun sejumlah 15 nilai
    Mengurangkan atribut energy sejumlah 5 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    tidak dilakukan proses jika pengurangan nilai kurang dari nilai minimum  
    """
    global energy, hygiene
    if (not CekStatusLebih(tambah_kebersihan = 15) and not CekStatusKurang(kurang_energi = 5)):
        hygiene += 15
        energy -= 5

def CuciTangan():
    """
    Menambahkan atribut hygiene sejumlah 5 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    """    
    global hygiene
    if (not CekStatusLebih(tambah_kebersihan = 5)):
        hygiene += 5

def MendengarkanMusikDiRadio():
    """
    Menambahkan atribut fun sejumlah 10 nilai
    Mengurangkan atribut energy sejumlah 5 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    tidak dilakukan proses jika pengurangan nilai kurang dari nilai minimum  
    """
    global energy, fun
    if (not CekStatusLebih(tambah_kesenangan = 10) and not CekStatusKurang(kurang_energi = 5)):
        fun += 10
        energy -= 5

def MembacaKoran():
    """
    Menambahkan atribut fun sejumlah 5 nilai
    Mengurangkan atribut energy sejumlah 5 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    tidak dilakukan proses jika pengurangan nilai kurang dari nilai minimum  
    """
    global energy, fun
    if (not CekStatusLebih(tambah_kesenangan = 5) and not CekStatusKurang(kurang_energi = 5)):
        fun += 5
        energy -= 5

def MembacaNovel():
    """
    Menambahkan atribut fun sejumlah 10 nilai
    Mengurangkan atribut energy sejumlah 5 nilai
    tidak dilakukan proses jika penambahan nilai lebih dari nilai maksimum  
    tidak dilakukan proses jika pengurangan nilai kurang dari nilai minimum  
    """
    global energy, fun   
    if (not CekStatusLebih(tambah_kesenangan = 10) and not CekStatusKurang(kurang_energi = 5)):
        fun += 10
        energy -= 5

def PermainanSelesai():
    """
    Mengembalikan nilai true jika permainan selesai, 
    yaitu ketika semua atribut bernilai 15 atau semua atribut bernilai 0
    """
    return ((hygiene == 15) and (energy == 15) and (fun == 15)) or ((hygiene == 0) and (energy == 0) and (fun ==0))

def CekStatusPermainanSelesai():
    """
    Mencetak ke layar hasil dari permainan bergantung pada state ketika permainan selesai, 
    yaitu antara semua atribut bernilai 15 atau semua atribut bernilai 0
    """
    if ((hygiene == 15) and (energy == 15) and (fun ==15)):
        print("Permainan Selesai! Anda Menang")
    else:  #((hygiene == 0) and (energy == 0) and (fun ==0))
        print("Permainan Selesai! Anda Mati dan Kalah")

def ShowPossibleAction():
    print("")
    print("AKSI YANG BISA DILAKUKAN: ")
    print("1. Tidur Siang")
    print("2. Tidur Malam")
    print("3. Makan Hamburger")
    print("4. Makan Pizza")
    print("5. Makan Steak and Beans")
    print("6. Minum Air")
    print("7. Minum Kopi")
    print("8. Minum Jus")
    print("9. Buang Air Kecil")
    print("10. Buang Air Besar")
    print("11. Besosialisasi ke Kafe")
    print("12. Bermain Media Sosial")
    print("13. Bermain komputer")
    print("14. Mandi")
    print("15. Cuci Tangan")
    print("16. Mendengarkan Musik di Radio")
    print("17. Membaca Koran")
    print("18. Membaca Novel")
    print(" ______________")
    print(" ")