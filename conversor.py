base10 = int(input("Número a ser convertido (base 10): "))

arrResult = []
arrMod = []

result = base10 // 2 
mod = base10 % 2

arrResult.append(result)
arrMod.append(mod)

while result >= 2:
    mod = result % 2
    result = result // 2
    arrResult.append(result)
    arrMod.append(mod)

arrMod.append(arrResult[-1])
arrMod.reverse()

binario = ''.join([str(n) for n in arrMod])
    
print(arrResult)
print(arrMod)
print("base 2:", binario)
    
    