from spreadsheet import Spreadsheet
from stats import column_stats, column_box_stats
from graphs import scatter_with_correlation, box_plot_column

def sheet_menu(sheet):
    while True:
        print(f"\n--- Spreadsheet: {sheet.name} ---")
        print("0. Show column indexes")
        print("1. Add new column")
        print("2. Add values to column")
        print("3. Edit single cell")
        print("4. Delete column")
        print("5. Delete row")
        print("6. View spreadsheet")
        print("7. Column statistics (mean/median/mode)")
        print("8. Scatter plot")
        print("9. Box plot + quartile stats")
        print("10. Save & return")

        choice = input("Choose: ")

        try:
            if choice == "0":
                for i, h in enumerate(sheet.headers):
                    print(f"{i}: {h}")

            elif choice == "1":
                title = input("Column title: ")
                values = [float(x) for x in input("Values: ").split(",")]
                sheet.add_column(title, values)

            elif choice == "2":
                col = int(input("Column index: "))
                values = [float(x) for x in input("Values to add: ").split(",")]
                sheet.append_to_column(col, values)

            elif choice == "3":
                row = int(input("Row index (starting at 0): "))
                col = int(input("Column index: "))
                value = float(input("New value: "))
                sheet.edit_cell(row, col, value)

            elif choice == "4":
                col = int(input("Column index to delete: "))
                if input("Type DELETE to confirm: ") == "DELETE":
                    sheet.delete_column(col)

            elif choice == "5":
                row = int(input("Row index to delete: "))
                if input("Type DELETE to confirm: ") == "DELETE":
                    sheet.delete_row(row)

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
                col = int(input("Column index: "))
                stats = column_box_stats(sheet, col)
                for k, v in stats.items():
                    print(f"{k}: {v}")
                box_plot_column(sheet, col)

            elif choice == "10":
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
                if input("Type DELETE to confirm: ") == "DELETE":
                    Spreadsheet.delete(name)
                    print("Deleted.")

            elif choice == "4":
                break

            else:
                print("Invalid option.")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
