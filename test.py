import csv
import json

inp = input()

if inp == "0":
    with open('enfermedades.csv', 'r') as csvfile:
        data = {}
        reader = csv.reader(csvfile)
        next(reader)  # Saltar el encabezado si existe
        
        for row in reader:
            if 7 <= reader.line_num <= 27:
                data[row[1]] = {}
                data[row[1]]["sitomas"] = row[2] #Columna B (índice 1)
                data[row[1]]["prevencion"] = row[3] #Columna C (índice 2)
                data[row[1]]["tratamiento"] = row[4] #Columna D (índice 3)
        
        print(json.dumps(data, indent=3))

    