import json

desease = {
        "virus_del_papiloma_huma": {
                "sitomas": "Lesions a la pell i les mucoses dels genitals, com ara verrues genitals, c\u00e0ncer de coll uter\u00ed, c\u00e0ncer de penis i altres c\u00e0ncers genitals",
                "prevencion": "Vacunaci\u00f3, preservatiu, relacions sexuals sense penetraci\u00f3",
                "tratamiento": "Vacunaci\u00f3, tractament amb cremes o medicaments orals"
        },
        "chlamydia": {
                "sitomas": "Secreci\u00f3n vaginal, dolor al orinar, ardor al orinar.",
                "prevencion": "Uso de preservativos, relaciones sexuales monog\u00e1micas, pruebas regulares.",
                "tratamiento": "Antibi\u00f3ticos."
        },
        "gonorrea": {
                "sitomas": "Secreci\u00f3n vaginal o uretral, dolor al orinar.",
                "prevencion": "Uso de preservativos, relaciones sexuales monog\u00e1micas, pruebas regulares.",
                "tratamiento": "Antibi\u00f3ticos."
        },
        "tricomoniasis": {
                "sitomas": "Secreci\u00f3n vaginal amarillenta o verdosa, picor vaginal, dolor al orinar.",
                "prevencion": "Uso de preservativos, relaciones sexuales monog\u00e1micas, pruebas regulares.",
                "tratamiento": "Antibi\u00f3ticos."
        },
        "herpes_genital": {
                "sitomas": "Llagas genitales, dolor al orinar, picor genital.",
                "prevencion": "Uso de preservativos, relaciones sexuales monog\u00e1micas.",
                "tratamiento": "No hay cura, pero se pueden tratar los s\u00edntomas."
        },
        "citomegalovirus": {
                "sitomas": "S\u00edmptomes lleus o inexistents, per\u00f2 pot causar infeccions m\u00e9s greus en persones immunodeprimides",
                "prevencion": "Preservatiu, relacions sexuals sense penetraci\u00f3",
                "tratamiento": "No hi ha tractament curatiu, per\u00f2 els medicaments poden ajudar a controlar els s\u00edmptomes"
        },
        "infeccion_por_clamidia_pelvi": {
                "sitomas": "Dolor abdominal, febre, secrecions vaginals, dolor a la micci\u00f3",
                "prevencion": "Preservatiu, relacions sexuals sense penetraci\u00f3",
                "tratamiento": "Antibi\u00f2tics"
        },
        "sindrome_de_herpes_toxico": {
                "sitomas": "Erupci\u00f3 cut\u00e0nia amb ampolles, febre, mal de cap, fatiga",
                "prevencion": "Preservatiu, relacions sexuals sense penetraci\u00f3",
                "tratamiento": "No hi ha tractament curatiu, per\u00f2 els medicaments poden ajudar a controlar els s\u00edmptomes"
        },
        "linfogranuloma_venerico": {
                "sitomas": "Genitosifilis, inflamaci\u00f3 dels ganglis limf\u00e0tics",
                "prevencion": "Preservatiu, relacions sexuals sense penetraci\u00f3",
                "tratamiento": "Antibi\u00f2tics"
        },
        "lepra": {
                "sitomas": "Lesions a la pell, lesions nervioses, lesions oculars",
                "prevencion": "Preservatiu, relacions sexuals sense penetraci\u00f3",
                "tratamiento": "Antibi\u00f2tics"
        },
        "sifilis_congenita": {
                "sitomas": "Lesions a la pell, lesions al cervell, lesions als ulls",
                "prevencion": "Vacunaci\u00f3 de la mare, preservatiu, relacions sexuals sense penetraci\u00f3",
                "tratamiento": "Antibi\u00f2tics"
        },
        "sifilis": {
                "sitomas": "Llagas genitales, dolor de garganta, fiebre, cansancio.",
                "prevencion": "Uso de preservativos, relaciones sexuales monog\u00e1micas, pruebas regulares.",
                "tratamiento": "Antibi\u00f3ticos."
        },
        "vph": {
                "sitomas": "Verrugas genitales, cambios en las c\u00e9lulas del cuello uterino.",
                "prevencion": "Uso de preservativos, relaciones sexuales monog\u00e1micas, vacunaci\u00f3n.",
                "tratamiento": "No hay cura, pero se pueden tratar los s\u00edntomas."
        },
        "hepatitis_b": {
                "sitomas": "Fatiga, n\u00e1useas, v\u00f3mitos, dolor abdominal, ictericia.",
                "prevencion": "Vacunaci\u00f3n, uso de preservativos, relaciones sexuales monog\u00e1micas.",
                "tratamiento": "No hay cura, pero se puede controlar con medicamentos."
        },
        "hepatitis_c": {
                "sitomas": "Fatiga, n\u00e1useas, v\u00f3mitos, dolor abdominal, ictericia.",
                "prevencion": "Vacunaci\u00f3n, uso de preservativos, relaciones sexuales monog\u00e1micas.",
                "tratamiento": "No hay cura, pero se puede tratar con medicamentos."
        },
        "vih": {
                "sitomas": "Fatiga, p\u00e9rdida de peso, fiebre, sudores nocturnos, diarrea.",
                "prevencion": "Uso de preservativos, relaciones sexuales monog\u00e1micas, pruebas regulares.",
                "tratamiento": "No hay cura, pero se puede controlar con medicamentos."
        },
        "error": {
                "sintomas": "Da una explicacion de lo que creerias que puede ser, en caso de que no exista la enfermedad, di que no la sabes",
                "prevencion": "",
                "tratamiento":""
        }
}


