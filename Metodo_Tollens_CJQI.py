usuario = input("¿Me llevare un paraguas?(Y/N): ")
if usuario == "N":
    premisa_1 = True  # Si está lloviendo (A), entonces llevaré un paraguas (B)
if usuario == "Y":
    premisa_1 = False  


premisa_2 = False  # No llevo un paraguas (no B)

if premisa_1 and not premisa_2:
    no_esta_lloviendo = False  # Conclusión: No está lloviendo (no A)
    print("No está lloviendo")
else:
    no_esta_lloviendo = True  # Conclusión: Está lloviendo (A)  
    print("Esta lloviendo, ten cuidado")