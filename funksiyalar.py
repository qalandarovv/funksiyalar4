def salomlash(ism,fam):
    text = f"Assalomu alaykum hurmatli {ism} {fam} jamomizga hush kelibsiz!"
    return text
ism = input("Ibrohimjon: ").title()
fam = input("Qalandarov: ").title()
print(salomlash(ism,fam))