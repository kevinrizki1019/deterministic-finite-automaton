hygiene = int(0)
energy = int(10)
fun = int(0)

state = [[["" for k in range(4)] for j in range(4)] for i in range(4)]

for i in range(len(state) - 1):
    for j in range(len(state[i]) - 1):
        for k in range(len(state[i][j]) - 1):
            state[i][j][k] = "State (" + str(i * 5) + " ," + str(j * 5) + ", " + str(k * 5) + ")"
