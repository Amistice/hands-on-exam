from collections import defaultdict


def group_by_company(consultants: list) -> dict:
    grouped = defaultdict(list)
    for consultant in consultants:
        grouped[consultant['company']].append(consultant)
    return dict(grouped)


if __name__ == "__main__":
    consultants = [
        {'name': 'Peyton Turner',    'company': 'Walker Inc'},
        {'name': 'Isaias Fritsch',   'company': 'Walker Inc'},
        {'name': 'Susana Wilderman', 'company': 'Nolan Inc'},
    ]
    result = group_by_company(consultants)
    for company, members in result.items():
        print(f"{company}: {members}")