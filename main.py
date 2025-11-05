from fonctions import calcul_ht, calcul_ttc, arrondir, afficher_facture

# Variables
nom_boutique = "ChossettZ"
produit = "chaussettes"
prix_unitaire = 5.99
quantite_stock = 20
tva = 0.20
compte_client = 100
compte_boutique = 0

def main():
    global quantite_stock, compte_client, compte_boutique

    print(f"Bienvenue chez {nom_boutique} !")
    print(f"Stock disponible : {quantite_stock} chaussettes, prix : {prix_unitaire}€")
    print(f"Votre compte : {compte_client}€")

    try:
        qte = int(input("Combien de paires voulez-vous acheter ? "))
        if qte <= 0 or qte > quantite_stock:
            print("Quantité invalide.")
            return
    except ValueError:
        print("Entrée invalide.")
        return

    ht = calcul_ht(prix_unitaire, qte)
    ttc = calcul_ttc(ht, tva)

    if compte_client >= ttc:
        compte_client -= ttc
        compte_boutique += ttc
        quantite_stock -= qte
        afficher_facture(nom_boutique, produit, qte, ht, ttc)
    else:
        print("Solde insuffisant.")

    if quantite_stock < 10:
        print("!! Stock bientôt épuisé !!")
    elif 10 < quantite_stock < 15 and prix_unitaire > 5:
        print("!! Attention produit presque en rupture !!")

    # Types des variables
    print("Types des variables :")
    print("nom_boutique :", type(nom_boutique))
    print("produit :", type(produit))
    print("prix_unitaire :", type(prix_unitaire))
    print("quantite_stock :", type(quantite_stock))
    print("tva :", type(tva))
    print("compte_client :", type(compte_client))
    print("compte_boutique :", type(compte_boutique))

if __name__ == "__main__":
    main()
