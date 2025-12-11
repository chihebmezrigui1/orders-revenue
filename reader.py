from typing import Dict, List
import json


def read_orders(file_path: str) -> List[Dict]:
   # Lire un fichier ligne par ligne et retourner les objets JSON valides.

    orders: List[Dict] = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            raw = line.strip()
            if not raw:
                continue

            try:
                obj = json.loads(raw)
                orders.append(obj)
            except json.JSONDecodeError as e:
                print(f"[WARN] Ligne {line_num}: JSON invalide -> {e}")

    return orders