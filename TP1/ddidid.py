import math

class Point:
    
    def __init__(self, x=0, y=0) -> None:
        self.__x = x  
        self.__y = y

    def distanceCoord(self) -> float :
        dist = math.sqrt(self.__x ** 2 + self.__y ** 2)
        return print(f"distance entre les coordonnées de po : {dist}")

    def distancePoint(self, camarade:"Point" )-> float: 
        dist = math.sqrt((camarade.__x - self.__x)** 2 + (camarade.__y - self.__y)** 2)
        return dist

    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    




class Cercle():
    def __init__(self, rayon : float, centre : Point = Point()):
        self.__rayon = rayon
        self.__centre = centre
    
    def diamètre(self):
        diam = self.__rayon * 2 
        return diam
    
    def perimetre(self):
        peri = 2 * 3,14 * self.__rayon
        return peri
    
    def surface(self):
        sur = 3,14 * (self.diamètre() ** 2 / 4)
        return print(f"la surface est : {sur}")
    
    def intersection(self, camarade: 'Cercle'):
        rayonadd = self.__rayon + camarade.__rayon
        if rayonadd > self.__centre.distancePoint(camarade.__centre):
            print("intersection entre les deux cercle !! ")
        else : 
            print("Aucune intersection entre les deux cercle  ")


    def faitpartie(self, camarade: 'Point'):
        if self.__rayon < self.__centre.distancePoint(camarade): 
            print("fait partie")
        else:
            print("ne fait pas partie")

class Rectangle():
    def __init__(self, pointini :"Point", longX :float = 1, longY :float = 1, pointhaut :Point = None):
        if pointhaut:
            self.__pointini = pointini
            

            if pointhaut.x - pointini.x < 0:
                self.__longX = ( pointhaut.x - pointini.x )*(-1)
                self.__longY = ( pointhaut.y - pointini.y )*(-1)
            else : 
                self.__longX = pointhaut.x - pointini.x
                self.__longY = pointhaut.y - pointini.y

        else : 
            self.__pointini = pointini
            self.__longX = longX
            self.__longY = longY

    def surface(self):
        surface = self.__longX * self.__longY
        return surface
        
    def perimetre(self):
        peri = self.__longX *2 + self.__longY *2
        return peri
    
     # Obtenir le point bas-gauche
    def get_bas_gauche(self) -> Point:
        return self.point_bas_gauche

    # Obtenir le point bas-droit
    def get_bas_droit(self) -> Point:
        return Point(self.pointini.x + self.__longX, self.pointini.y)

    # Obtenir le point haut-gauche
    def get_haut_gauche(self) -> Point:
        return Point(self.point_bas_gauche.x, self.point_bas_gauche.y + self.hauteur)

    # Obtenir le point haut-droit
    def get_haut_droit(self) -> Point:
        return Point(self.point_bas_gauche.x + self.longueur, self.point_bas_gauche.y + self.hauteur)

        
    
        
    
    

    

    


def main():
    print("---test de la classe point---")
 
    p1 = Point()
    print(f"objet p1 : ({p1.x}, {p1.y})")
    p2 = Point(5, 5)
    print(f"objet p2 : ({p2.x}, {p2.y})")
    po = Point(13, 12)
    print(f"objet po : ({po.x}, {po.y})")


    print("-----------------")
    
    po.distanceCoord()
    print("-----------------")
    po.distancePoint(p2)
    print("-----------------")
    print("-----------------")

    c1 = Cercle(5, p1)
    c1.diamètre()
    c1.perimetre()
    c1.surface()
    print("-----------------")
    C2 = Cercle(3, p2)
    print("-----------------")
    c1.intersection(C2)
    print("-----------------")
    c1.faitpartie(p1)




    
if __name__ == "__main__":
    main()










