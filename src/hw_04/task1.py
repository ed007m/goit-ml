from typing import Tuple


def total_salary(file_path: str) -> Tuple[float, float]:
    total = 0.0
    count = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    name, salary = line.split(',')
                    total += float(salary)
                    count += 1
                except ValueError:
                    continue

        average = total / count if count > 0 else 0.0
        return total, average

    except FileNotFoundError:
        return 0.0, 0.0
    except Exception:
        return 0.0, 0.0