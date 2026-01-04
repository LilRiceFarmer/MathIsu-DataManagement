from spreadsheet import Spreadsheet
from stats import column_stats
from graphs import scatter_with_correlation

def sheet_menu(sheet):
     # Menu for working with a single spreadsheet
    # Lets the user view, edit, add, or delete columns/rows, do stats, or make plots
    while True:
        print(f"\n--- Spreadsheet: {sheet.name} ---")
        print("0. Show column indexes")
        print("1. Add new column")
        print("2. Add values to column")
        print("3. Edit single cell")
        print("4. Delete column")
        print("5. Delete row")
        print("6. View spreadsheet")
        print("7. Column statistics")
        print("8. Scatter plot")
        print("9. Save & return")

        choice = input("Choose: ")

        try:
            if choice == "0":
                print("\nColumn indexes:")
                for i, h in enumerate(sheet.headers):
                    print(f"{i}: {h}")

            elif choice == "1":
                title = input("Column title: ")
                values = [float(x) for x in input("Values: ").split(",")]
                sheet.add_column(title, values)
                print("Column added.")

            elif choice == "2":
                col = int(input("Column index: "))
                values = [float(x) for x in input("Values to Add: ").split(",")]
                sheet.append_to_column(col, values)
                print("Values Added.")

            elif choice == "3":
                row = int(input("Row index (starting at 0): "))
                col = int(input("Column index: "))
                value = float(input("New value: "))
                sheet.edit_cell(row, col, value)
                print("Cell updated.")

            elif choice == "4":
                col = int(input("Column index to delete: "))
                confirm = input("Type DELETE to confirm: ")
                if confirm == "DELETE":
                    sheet.delete_column(col)
                    print("Column deleted.")

            elif choice == "5":
                row = int(input("Row index to delete: "))
                confirm = input("Type DELETE to confirm: ")
                if confirm == "DELETE":
                    sheet.delete_row(row)
                    print("Row deleted.")

            elif choice == "6":
                sheet.display()

            elif choice == "7":
                col = int(input("Column index: "))
                print(column_stats(sheet, col))

            elif choice == "8":
                x = int(input("X column index: "))
                y = int(input("Y column index: "))
                scatter_with_correlation(sheet, x, y)

            elif choice == "9":
                sheet.save()
                print("Saved.")
                return

            else:
                print("Invalid option.")

        except Exception as e:
            print("Error:", e)
            input("Press Enter to continue...")

def main():
    while True:
        print("\n=== Spreadsheet App ===")
        print("1. Create spreadsheet")
        print("2. Load spreadsheet")
        print("3. Delete spreadsheet")
        print("4. Exit")

        choice = input("Choose: ")

        try:
            if choice == "1":
                Spreadsheet.create(input("Name: "), input("Password: "))
                print("Created.")

            elif choice == "2":
                sheet = Spreadsheet.load(input("Name: "), input("Password: "))
                sheet_menu(sheet)

            elif choice == "3":
                name = input("Name: ")
                confirm = input("Type DELETE to confirm: ")
                if confirm == "DELETE":
                    Spreadsheet.delete(name)
                    print("Spreadsheet deleted.")

            elif choice == "4":
                break

            else:
                print("Invalid option.")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
