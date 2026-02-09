soogihind = 10
ruumirent = 55
def eelarve(arv):
    summa = arv*55
    return summa
kutsutudinimesed = int(input("Mitu inimest on kutsutud?: "))
tulijad = int(input("Mitu inimest tuleb?: "))


maksimaalne_eelarve = eelarve(kutsutudinimesed, tulijad)
minimaalne_eelarve = eelarve(kutsutudinimesed, tulijad)
print(eelarve(kutsutudinimesed))
print(eelarve(tulijad))