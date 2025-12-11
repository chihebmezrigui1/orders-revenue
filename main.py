import argparse
from datetime import datetime
from reader import read_orders
from compute import compute_total_revenue_eur, revenue_by_marketplace
from report import find_suspicious_orders, print_report


def main():
    parser = argparse.ArgumentParser(description="Lecture de commandes et calcul du revenu.")
    parser.add_argument("--input", required=True, help="Chemin vers le fichier orders.json")
    parser.add_argument("--from", dest="from_date", required=False,
                        help="Filtre sur la date (YYYY-MM-DD) : seules les commandes >= date")
    args = parser.parse_args()

    orders = read_orders(args.input)

    # Filtrage optionnel par date
    if args.from_date:
        try:
            dt_from = datetime.strptime(args.from_date, "%Y-%m-%d")
            filtered_orders = []
            for o in orders:
                created_at = o.get("created_at")
                if created_at:
                    try:
                        dt = datetime.strptime(created_at[:10], "%Y-%m-%d")
                        if dt >= dt_from:
                            filtered_orders.append(o)
                    except Exception:
                        # Si date invalide, on ignore la commande pour le filtre
                        pass
            orders = filtered_orders
        except ValueError:
            print(f"Date '-from' invalide : {args.from_date}. Aucun filtrage appliqué.")

    print(f"{len(orders)} commandes lues avec succès.\n")

    total = compute_total_revenue_eur(orders)
    by_mp = revenue_by_marketplace(orders)
    suspects = find_suspicious_orders(orders)

    print_report(total, by_mp, suspects)


if __name__ == "__main__":
    main()
