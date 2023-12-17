import csv
import json

inp = input()

if inp == "0":
    with open('enfermedades.csv', 'r') as csvfile:
        data = {}
        reader = csv.reader(csvfile)
        next(reader)  # Saltar el encabezado si existe
        
        for row in reader:
            if 31 <= reader.line_num <= 58:
                data[row[1]] = {}
                data[row[1]]["funcionamiento"] = row[2] #Columna B (índice 1)
                data[row[1]]["eficacia"] = row[3] #Columna C (índice 2)
                data[row[1]]["cambios_en_la_regla"] = row[4] #Columna D (índice 3)
                data[row[1]]["como_se_utiliza"] = row[5] #Columna D (índice 3)
                data[row[1]]["mal_uso_o_rotura"] = row[6] #Columna D (índice 3)
                data[row[1]]["tiempo_en_fertilidad"] = row[7] #Columna D (índice 3)
                data[row[1]]["cuando_no_utilizarlo"] = row[8] #Columna D (índice 3)
                data[row[1]]["efectos_negativos_de_uso"] = row[9] #Columna D (índice 3)
                data[row[1]]["ventajas"] = row[10] #Columna D (índice 3)
                data[row[1]]["inconvenientes"] = row[11] #Columna D (índice 3)
                data[row[1]]["precio"] = row[12] #Columna D (índice 3)
        
        print(json.dumps(data, indent=3))

    