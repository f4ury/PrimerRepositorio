frutas = {"manzana":"con un precio de $50","pera":"con un precio de $25","mango":"con un precio de $45","sandia":"con un precio de $100","melon":"con un precio de $80"}
p_fruta = input("Que fruta le gustaria comprar: ")
a_comprar = int(input("Cuantas le gustaria comprar: "))

if p_fruta == "manzana":
   resultado = 50 * a_comprar
   print (f"la fruta que a comprado es {p_fruta}, la cantidad que usted quiere de la fruta es {a_comprar} haciendo un total de {resultado}")
elif p_fruta == "pera":
    resultado = 25 * a_comprar
    print (f"la fruta que a comprado es {p_fruta}, la cantidad que usted quiere de la fruta es {a_comprar} haciendo un total de {resultado}")
elif p_fruta == "mango":
    resultado = 45 * a_comprar
    print (f"la fruta que a comprado es {p_fruta}, la cantidad que usted quiere de la fruta es {a_comprar} haciendo un total de {resultado}")
elif p_fruta == "sandia":
   resultado = 100 * a_comprar
   print (f"la fruta que a comprado es {p_fruta}, la cantidad que usted quiere de la fruta es {a_comprar} haciendo un total de {resultado}")
elif p_fruta == "melon":
    resultado = 80 * a_comprar
    print (f"la fruta que a comprado es {p_fruta}, la cantidad que usted quiere de la fruta es {a_comprar} haciendo un total de {resultado}")
else:
    print("Lo sentimos no tenemos de la fruta que usted busca.")
 
 