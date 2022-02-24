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
    temp = RC4(keySeed, originalText)
    # Output
    print("Salida: " + str(temp))

    return


if __name__ == "__main__":
    main()
