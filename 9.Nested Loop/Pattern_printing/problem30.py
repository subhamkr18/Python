def tax_calculator(income: float) -> float:
    if income < 0:
        raise ValueError("Income cannot be negative.")

    tax = 0.0

    if income > 250_000:
        taxable_slab_2 = min(income, 500_000) - 250_000
        tax += taxable_slab_2 * 0.05

    if income > 500_000:
        taxable_slab_3 = min(income, 1_000_000) - 500_000
        tax += taxable_slab_3 * 0.20

    if income > 1_00_000:
        taxable_slab_4 = income - 1_000_000
        tax += taxable_slab_4 * 0.30

    return round(tax, 2)


if __name__ == "__main__":
    print(tax_calculator(200_000))
    print(tax_calculator(400_000))
    print(tax_calculator(750_000))
    print(tax_calculator(1_200_000))