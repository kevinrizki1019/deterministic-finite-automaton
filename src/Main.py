# file: Main.py, driver untuk menjalankan program utama The Sims Simulator
# @Sholeh To The Max : Fabian Zhafransyah - 13518022, Kevin Rizki Mohammad - 13518100
# 30 Sep 2019
# TUGAS BESAR TEORI BAHASA FORMAL DAN AUTOMATA 1
# THE SIMS SIMULATOR, Link: https://docs.google.com/document/d/1Te3TjxvMsjGSek1sFNQm1gMwnQhB4o2JZIFb8brC_KQ/edit

import Action
import State

if __name__ == "__main__":
    MasukanUser = input("Jalankan Permainan (YA/TIDAK)? ")
    if (MasukanUser != "TIDAK"):
        print('Jalanin aja dulu...') 
        print('')
        print('             @@@@@@@@@@@**&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('             @@@@@@*************@@@@@@@@@@@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('             @@@@@//////////////@@@@@@@@@@//////@@@@@@@@@@@@@@////////@@')
        print('             @@@@//////@@@@@@/@@@//////@@@//////@@@/////@@@////////////@')
        print('             @@@@//////@@@@@@@@@@//////@@@//////@@//////(@/////////////@')
        print('             @@@@(//////////@@@@@//////@@////////@///////@/////#@@@@@@@@')
        print('             @@@@@@(((((((((((((@((((((@@((((((((((((((((@(((((((((#@@@@')
        print('             ////@&@@(@((((((((((@(((((@@(((((((((((((((((@((((((((((((@')
        print('             @(@(@(#((@@@@@((((((@(((((@((((((((((((((((((@@@@@((((((((@')
        print('             @@@@@@%@@@@@@@((((((@(((((@(((((@((((((((((((@@#@@@@@#((((@')
        print('             @@@@@###############@#####@#####@######@##################@')
        print('             @@@@##############@@############@######@@################@@')
        print('             @@@@@@************@*****@@*****@@@*****@@@****@@@@@@*****@@')
        print('             @@@@@@@@@@**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('')
        print("                         *********************************")
        print("                         *                               *")
        print("                         *  MULAI PERMAINAN THE SIMS KW  *")
        print("                         *                               *")
        print("                         *********************************")
        Action.ShowPossibleAction()
        while (not Action.PermainanSelesai()):
            Action.TunjukkanStatus()
            Aksi = input("Masukkan Aksi: ")
            if (Aksi == "Tidur Siang"):
                Action.TidurSiang()
            elif (Aksi == "Tidur Malam"):
                Action.TidurMalam()
            elif (Aksi == "Makan Hamburger"):
                Action.MakanHamburger()
            elif (Aksi == "Makan Pizza"):
                Action.MakanPizza()
            elif (Aksi == "Makan Steak and Beans"):
                Action.MakanSteakAndBeans()
            elif (Aksi == "Minum Air"):
                Action.MinumAir()
            elif (Aksi == "Minum Kopi"):
                Action.MinumKopi()
            elif (Aksi == "Minum Jus"):
                Action.MinumJus()
            elif (Aksi == "Buang Air Kecil"):
                Action.BuangAirKecil()
            elif (Aksi == "Buang Air Besar"):
                Action.BuangAirBesar()
            elif (Aksi == "Bersosialisasi ke Kafe"):
                Action.BersosialisasiKeKafe()
            elif (Aksi == "Bermain Media Sosial"):
                Action.BermainMediaSosial()
            elif (Aksi == "Bermain komputer"):
                Action.BermainKomputer()
            elif (Aksi == "Mandi"):
                Action.Mandi()
            elif (Aksi == "Cuci Tangan"):
                Action.CuciTangan()
            elif (Aksi == "Mendengarkan Musik di Radio"):
                Action.MendengarkanMusikDiRadio()
            elif (Aksi == "Membaca Koran"):
                Action.MembacaKoran()
            elif (Aksi == "Membaca Novel"):
                Action.MembacaNovel()
            else:
                print("Aksi tidak valid")
            print("")
        Action.TunjukkanStatus()
        Action.CekStatusPermainanSelesai()
        

