

def LePlusGrand(a:int, b:int)->int :  # :int      | permet de spécifier le type de données de donnée que l'on veut, ici des entier.
                                      # -->int    | speficie le type de donnée  souhaité à la fin de la fonction 
    if a > 0:
        return print(f"le plus grand est {a}")
    elif b > 0 :
        return f"le plus grand est {b}"
    else:
        return f"les deux sont égaux"
    
def Seuil(a:int, seuil=10):
    if a > seuil:
        return print("//Seuil dépassé ERREUR //")
    
def LIste(*args): # *args permet d'entrer autant d'agument que l'on veut, parfait pour une liste.
    liste = []
    for arg in args:
        liste.append(arg)
        
    return print(max(liste)) # max() est une fonction qui permet la de savoir le nombre le plus grand d'une liste.


def LIsteSeuil(*args, seuil=3): 
    liste = []
    for arg in args:
        if arg < seuil:
            liste.append(arg)
        
    return print(len(liste)) 


def dict(chaine:str, **kwargs) -> str:
    for key, value in kwargs.items():
        print (f"{chaine} {key} : {value}")

#a = int(input("A = "))
#b = int(input("B = "))

#Seuil(a, 25)
#LIsteSeuil(1,1,1,1,3,4,5, seuil=1)

dict("salut" , nom="tonperere", age=30)