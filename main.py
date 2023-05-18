a = int(input())
if a < 0:
   print("Impossível!")
elif a >=0 and a < 18:
   print("Não precisa se alistar.")
elif a >= 18 and a <= 64:
    print("Não esqueça de votar na próxima eleição.")
elif a > 65:
    print("Vá descansar.")
else:
    print("Eita!")    
