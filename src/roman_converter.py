def decimal_a_romano(numero):
    valor=1
    
    convercion={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
   
    resultado = ""
    for valor in sorted(convercion.keys(), reverse=True):
        while numero >= valor:
            resultado += convercion[valor]
            numero -= valor
    return(resultado)

    

numero=0
numero=int(input("¿Cuál es tu número decimal (1 a 3999)? "))
while numero > 3999 or numero <= 0:
    print("Error: el número debe estar entre 1 y 3999.")
    numero = int(input("Reingresa tu número: "))



romano=decimal_a_romano(numero)
print("En números romanos:" ,romano)