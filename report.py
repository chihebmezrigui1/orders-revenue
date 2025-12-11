from typing import Dict, List


def find_suspicious_orders(orders: List[Dict]) -> List[str]:
    suspects: List[str] = []

    for o in orders:
        oid = str(o.get("id", "<unknown id>"))
        reasons: List[str] = []

        # montant négatif ou invalide
        try:
            amount = int(o.get("amount_cents", 0))
            if amount < 0:
                reasons.append(f"negative amount ({amount})")
        except Exception:
            reasons.append(f"invalid amount ({o.get('amount_cents')})")

        # marketplace vide ou manquante
        mp = o.get("marketplace")
        if mp is None or not str(mp).strip():
            reasons.append("empty marketplace")

        if reasons:
            suspects.append(f"- {oid}: {', '.join(reasons)}")

    return suspects


def print_report(total_eur: float, by_mp: Dict[str, float], suspects: List[str]) -> None:
    """
    Affiche le rapport final :
      - total revenue
      - revenue by marketplace (tri décroissant)
      - suspicious orders
    """
    # Total
    print(f"Total revenue: {total_eur:.2f} EUR\n")

    # Par marketplace, tri décroissant
    if by_mp:
        print("Revenue by marketplace:")
        sorted_mp = sorted(by_mp.items(), key=lambda kv: kv[1], reverse=True)
        for mp, eur in sorted_mp:
            print(f"- {mp}: {eur:.2f} EUR")
    else:
        print("Revenue by marketplace: (none)")

    print()

    # Commandes suspectes
    if suspects:
        print("Suspicious orders:")
        for s in suspects:
            print(s)
    else:
        print("Suspicious orders: (none)")
