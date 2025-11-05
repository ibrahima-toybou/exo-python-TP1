def calcul_ht(prix, quantite):
    return (prix * quantite)

def calcul_ttc(prix_ht, tva):
    return prix_ht * (1 + tva)

def arrondir(valeur):
    return round(valeur, 2)

def afficher_facture(nom_boutique, produit, qte, ht, ttc):
    print("-"*50)
    print(nom_boutique)
    print("-"*50)
    print(f"Produit                           qté           ht")
    print(f"{produit} ....................  {qte}          {arrondir(ht)}")
    print(f"                           Total HT :         {arrondir(ht)}")
    print(f"                                TVA :         {arrondir(ttc - ht)}")
    print(f"                          Total TTC :         {arrondir(ttc)}")
    print("-"*50)
