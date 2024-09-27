


class Velo:
    def __init__(self, couleur:str, marque:str, pneu:int ,nbrvitesse=8, vitesse=1):
        self.couleur = couleur
        self.marque = marque
        self.pneutaille = pneu
        self.nbrVItesse = nbrvitesse

        self.vitessecourante = vitesse
        

    
    def gear_up(self):
        if self.vitessecourante < self.nbrVItesse:
            self.vitessecourante += 1
            print(f"vitesse + 1 : {self.vitessecourante}")
        else:
            print(f" vitesse max deja atteinte : {self.vitessecourante}")

    def gear_down(self):
        if self.vitessecourante > 1:
            self.vitessecourante -= 1
            print(f"vitesse - 1 : {self.vitessecourante}")
        else:
            print(f" vitesse min deja atteinte : : {self.vitessecourante}")


if __name__ == "__main__":

    velo1 = Velo("bleu", "renault", 10)

    velo1.gear_up()

    velo1.gear_down()
