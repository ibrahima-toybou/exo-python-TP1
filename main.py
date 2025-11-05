nom_boutique  = str("ChossettZ")
produit : str = "Chaussures"
prix_unitaire = float (5.99)
quantite_stock : int = 20
tva : float = 0.20
compte_client  = float(100)
compte_boutique : float = 0

print(f"La boutique {nom_boutique} vend des {produit} au prix de {prix_unitaire}€ "
      f"l'unité (TVA : {tva*100}%). Il reste {quantite_stock} articles en stock. "
      f"Le compte du client est de {compte_client}€ et celui de la boutique est de {compte_boutique}€.")

prix_ht = round(prix_unitaire, 2)
prix_ttc = round(prix_ht * (1 + tva), 2)
print(f"Le prix hors taxe est de {prix_ht}€ et le prix toutes taxes comprises est de {prix_ttc}€.")

nb_paires = int(input("Combien de paires de chaussures souhaitez-vous acheter ? "))
