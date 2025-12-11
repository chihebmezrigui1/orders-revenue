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
```

1. Lancer le script main :
```bash
python main.py --input orders.json
```

2. filtrer par date : seules les commandes dont created_at >= YYYY-MM-DD sont considérées :
```bash
python main.py --input orders.json --from 2024-11-01
```
3. Pour lancer les tests unitaires
```bash
python -m unittest discover tests
```
---

## Questions

1. Si ce programme tournait en production, que surveiller / logger ? : 
- Erreurs de parsing JSON (lignes invalides)
- Commandes suspectes (montants négatifs, marketplaces vides)
- Nombre de commandes traitées et temps de traitement

2. Si le fichier passait de 10 Ko → 10 Go, que changerais-tu ?
- Lecture en streaming
- Ne pas stocker toutes les commandes en mémoire : calculer les totaux et revenus à la volée
- Considérer batch processing ou parallélisation si nécessaire

3. Quel est le cas de test prioritaire et pourquoi ?
- Commandes suspectes : montants négatifs ou marketplaces vides
- Pourquoi : elles impactent directement le calcul du revenu et le reporting ; détecter ces cas est critique pour la fiabilité des chiffres


