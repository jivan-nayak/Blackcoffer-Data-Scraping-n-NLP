import openpyxl


def write_to_excel(file_path, data):
    # Open the Excel file
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    # Write data to corresponding columns for each row
    for i, row_data in enumerate(data):
        print(i)
        row_num = i + 10
        for j, cell_data in enumerate(row_data):
            print(j)
            col_num = j + 10
            cell = ws.cell(row=row_num, column=col_num)
            cell.value = cell_data
    # Save the changes to the Excel file
    wb.save(file_path)

# Example usage:
file_path = "F:/Python projects LoL/Data-Extraction-Trial/utils/example.xlsx"
data = [
    ["John", "Doe", 25],

]
write_to_excel(file_path, data)
