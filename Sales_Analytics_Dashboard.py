
import numpy as np


# 1. COLLECT THE DATASET

def create_dataset():
    print("\n========== SALES DATASET ==========")
 
        # Sample data
    product_ids = np.array(
            ["P101", "P102", "P103", "P104", "P105",
             "P106", "P107", "P108"]
        )

    monthly_sales = np.array(
            [120, 200, 150, 90, 250, 180, 75, 220],
            dtype=float
        )

    selling_prices = np.array(
            [50, 30, 40, 80, 25, 35, 100, 45],
            dtype=float
        )

    total_costs = np.array(
            [4000, 4500, 4500, 5000, 4000, 4500, 5500, 6500],
            dtype=float
        )

    # 2. ARITHMETIC OPERATIONS

    # Multiplication: sales units x selling price
    revenue = monthly_sales * selling_prices

    # Subtraction: revenue - total cost
    profit = revenue - total_costs

    return product_ids, monthly_sales, revenue, profit


# 3. DISPLAY THE DATASET

def display_dataset(product_ids, monthly_sales, revenue, profit):
    print("\n========== PRODUCT DATASET ==========")

    print(
        f"{'Product ID':<12}"
        f"{'Sales':>10}"
        f"{'Revenue':>15}"
        f"{'Profit':>15}"
    )


    for i in range(len(product_ids)):
        print(
            f"{product_ids[i]:<12}"
            f"{monthly_sales[i]:>10.0f}"
            f"{revenue[i]:>15.2f}"
            f"{profit[i]:>15.2f}"
        )


# 4. CALCULATE STATISTICS

def calculate_statistics(product_ids, monthly_sales, revenue, profit):

    # Revenue statistics
    total_revenue = np.sum(revenue)
    average_revenue = np.mean(revenue)
    median_revenue = np.median(revenue)
    minimum_revenue = np.min(revenue)
    maximum_revenue = np.max(revenue)

    # Sales statistics
    highest_sales = np.max(monthly_sales)
    lowest_sales = np.min(monthly_sales)

    # Revenue variation
    revenue_variance = np.var(revenue)
    revenue_std = np.std(revenue)

    # Profit percentage (profit margin)
    if total_revenue != 0:
        profit_percentage = (np.sum(profit) / total_revenue) * 100
    else:
        profit_percentage = 0

    # Best and worst products by units sold
    best_index = np.argmax(monthly_sales)
    worst_index = np.argmin(monthly_sales)

    # Addition and division demonstration
    total_sales = np.sum(monthly_sales)
    number_of_products = len(product_ids)

    average_sales = total_sales / number_of_products

    # Return all calculated results
    return {
        "total_revenue": total_revenue,
        "average_revenue": average_revenue,
        "median_revenue": median_revenue,
        "minimum_revenue": minimum_revenue,
        "maximum_revenue": maximum_revenue,
        "highest_sales": highest_sales,
        "lowest_sales": lowest_sales,
        "revenue_variance": revenue_variance,
        "revenue_std": revenue_std,
        "profit_percentage": profit_percentage,
        "total_profit": np.sum(profit),
        "total_sales": total_sales,
        "average_sales": average_sales,
        "best_product": product_ids[best_index],
        "worst_product": product_ids[worst_index],
    }


# 5. DISPLAY THE ANALYTICS DASHBOARD

def display_statistics(stats):
    print("\n========== SALES ANALYTICS DASHBOARD ==========")

    print(f"Total Revenue       : {stats['total_revenue']:.2f}")
    print(f"Average Revenue     : {stats['average_revenue']:.2f}")
    print(f"Median Revenue      : {stats['median_revenue']:.2f}")
    print(f"Highest Revenue     : {stats['maximum_revenue']:.2f}")
    print(f"Lowest Revenue      : {stats['minimum_revenue']:.2f}")

    print(f"\nTotal Profit        : {stats['total_profit']:.2f}")
    print(f"Profit Percentage   : {stats['profit_percentage']:.2f}%")

    print(f"\nHighest Sales       : {stats['highest_sales']:.0f} units")
    print(f"Lowest Sales        : {stats['lowest_sales']:.0f} units")
    print(f"Total Units Sold    : {stats['total_sales']:.0f}")
    print(f"Average Units Sold  : {stats['average_sales']:.2f}")

    print(f"\nRevenue Variance    : {stats['revenue_variance']:.2f}")
    print(f"Revenue Std Dev     : {stats['revenue_std']:.2f}")

    print(f"\nBest-Selling Product : {stats['best_product']}")
    print(f"Worst-Selling Product: {stats['worst_product']}")


# 6. DISPLAY TOP 5 PRODUCTS BY REVENUE

def display_top_products(product_ids, revenue, profit):
    print("\n========== TOP 5 PRODUCTS BY REVENUE ==========")

    # argsort sorts values in ascending order.
    # [::-1] reverses the order to descending.
    sorted_indices = np.argsort(revenue)[::-1]

    # Select at most five products
    top_indices = sorted_indices[:5]

    print(
        f"{'Rank':<8}"
        f"{'Product ID':<15}"
        f"{'Revenue':>15}"
        f"{'Profit':>15}"
    )

    print("-" * 53)

    for rank, index in enumerate(top_indices, start=1):
        print(
            f"{rank:<8}"
            f"{product_ids[index]:<15}"
            f"{revenue[index]:>15.2f}"
            f"{profit[index]:>15.2f}"
        )


# 7. MAIN FUNCTION

def main():
    print("=" * 45)
    print("     SALES ANALYTICS DASHBOARD")
    print("          Powered by NumPy")
    print("=" * 45)

    dataset = create_dataset()

    if dataset is None:
        print("Dataset creation failed. Please run the program again.")
        return

    product_ids, monthly_sales, revenue, profit = dataset

    if len(product_ids) == 0:
        print("The dataset is empty.")
        return

    display_dataset(product_ids, monthly_sales, revenue, profit)

    stats = calculate_statistics(
        product_ids, monthly_sales, revenue, profit
    )

    display_statistics(stats)

    display_top_products(product_ids, revenue, profit)

    print("\nAnalysis completed successfully!")


# 8. RUN THE PROGRAM

if __name__ == "__main__":
    main()
