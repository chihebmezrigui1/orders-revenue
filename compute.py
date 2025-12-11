from typing import Dict, List
from collections import defaultdict


def compute_total_revenue_eur(orders: List[Dict]) -> float:
    #Somme des amount convertie en euros.

    total_cents = sum(int(o.get("amount_cents", 0)) for o in orders)
    return total_cents / 100.0


def revenue_by_marketplace(orders: List[Dict]) -> Dict[str, float]:
#    Retourne un dict marketplace -> revenu (euros) en ignorant les marketplaces vides.

    sums = defaultdict(int)

    for o in orders:
        mp = (o.get("marketplace") or "").strip()
        if not mp:
            continue

        try:
            cents = int(o.get("amount_cents", 0))
        except Exception:
            cents = 0

        sums[mp] += cents

    # Conversion en euros
    return {mp: total / 100.0 for mp, total in sums.items()}