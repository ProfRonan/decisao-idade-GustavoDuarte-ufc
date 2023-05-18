a = int(input())
if a < 0:
   print("impossível!")
elif a >=0 and a < 18:
   print("não precisa se alistar.")
elif a >= 18 and a <= 64:
    print("Não esqueça de votar na próxima eleição.")
elif a > 65:
    print("Vá descansar.")
else:
    print("eita!")    
