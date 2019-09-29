from State import hygiene, energy, fun, state 

def TidurSiang():
    global energy
    energy += 10
    print(energy)

def TidurMalam():
    global energy
    energy += 15

def MakanHamburger():
    global energy
    energy += 5

def MakanPizza():
    global energy
    energy += 10

def MakanSteakAndBans():
    global energy
    energy += 15

def MinumAir():
    global hygiene
    hygiene -= 5

def MinumKopi():
    global energy, hygiene
    energy += 5
    hygiene -= 10

def MinumJus():
    global energy, hygiene
    energy += 10
    hygiene -= 5

def BuangAirKecil():
    global hygiene
    hygiene += 5

def BuangAirBesar():
    global hygiene
    hygiene += 10

def BersosialisasiKeKafe():
    global hygiene, fun, energy
    hygiene -= 5
    fun += 15
    energy -= 5

def BermainMediaSosial():
    global fun, energy
    fun += 10
    energy -= 10

def BermainKomputer():
    global fun, energy
    fun += 15
    energy -= 10

def Mandi():
    global energy, hygiene
    hygiene += 15
    energy -= 5

def CuciTangan():
    global hygiene
    hygiene += 5

def MendengarkanMusikDiRadio():
    global energy, fun
    fun += 10
    energy -= 5

def MembacaKoran():
    global energy, fun
    fun += 5
    energy -= 5

def MembacaNovel():   
    global fun, energy 
    fun += 10
    energy -= 5