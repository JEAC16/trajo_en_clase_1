diccionario={
    "JUICIOSO":"persona responsable",
    "CHIMBA":"algo que las espectativas o algo bonito",
    "CRISPETAS":"también conocidas como , rosas, pochoclos, cabritas",
    "AGUACATE":"también conocido como palta"
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

#print(diccionario.keys())
if word in diccionario.keys():
    print(diccionario[word])
    
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("esa palabra no esta en el diccionario")
