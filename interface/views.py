import csv
import os
from django.conf import settings
from django.shortcuts import render

# Create your views here.
def view_table(request):

    custom_keys = ['index', 'value'] 
    data = []
    csv_path = os.path.join(settings.BASE_DIR, 'static', 'csv', 'Table_Input.csv')
    with open(csv_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            row_dict = {custom_keys[i]: row[i] for i in range(len(custom_keys))}
            data.append(row_dict)

    target_indexes = ['A5', 'A20', 'A15', 'A7', 'A13', 'A12']

    matched_rows = {}
    for idx in target_indexes:
        matched_rows[idx] = next((row for row in data if row['index'] == idx), None)

    val_A5 = int(matched_rows['A5']['value'])
    val_A20 = int(matched_rows['A20']['value'])
    val_A15 = int(matched_rows['A15']['value'])
    val_A7 = int(matched_rows['A7']['value'])
    val_A13 = int(matched_rows['A13']['value'])
    val_A12 = int(matched_rows['A12']['value'])

    alpha = val_A5 + val_A20
    beta = val_A15/val_A7
    charlie = val_A13*val_A12
    return render(request, "index.html", {
        'headers': headers, 
        'rows': data,
        'alpha':int(alpha),
        'beta':int(beta),
        'charlie':int(charlie)
        })