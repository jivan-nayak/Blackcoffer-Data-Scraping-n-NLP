import openpyxl


def write_to_excel(file_path, data, i):
    # Open the Excel file
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

    # Write data to corresponding columns for each row
    row_num = i + 2
    for j, cell_data in enumerate(data):
        col_num = j + 3
        cell = ws.cell(row=row_num, column=col_num)
        cell.value = cell_data
    # Save the changes to the Excel file
    wb.save(file_path)
