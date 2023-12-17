import csv
import json

inp = input()

if inp == "0":
    with open('questionari.csv', 'r') as csvfile:
        data = {}
        reader = csv.reader(csvfile)
        next(reader)  # Saltar el encabezado si existe
        
        for row in reader:
            data[row[0]] = {}
            data[row[0]]["question"] = row[1]
            data[row[0]]["answer1"] = row[2]
            data[row[0]]["answer2"] = row[3]
            data[row[0]]["answer3"] = row[4]
            data[row[0]]["answer4"] = row[5]
            data[row[0]]["correct"] = row[6]

    json_data = json.dumps(data, indent=4)

    print(json_data)


elif inp == "1":
    experiences = json.load(open("questionari.json"))

    for i in range(20):
        print(experiences[str(i+1)])

        

        




'''

{'question': 'Com pot la pornografia influir en la percepció del consentiment en les relacions sexuals?⚠️🤝', 'answer1': 'Promoguent una comprensió saludable', 'answer2': 'No afectant la percepció del consentiment', 'answer3': 'Contribuint a malentesos sobre el consentiment', 'answer4': 'Reforçant la importància del respecte i la comunicació', 'correct': 'Contribuint a malentesos sobre el consentiment'}


['1', "Com pot afectar la pornografia a l'autoestima en comparar-se amb actors i actrius de la indústria?😳🔍", "Augmenta l'autoestima", 'No té impacte', 'Pot generar inseguretat', 'Millora la confiança en un mateix', 'Pot generar inseguretat']





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
'''