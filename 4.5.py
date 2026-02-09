import os
print(os.getcwd())
from pathlib import Path


failinimi = input("Sisesta failinimi: ")

failitee = Path(failinimi)


def pronksikarva_summa(a_arv):
    summa = 0
    for arv in a_arv:
        if arv == 1:
            summa += 1
        if arv == 2:
            summa += 2
        if arv == 5:
            summa += 5
    return sum(a_arv)



a_arv = []
with open(failitee, "r", encoding="utf-8") as fail:
    for rida in fail:
        arv = int(rida.strip())
        a_arv.append(arv)

fail.close()

tulemus = pronksikarva_summa(a_arv)

print(f"Hoiupõrsasse läheb {tulemus} senti")