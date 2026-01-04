import csv #adds a way to interact with comma seperated values
import os #adds a way to interact with an operating system (it can run window mac linux etc)
from auth import set_password, check_password, delete_password

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)  # Makes sure the folder for CSV files exists

class Spreadsheet:
    #initialization!
    def __init__(self, name, headers=None, data=None):
        # Create a new spreadsheet object
        # headers: list of column names
        # data: list of rows (each row is a list of values)
        self.name = name
        self.headers = headers or ["#"]
        self.data = data or []
        self._normalize()

    # file
    @staticmethod
    def exists(name):
     # Check if a spreadsheet file exists
        
        return os.path.exists(f"{DATA_DIR}/{name}.csv")

    @staticmethod
    def create(name, password):
        # Create a new spreadsheet file with a password

        if Spreadsheet.exists(name):
            raise Exception("Spreadsheet already exists.")
        set_password(name, password)
        sheet = Spreadsheet(name)
        sheet.save()    # Saves the empty spreadsheet to CSV
        return sheet

    @staticmethod
    def load(name, password):  # Load a spreadsheet from a CSV file if the password matches
        if not Spreadsheet.exists(name):
            raise Exception("Spreadsheet not found.")
        if not check_password(name, password):
            raise Exception("Wrong password.")

        with open(f"{DATA_DIR}/{name}.csv") as f:
            rows = list(csv.reader(f))

        headers = rows[0]     # Convert integer cells to floats and leaves empty strings as "" (nothing in string form)
        data = [[float(x) if x else "" for x in row] for row in rows[1:]]
        return Spreadsheet(name, headers, data)

    def save(self):
        # Save the current spreadsheet data to a CSV file
        self._update_index() # Make sure the index column is correct
        self._normalize()   # Make sure all rows match header length so that it looks normal
        with open(f"{DATA_DIR}/{self.name}.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)
            writer.writerows(self.data)

    @staticmethod
    def delete(name):# Delete a spreadsheet file and its password
        os.remove(f"{DATA_DIR}/{name}.csv")
        delete_password(name)

    # core helpers
    def _normalize(self):  # Ensure every row has the same number of columns as the header
        for row in self.data:
            while len(row) < len(self.headers):
                row.append("")
            while len(row) > len(self.headers):
                row.pop()

    def _update_index(self): 
        # Make the first column show row numbers (1, 2, 3, …) automatically
    # so the numbers are always correct even if rows are added or deleted
        for i, row in enumerate(self.data):
            if len(row) == 0:
                row.append(i + 1)
            else:
                row[0] = i + 1

    # data
    def add_column(self, title, values): # Add a new column to the spreadsheet with the given title and list of values
        self.headers.append(title)
        self._normalize() # Make sure all existing rows have space for the new column

        for i, v in enumerate(values):  # If there aren't enough rows yet, add new ones
            if i >= len(self.data):
                self.data.append([i + 1] + [""] * (len(self.headers) - 1))
            self.data[i][-1] = v # Set the new value in the last column

        self._update_index()
        self._normalize()

    def append_to_column(self, col, values):
    # Add values to a specific column, creating new rows as needed
        if col <= 0 or col >= len(self.headers):
            raise Exception("Invalid column index.")

        for v in values:
        # Create a new row with empty cells and add the value to the specified column
            new_row = [len(self.data) + 1] + [""] * (len(self.headers) - 1)
            new_row[col] = v
            self.data.append(new_row)

        self._update_index()
        self._normalize()

    def edit_cell(self, row, col, value):
    # Change the value of a single cell (row, col)
        if col <= 0:
            raise Exception("Cannot edit index column.")

        # If the row doesn't exist yet, add new rows

        while row >= len(self.data):
            self.data.append([len(self.data) + 1] + [""] * (len(self.headers) - 1))

        self.data[row][col] = value
        self._update_index()
        self._normalize()

    # delete
    def delete_column(self, col):
     # Remove a column from the spreadsheet (cannot delete the index column)
        if col == 0:
            raise Exception("Cannot delete index column.")
        if col < 0 or col >= len(self.headers):
            raise Exception("Invalid column index.")

        self.headers.pop(col)
        for row in self.data:
            row.pop(col)

        self._normalize()

    def delete_row(self, row):
         # Remove a row from the spreadsheet
        if row < 0 or row >= len(self.data):
            raise Exception("Invalid row index.")

        self.data.pop(row)
        self._update_index()
        self._normalize()

    # display
    def display(self):
       # Print the spreadsheet in a table-like format

        widths = []
        for i, h in enumerate(self.headers):
            w = len(h)
            for r in self.data:
                w = max(w, len(str(r[i])))
            widths.append(w + 2)
        # Print header row
        header_line = "".join(self.headers[i].ljust(widths[i]) for i in range(len(self.headers)))
        print("\n" + header_line)
        print("-" * sum(widths))

        for r in self.data:
            print("".join(str(r[i]).ljust(widths[i]) for i in range(len(self.headers))))
