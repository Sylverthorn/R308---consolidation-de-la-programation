

class Joueur():
    def __init__(self, nom, liste):







class Personnage():
    def __init__(self, pseudo :str, niveau :float = 1, PV :float = 1, initiative :float = 1):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__PV = PV 
        self.__initiative = initiative
        

        if niveau > 1:
            self.__initiative = niveau



    def __attaque(self, autre_perso: 'Personnage'):
        if self.__initiative - autre_perso.__initiative < 0 :
            self.__PV -= autre_perso.degat()
            print(f"{autre_perso.__pseudo} attaque en premier ! {self.__pseudo} perd {autre_perso.degat()} points de vie.")
            if self.__PV >= 0:
                autre_perso.__PV -= self.degat()
                print(f'{self.__pseudo} à riposté ! {autre_perso.__pseudo} perd {self.degat()} points de vie.')

        
        elif self.__initiative == autre_perso.__initiative:
            self.__PV -= autre_perso.degat()
            autre_perso.__PV -= self.degat()

            print(f"{self.__pseudo} perd {autre_perso.degat()} points de vie.")
            print(f"{autre_perso.__pseudo} perd {self.degat()} points de vie.")
        else: 
            autre_perso.__PV -= self.degat()
            print(f"{self.__pseudo} attaque en premier ! {autre_perso.__pseudo} perd {self.degat()} points de vie.")
            if self.__PV >= 0:
                self.__PV -= autre_perso.degat()
                print(f'{autre_perso.__pseudo} à riposté ! {self.__pseudo} perd {autre_perso.degat()} points de vie.')



        if self.__PV <= 0 and autre_perso.__PV <= 0:
            print(f"{self.__pseudo} et {autre_perso.__pseudo} sont morts au combat !")

        elif self.__PV <= 0:
            print(f"{self.__pseudo} est mort au combat ! {autre_perso.__pseudo} remporte la victoire !")

        elif autre_perso.__PV <= 0:
            print(f"{autre_perso.__pseudo} est mort au combat ! {self.__pseudo} remporte la victoire !")

        else:
            print(f"Le combat continue ! {self.__pseudo} a {self.__PV} points de vie restants.")
            print(f"{autre_perso.__pseudo} a {autre_perso.__PV} points de vie restants.")
            

    def combat(self, autre_perso):
        while self.__PV > 0 and autre_perso.__PV > 0:
            self.__attaque(autre_perso)

    def soin(self):
        self.__PV = self.__niveau
        print(f"PV de {self.__pseudo} restauré")


    def degat(self):
        self.__degat = self.__niveau
        return self.__degat


    def __str__(self):
        return (f"| Personnage: {self.__pseudo}\n"
                f"| Niveau: {self.__niveau}\n"
                f"| Points de vie (PV): {self.__PV}\n"
                f"| Initiative: {self.__initiative}\n")
    

    @property
    def PV(self):
        return self._Personnage__PV





class Gerrier(Personnage):
    def __init__(self, pseudo: str, niveau: float = 1, PV: float = 1, initiative: float = 1):
        super().__init__(pseudo, niveau, PV, initiative)
        self._Personnage__niveau = niveau * 8 + 4
        self._Personnage__initiative = niveau * 4 + 6

    def degat(self):
        self.__degat = self._Personnage__niveau * 2
        return self.__degat

    @property
    def PV(self):
        return self._Personnage__PV

    def __str__(self):
        return (f"| Personnage: {self._Personnage__pseudo}\n"
                f"| Classe : Gerrier\n"
                f"| Niveau: {self._Personnage__niveau}\n"
                f"| Points de vie (PV): {self._Personnage__PV}\n"
                f"| Initiative: {self._Personnage__initiative}\n")


class Mage(Personnage):
    def __init__(self, pseudo: str, niveau: float = 1, PV: float = 1, initiative: float = 1):
        # Appel du constructeur de la classe parent (Personnage)
        super().__init__(pseudo, niveau, PV, initiative)
        
        # Modification des PV et de l'initiative pour le mage
        self._Personnage__PV = niveau * 5 + 10
        self._Personnage__initiative = niveau * 6 + 4
        
        # Attribut spécifique au mage
        self.__mana = niveau * 5

    def degat(self):
        if self.__mana != 0:
            self.__degat = self._Personnage__niveau + 3
        else:
            self.__degat = self._Personnage__niveau
        return self.__degat

    def __str__(self):
        return (f"| Personnage: {self._Personnage__pseudo}\n"
                f"| Classe : Mage\n"
                f"| Niveau: {self._Personnage__niveau}\n"
                f"| Points de vie (PV): {self._Personnage__PV}\n"
                f"| Initiative: {self._Personnage__initiative}\n"
                f"| Mana: {self.__mana}\n"
                f"| Degat: {self.__degat}")

    @property
    def PV(self):
        return self._Personnage__PV
    
    



yanis = Gerrier('yanis', 30, 100)

adel = Mage('adel', 40 , 100)

adel.combat(yanis)

print(yanis)
print("----------------------------")
print(adel)
