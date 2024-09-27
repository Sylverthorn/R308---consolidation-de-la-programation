


class Tasse:
    # Attribut de classe
    matière:str = "céramique"

# Méthode d'initialisation avec les attributs d'instance
    def __init__(self, couleur:str, contenance:float, marque:str):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque
        self.contenu = None # Initialisation sans contenu par défaut


# Méthode __str__ pour une représentation formatée
    def __str__(self) -> str:
        if self.contenu is None :
            contenu:str = ""
        else:
            contenu:str = " de " + self.contenu # Verifier si la tasse est vide ou non pour l'afficher ou non
        return f"""la tasse de matière {self.matière}, de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} mL{contenu}."""


# Méthode pour définir le contenu de la tasse
    def remplir(self, boisson):
        if self.contenu is None:
            self.contenu = boisson
            print(f" tasse rempli avec {boisson}.")
        else:
            print(f"la tasse est déjà rempli.")

# Méthode pour éliminer le contenu de la tasse
    def boire(self):
        if self.contenu is not None:
            print(f"vous avez bu le {self.contenu}.")
            del self.contenu
        else :
            print(f"la tasse est vide.")

# Création de plusieurs objets Tasse
tasse1 = Tasse("bleu", 100, "Hilt")
tasse2 = Tasse("rouge", 50, "lidl")


# Affichage des informations sur les tasses
print(tasse1)
print(tasse2)


# Boire le contenu de la tasses1 normalement vide
tasse1.boire()

# Remplir la tasse1 avec une boisson
tasse1.remplir("coca")
print(tasse1)

# Essayer de boire à nouveau
tasse1.boire()


            
        
