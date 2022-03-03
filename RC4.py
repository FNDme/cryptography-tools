from conversor import int_to_bin
# Key Scheduling Algorithm
def KSA(key):
    # Initialization
    S = [i for i in range(256)]
    K = [key[i % len(key)] for i in range(256)]
    j = 0

    # State Generation
    for i in range(256):
        j = (j + S[i] + K[i]) % 256
        S[i], S[j] = S[j], S[i]

    return S

# Pseudo Random Generation Algorithm
def PRGA(S, n):
    # Initialization
    i = 0
    j = 0
    temp = []

    # Generation of encoding bytes
    for _ in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        temp.append(S[t])

    return temp

# Rivest Cipher 4
def RC4(key, data):
    # Initialization
    S = PRGA(KSA(key), len(data))
    solution = []

    # Generation of coded bytes
    for i in range(len(data)):
        solution.append(data[i] ^ S[i])

    return solution

def RC4_Console(key, data):
    print("Semilla de clave = " + str(key))
    print("Texto original = " + str(data))
    print("\033[4mInicialización:\033[0m")
    S = [i for i in range(256)]
    print("S=[", S[0], ", ", S[1], ", ", S[2], ", ..., ", S[255], "]")
    K = [key[i % len(key)] for i in range(256)]
    print("K=[", K[0], ", ", K[1], ", ", K[2], ", ..., ", K[255], "]")
    j = 0
    for i in range(256):
        j = (j + S[i] + K[i]) % 256
        S[i], S[j] = S[j], S[i]
        if i == 0 or i == 1 or i == 2 or i == 254 or i == 255:
            print("S[", i, "] = ", S[i], " K[", i, "] = ", K[i], " produce f=", j, " y S[", i, "] = ", S[i], " S[", j, "] = ", S[j])
        elif i == 3:
            print("...")

    print("S=[", end="")
    for i in range(256):
        if(i < 13 or i > 250):
            print(S[i], end=", ")
        if i == 13:
            print("...", end=", ")
    print("]")
    i = 0
    j = 0
    temp = []
    print("\033[4mGeneración de secuencia cifrante y texto cifrado:\033[0m")
    for k in range(len(data)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        temp.append([S[t], t])

    solution = []
    for i in range(len(data)):
        solution.append(data[i] ^ temp[i][0])
        print("Byte ", (i + 1), " de secuencia cifrante: Salida= S[", temp[i][1], "] = ", temp[i][0], ":\t", int_to_bin(temp[i][0]))
        print("Byte ", (i + 1), " de texto original: Entrada: M[", (i + 1), "] = ", data[i], ":\t\t", int_to_bin(data[i]))
        print("Byte ", (i + 1), " de texto cifrado, Salida= C[", (i + 1), "] = ", solution[i], ":\t\t", int_to_bin(solution[i]))
        print()
    return solution

# Terminal version
def main():
    # Input keySeed
    print("Entrada:")
    keySeed = input("Semilla de clave: ")
    keySeed = keySeed.split(",")
    keySeed = [int(i) for i in keySeed]
    # Input data
    originalText = input("Texto original: ")
    originalText = originalText.split(",")
    originalText = [int(i) for i in originalText]
    # Encoding
    temp = RC4_Console(keySeed, originalText)
    # Output
    print("Salida: " + str(temp))

    return


if __name__ == "__main__":
    main()
