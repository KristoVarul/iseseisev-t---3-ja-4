def kuu_nimi(kuupaev):
    kuu = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober" "novembr", "detsember"]

def kuupaev_sõnena(kuupaev):
    i = kuupaev.split(".")
    paev = i[0]
    kuu = int(i[1])
    aasta = i[2]
    kuu_nimed = kuu_nimi(kuu)
    return (f"{paev}. {kuu_nimed}. {aasta}. a")

kuupaev = input("Sisesta kuupäeva kujul DD.MM.YYYY: ")
tulemus = kuupaev_sõnena(kuupaev)

print(tulemus)