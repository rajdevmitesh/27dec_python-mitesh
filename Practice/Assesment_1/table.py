def create_table():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    table = []

    for i in range(rows):
        row = []
        for j in range(cols):
            value = input(f"Enter value for cell ({i+1}, {j+1}): ")
            row.append(value)
        table.append(row)

    print("\nGenerated Table:")
    for row in table:
        print("\t".join(row))

if __name__ == "__main__":
    create_table()