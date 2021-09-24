def changeAds(base10):
    arrMod = []
    arrBin = []

    result = base10 // 2 
    mod = base10 % 2

    arrMod.append(mod)

    while result >= 2:
        mod = result % 2
        result = result // 2
        arrMod.append(mod)

    arrMod.append(result)
    arrMod.reverse()

    for i in arrMod:
        if i == 1:
            i = 0
            arrBin.append(i)
        else:
            i = 1
            arrBin.append(i)

    length = len(arrBin)-1
    decimal = 0

    for i in arrBin:
        n = i*2**length
        length = length - 1
        decimal = decimal + n
    
    return print(decimal)

base10 = int(input("Número a ser convertido (base 10): "))

changeAds(base10)