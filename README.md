# Orders Revenue

Ce projet lit un fichier `orders.json` (1 JSON par ligne) et calcule : 
- le revenu total en euros,
- le revenu par marketplace (tri décroissant),
- les commandes suspectes (montants négatifs ou marketplace vide).

Le code est modulaire, testable : Il inclut un filtre optionnel par date et des tests unitaires.

---

## Contenu du dépôt

- `reader.py` : lecture et parsing des commandes
- `compute.py` : calcul du revenu total et par marketplace
- `report.py` : identification des commandes suspectes et affichage
- `main.py` : point d’entrée CLI
- `orders.json` : fichier d’exemple
- `tests/` : tests unitaires (test_compute & test_report)

---

## Instructions pour lancer

1. Cloner le dépôt :

```bash
git clone https://github.com/chihebmezrigui1/orders-revenue.git
cd orders-revenue
