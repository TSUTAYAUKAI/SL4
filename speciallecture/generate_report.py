def generate_report(data):
    # データの集計
    total_customers, total_sales = aggregate_totals(data)

    # データの平均計算
    average_customers, average_sales = compute_averages(data, total_customers, total_sales)

    # レポート生成
    report = build_report(average_customers, average_sales, total_customers, total_sales)

    return report


def build_report(average_customers, average_sales, total_customers, total_sales):
    report = f"Total Sales: {total_sales}\n"
    report += f"Total Customers: {total_customers}\n"
    report += f"Average Sales per Day: {average_sales:.2f}\n"
    report += f"Average Customers per Day: {average_customers:.2f}\n"
    return report


def compute_averages(data, total_customers, total_sales):
    average_sales = total_sales / len(data)
    average_customers = total_customers / len(data)
    return average_customers, average_sales


def aggregate_totals(data):
    total_sales = 0
    total_customers = 0
    for record in data:
        total_sales += record['sales']
        total_customers += record['customers']
    return total_customers, total_sales


data = [
    {"sales": 100, "customers": 10},
    {"sales": 150, "customers": 20},
    {"sales": 200, "customers": 15},
]

print(generate_report(data))