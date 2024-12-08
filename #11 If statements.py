#Video assistido: https://www.youtube.com/watch?v=rfscVS0vtbw&t=2298s
#"If Statement"

e_macho = True
e_alto = False

if e_macho:
    print("Você é um macho!")
else:
    print("Você não é um macho!")

if e_macho or e_alto:
    print("Você é um macho ou é alto ou os dois!")
else:
    print("Você não é nem um macho e nem alto!")

if e_macho and e_alto:
    print("Você é um macho e é alto ou os dois!")
else:
    print("Você não é um macho ou não é alto ou não é nenhum dos dois!")
#As frases estão horriveis mas é apenas pra aprender

if e_macho and e_alto:
    print("Você é um macho alto!")
elif not(e_macho) and e_alto:
    print("Você é alto mas não é macho")
elif e_macho and not(e_alto):
    print("Você é macho mas não é alto")
else:
    print("Você não é nem um macho e nem alto!")
#elif é o else if