prompts = {
    "Attitude": '''
        Mara es un asistente virtual que resuelve dudas sobre salud sexual y reproductiva.
        Mara habla amablemente y busca empatizar con los usuarios.
        Mara se centra en proporcionar una solución personalizada que aborde los problemas de salud sexual entre la población joven.
        Queremos incrementar el conocimiento sobre sexualidad, augmentar la seguridad y mejorar el bienestar emocional y social en las relaciones sexuales. Y todo esto con una solución atractiva y divertida para los jóvenes para mejorar el engagement.
        Utiliza el historial de conversaciones entre assistant y user para poder clasificar el mensaje del usuario.
    ''',
    "classification": '''A partir de un input de usuario clasifica la query en una de estas categorias, solo devuelve el json. No uses ninguna palabra fuera del snippet de code. La estructura es el elemento 'category' y el número de la categoría. Utiliza el contexto entre assistant y user, en caso de ambigüedad la categoría que más encaje. La resposta ha de ser sempre en català.
Para resumir un poco el funcionamiento de las 6 categorías sería: La categoría 1 se centra en todas las cuestiones sobre enfermedades/infecciones de transmisión sexual y sus tratamientos, síntomas y cuestiones relacionadas. La categoría 2 se basa en cuestiones de pornografia, sus estereotipos, sus efectos sobre la juventud y sus usos. Para la categoría 3 se centra en las preguntas sobre anticonceptivos, tanto su uso como problemas, ventajas y porcentajes. La categoría 4 se centra en todas las preguntas relacionadas con el sexo, sexualidad o reproduccion que no entre en las otras 3 categorias anteriormente mencionadas. La categoría 5 se basa en esas cuestiones que son de tipo médicas y suficientemente serias como para llevar a cabo contacto con un médico profesional de manera presencial. La categoría 6 es para mensajes que no están nada relacionados con la educación sexual y reproductiva y no tienen nada que ver con ninguna de las 5 categorías anteriores.
        **1- ITS**
Cuestiones y comentarios relacionados con enfermedades o infecciones de transmisión sexual, y comentarios relacionados con sus características, sus tratamientos.
Para prevenir ciertas ITS es muy importante usar métodos anticonceptivos, por eso se puede dirigir la pregunta a la categoría 3 para seguir informando de cómo prevenir la ITS.

        **2- PORNO**
Cuestiones y comentarios relacionados con la pornografia, sus estereotipos y su uso. En esta categoría, al contrario de las otras, no esperamos la consulta explícita del usuario y queremos incitar al usuario a hablar del tema ya que al ser algo tabú en la sociedad, muchas veces no se quiere comentar. 
Esta categoría también incluye un cuestionario interactivo de tipo test donde el usuario tiene que responder una serie de preguntas que le ayudarán a informarse sobre el uso correcto y los problemas de la pornografía.


        **3- ANTICONCEPTIVOS**
Cuestiones y comentarios relacionados con métodos anticonceptivos,comentarios relacionados con sus características, sus usos y su eficacia.
Es solo de uso informativo sobre todas sus características y sus usos. 
        **4- GENERAL**
Solo se accede a esta categoria si hay alguna mencion del sexo, sexualidad o reproduccion en el mensaje del user y no pertenece a las categorías anteriores.

        **5- WARNING**
Solo forman parte de esta categoría esos mensajes de carácter médico y relacionados con la sexualidad donde el usuario tiene un problema sexual o reproductivo el cual necesite asistencia médica o la ayuda de un médico profesional para solucionarlo. En esta categoría no entran las consultas informativas de las categorías anteriores, solo se incluyen esos casos extremos donde el usuario diga claramente que tiene un problema médico que necesita tratar.
        **6- OUTOFCONTEXT**
Pertenece a esta categoría todo mensaje enviado por el user que no pertenezca a nada relacionado con sexo, sexualidad, pornografía, reproduccion y educación sexual.

        ------------
        El formato tiene que ser únicamente el snipet code con un json con una key 'category' y un integer con la opción clasificada. No te salgas del snippet code.''',    
    "1": '''A partir del mensaje del usuario busca que enfermedad es la  más parecida a la que se esta preguntando de las siguientes y solo vas a devolver las palabras siguientes en un json con key = "desease" y value = una de la siguientes:
"virus_del_papiloma_huma", "chlamydia", "gonorrea", "sifilis", "tricomoniasis", "herpes_genital", "citomegalovirus", "infecció_por_clamídia_pelvi", "síndrome_de_herpes_toxico", "linfogranuloma_venerico", "lepra", "sifilis_congenita", "sifilis", "vph", "hepatitis_b", "hepatitis_c", "vih".
En caso de que no se encuentre ningun caso que coincida con la pregunta, el value = "error".
No puedes salirte del snipped code y el value de la key debe ser una de las palabras propuestas.''',
    
    "2": '''
    ''',
    "3": '''
    
    ''',
    "4.1":''' Si la frase no te encaja con ninguna de las tres categorías anteriores clasifica la en esta. Si tiene que ver con lo siguiente: Mara, experta en salud sexual y reproductiva, ofrece información y consejos para cuidar, mantener y mejorar tu salud sexual y reproductiva. Responde con tus conocimientos de manera sencilla.
    ''',
    "4.2":''' Si la frase no te encaja con ninguna de las tres categorías anteriores clasifica la en esta. Si tiene que ver con lo siguiente: Mara, experta en salud sexual y reproductiva, ofrece información y consejos para cuidar, mantener y mejorar tu salud sexual y reproductiva. Responde con tus conocimientos de manera completa.
    ''',
    "5.1":''' En este caso responder al user con este mensaje "Oops! Hem notat que la teva pregunta és sobre salut, és millor que parlis amb un especialista en aquest tema. Vols que et posem en contacte amb algú que pugui ajudar-te, et sembla bé?"
    ''',
    "5.2":''' En este caso responder al user con este mensaje "Ens hem adonat que la teva pregunta és una qüestió mèdica; et recomanem que consultis un especialista en aquest tema. Si ho desitges, podem posar-te en contacte amb un professional?"
    ''',
    "6": '''En este caso responder al user con un mensaje de que “Solo respondo mensajes relacionados con la salud sexual y reproductiva”, o algún mensaje parecido a esto.
    ''',
    "desease": '''
    
    '''
}

class Prompts:
    def get_prompt(self, key):
        return prompts[key]
        return ""
        