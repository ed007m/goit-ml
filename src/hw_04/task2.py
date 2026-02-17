from typing import List, Dict


def get_cats_info(file_path: str) -> List[Dict[str, str]]:
    cats = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    cat_id, name, age = line.split(',')
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    continue

        return cats

    except FileNotFoundError:
        return []
    except Exception:
        return []