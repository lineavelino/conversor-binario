#Receber um número decimal -> converter para binário -> 
#reverter cada um dos números do binário (zero vira 1 e vice-versa) -> 
#converter o novo binário para decimal

base10 = int(input("Número a ser convertido (base 10): "))

arrMod = []

result = base10 // 2 
mod = base10 % 2

arrMod.append(mod)

while result >= 2:
    mod = result % 2
    result = result // 2
    arrMod.append(mod)

arrMod.append(result)
arrMod.reverse()

binario = ''.join([str(n) for n in arrMod])
    
print("base 2:", binario)