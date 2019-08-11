def hd(a):
    dic = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8,"9":9,"A":10, "B": 11, "C":12, "D":13, "E":14, "F":15}    
    e = 0
    soma = 0
    for i in range(len(a)-1, -1, -1):
        soma += int(dic[a[i].upper()]) * 16**e
        e += 1
    return soma

def dh(dvd):
    dic = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8",9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    DVS = 16
    saida = ""
    while dvd >= 16:
        saida = dic[dvd%DVS] + saida
        dvd = dvd // DVS
    
    saida = dic[dvd] + saida
    return "0x"+saida

def converte(num):
    if len(num) > 2 and num[1] == 'x':
        return hd(num[2:])
    else: return dh(int(num))

en = input()

while en != "-1":
    print(converte(en))
    en = input()

