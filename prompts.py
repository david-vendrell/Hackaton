import json

disease = {
        "virus_del_papiloma_huma": {
                "sintomas": "Lesions a la pell i les mucoses dels genitals, com ara verrues genitals, c\u00e0ncer de coll uter\u00ed, c\u00e0ncer de penis i altres c\u00e0ncers genitals",
                "prevencion": "Vacunaci\u00f3, preservatiu, relacions sexuals sense penetraci\u00f3",
                "tratamiento": "Vacunaci\u00f3, tractament amb cremes o medicaments orals"
        },
        "chlamydia": {
                "sintomas": "Secreci\u00f3n vaginal, dolor al orinar, ardor al orinar.",
                "prevencion": "Uso de preservativos, relaciones sexuales monog\u00e1micas, pruebas regulares.",
                "tratamiento": "Antibi\u00f3ticos."
        },
        "gonorrea": {
                "sintomas": "Secreci\u00f3n vaginal o uretral, dolor al orinar.",
                "prevencion": "Uso de preservativos, relaciones sexuales monog\u00e1micas, pruebas regulares.",
                "tratamiento": "Antibi\u00f3ticos."
        },
        "tricomoniasis": {
                "sintomas": "Secreci\u00f3n vaginal amarillenta o verdosa, picor vaginal, dolor al orinar.",
                "prevencion": "Uso de preservativos, relaciones sexuales monog\u00e1micas, pruebas regulares.",
                "tratamiento": "Antibi\u00f3ticos."
        },
        "herpes_genital": {
                "sintomas": "Llagas genitales, dolor al orinar, picor genital.",
                "prevencion": "Uso de preservativos, relaciones sexuales monog\u00e1micas.",
                "tratamiento": "No hay cura, pero se pueden tratar los s\u00edntomas."
        },
        "citomegalovirus": {
                "sintomas": "S\u00edmptomes lleus o inexistents, per\u00f2 pot causar infeccions m\u00e9s greus en persones immunodeprimides",
                "prevencion": "Preservatiu, relacions sexuals sense penetraci\u00f3",
                "tratamiento": "No hi ha tractament curatiu, per\u00f2 els medicaments poden ajudar a controlar els s\u00edmptomes"
        },
        "infeccion_por_clamidia_pelvi": {
                "sintomas": "Dolor abdominal, febre, secrecions vaginals, dolor a la micci\u00f3",
                "prevencion": "Preservatiu, relacions sexuals sense penetraci\u00f3",
                "tratamiento": "Antibi\u00f2tics"
        },
        "sindrome_de_herpes_toxico": {
                "sintomas": "Erupci\u00f3 cut\u00e0nia amb ampolles, febre, mal de cap, fatiga",
                "prevencion": "Preservatiu, relacions sexuals sense penetraci\u00f3",
                "tratamiento": "No hi ha tractament curatiu, per\u00f2 els medicaments poden ajudar a controlar els s\u00edmptomes"
        },
        "linfogranuloma_venerico": {
                "sintomas": "Genitosifilis, inflamaci\u00f3 dels ganglis limf\u00e0tics",
                "prevencion": "Preservatiu, relacions sexuals sense penetraci\u00f3",
                "tratamiento": "Antibi\u00f2tics"
        },
        "lepra": {
                "sintomas": "Lesions a la pell, lesions nervioses, lesions oculars",
                "prevencion": "Preservatiu, relacions sexuals sense penetraci\u00f3",
                "tratamiento": "Antibi\u00f2tics"
        },
        "sifilis_congenita": {
                "sintomas": "Lesions a la pell, lesions al cervell, lesions als ulls",
                "prevencion": "Vacunaci\u00f3 de la mare, preservatiu, relacions sexuals sense penetraci\u00f3",
                "tratamiento": "Antibi\u00f2tics"
        },
        "sifilis": {
                "sintomas": "Llagas genitales, dolor de garganta, fiebre, cansancio.",
                "prevencion": "Uso de preservativos, relaciones sexuales monog\u00e1micas, pruebas regulares.",
                "tratamiento": "Antibi\u00f3ticos."
        },
        "vph": {
                "sintomas": "Verrugas genitales, cambios en las c\u00e9lulas del cuello uterino.",
                "prevencion": "Uso de preservativos, relaciones sexuales monog\u00e1micas, vacunaci\u00f3n.",
                "tratamiento": "No hay cura, pero se pueden tratar los s\u00edntomas."
        },
        "hepatitis_b": {
                "sintomas": "Fatiga, n\u00e1useas, v\u00f3mitos, dolor abdominal, ictericia.",
                "prevencion": "Vacunaci\u00f3n, uso de preservativos, relaciones sexuales monog\u00e1micas.",
                "tratamiento": "No hay cura, pero se puede controlar con medicamentos."
        },
        "hepatitis_c": {
                "sintomas": "Fatiga, n\u00e1useas, v\u00f3mitos, dolor abdominal, ictericia.",
                "prevencion": "Vacunaci\u00f3n, uso de preservativos, relaciones sexuales monog\u00e1micas.",
                "tratamiento": "No hay cura, pero se puede tratar con medicamentos."
        },
        "vih": {
                "sintomas": "Fatiga, p\u00e9rdida de peso, fiebre, sudores nocturnos, diarrea.",
                "prevencion": "Uso de preservativos, relaciones sexuales monog\u00e1micas, pruebas regulares.",
                "tratamiento": "No hay cura, pero se puede controlar con medicamentos."
        },
        "error": {
                "sintomas": "Da una explicacion de lo que creerias que puede ser, en caso de que no exista la enfermedad, di que no la sabes",
                "prevencion": "",
                "tratamiento":""
        }
}

protection = {

   "preservatius_masculins": {
      "funcionamiento": "Es un m\u00e9todo de barrera que evita que el semen u otros fluidos secretados por el pene entren en contacto con la otra persona. Tiene como objetivo evitar embarazos no planificados, la transmisi\u00f3n del VIH y/o otras infecciones de transmisi\u00f3n sexual.",
      "eficacia": "Por cada 100 mujeres que utilizan este m\u00e9todo durante un a\u00f1o, 82 no quedan embarazadas.",
      "cambios_en_la_regla": "No se han descrito cambios en la regla.",
      "como_se_utiliza": "- Utiliza solo preservativos homologados por las autoridades sanitarias y la CEE. - Verifica la fecha de caducidad; duran 5 a\u00f1os despu\u00e9s de fabricarse. - Gu\u00e1rdalos en lugares frescos y secos para que no se deterioren. - Sigue adecuadamente los pasos para una utilizaci\u00f3n correcta: - Utiliza un preservativo nuevo en cada relaci\u00f3n sexual con penetraci\u00f3n. - Coloca un preservativo nuevo en los juguetes sexuales cada vez que se compartan. - \u00c1brelo con cuidado para no da\u00f1arlo con u\u00f1as, anillos y/o dientes. - Coloca el preservativo cuando el pene est\u00e9 erecto, antes de cualquier penetraci\u00f3n vaginal, anal u oral. - Presiona la punta del dep\u00f3sito del preservativo y desenrolla el preservativo hasta cubrir completamente el pene. - Se puede lubricar el preservativo, una vez colocado, con productos solubles en agua, ya que los aceites pueden da\u00f1ar el l\u00e1tex del preservativo. - Despu\u00e9s de eyacular, retira el preservativo con el pene a\u00fan erecto, sujetando el preservativo por la base. - Comprueba que no se haya roto, \u00e1talo y t\u00edralo a la basura, no al inodoro. - No lo utilices junto con el preservativo femenino.",
      "mal_uso_o_rotura": "Se puede recurrir a la anticoncepci\u00f3n de emergencia. Los anticonceptivos orales de emergencia son medicamentos que se dispensan en centros de atenci\u00f3n primaria, servicios de urgencias de hospitales y/o farmacias. Deben tomarse lo antes posible, con un poco de agua, y es mejor acompa\u00f1arlos con alg\u00fan alimento. Como primera opci\u00f3n, existe el levonorgestrel de 1,5 mg. Deben tomarse al mismo tiempo uno o dos comprimidos (seg\u00fan el preparado) en una sola toma, antes de las primeras 72 horas (3 d\u00edas) despu\u00e9s de la relaci\u00f3n sexual de riesgo. Otra opci\u00f3n es el comprimido de ulipristal de 30 mg, que debe tomarse antes de las 120 horas (5 d\u00edas) posteriores al coito, y tambi\u00e9n, para este periodo, existe la posibilidad de colocar un DIU de cobre.",
      "tiempo_en_fertilidad": "El preservativo no afecta la fertilidad de la mujer, porque no interfiere en el ciclo ov\u00e1rico.",
      "cuando_no_utilizarlo": "- Tienes alergia al material (habitualmente, l\u00e1tex). - Perd si s\u00e9n dialtres materials, si que el pots utilitzar; por ejemplo, de poliuretano.",
      "efectos_negativos_de_uso": "- No se conocen.",
      "ventajas": "- Ofrece doble protecci\u00f3n: ante un embarazo no deseado y ante el contagio del VIH u otras infecciones de transmisi\u00f3n sexual. - No requiere receta m\u00e9dica. - Es un m\u00e9todo natural, no lleva hormonas. - Tiene un precio asequible. - Es f\u00e1cil de encontrar en tiendas por Internet, supermercados y/o farmacias. - Tiene diferentes presentaciones, gustos, olores, formas, texturas (acanaladas, estriadas, texturizadas y punteadas), sensaciones, materiales, sustancias a\u00f1adidas, as\u00ed como aplicadores, para mejorar su calidad y hacerlos m\u00e1s atractivos, aceptables y agradables.",
      "inconvenientes": "- Es un m\u00e9todo que depende del usuario, por lo que su eficacia depende de su correcto uso. - Hay muchos factores que afectan al uso general y diario de los condones. Se necesita negociaci\u00f3n con la pareja y cumplir las normas correctas. La falta de conocimiento o experiencia con los preservativos y/o el consumo de alcohol u otras sustancias favorecen el uso inadecuado y afectan la efectividad. - Puede disminuir el placer sexual en comparaci\u00f3n con la ausencia de preservativo.",
      "precio": "Hay diferentes modelos y presentaciones; el precio se sit\u00faa cerca de un euro la unidad. Los de l\u00e1tex son m\u00e1s econ\u00f3micos que los de otros materiales, en general."
   },
   "implant_contraceptiu_subdermic": {
      "funcionamiento": "El progestagen evita que els ovaris fabriquin \u00f2vuls i fa que el fluix sigui m\u00e9s esp\u00e8s, dificultant la mobilitat dels espermatozoides.",
      "eficacia": "De cada 100 dones que utilitzen aquest m\u00e8tode durant un any, te\u00f2ricament 99,95 no es queden embarassades; en l\u2019\u00fas real, en s\u00f3n 99.",
      "cambios_en_la_regla": "\u00c9s probable que tingui petites sagnades vaginals entre regles, regles irregulars o abs\u00e8ncia de regla durant alguns mesos. Tamb\u00e9 pot ser que la regla sigui menys abundant i freq\u00fcent.",
      "como_se_utiliza": "Te\u2019l posa el professional de llevadoria o ginecologia a la consulta. Per inserir-lo, cal fer una petita intervenci\u00f3 quir\u00fargica amb anest\u00e8sia local, durant uns 10 minuts, en la cara interna del bra\u00e7.",
      "mal_uso_o_rotura": "Es pot produir l\u2019expulsi\u00f3 si est\u00e0 mal col\u00b7locat o si es t\u00e9 una infecci\u00f3 a la pell; per\u00f2 si aix\u00f2 pass\u00e9s, te n\u2019adonaries. Pot costar una mica m\u00e9s de treure si es mou, per\u00f2 no perd efic\u00e0cia.",
      "tiempo_en_fertilidad": "L\u2019efecte anticonceptiu desapareix r\u00e0pidament despr\u00e9s de retirar l\u2019implant, i es pot quedar embarassada com qualsevol dona que no l\u2019hagi portat.",
      "cuando_no_utilizarlo": "Algunes contraindicacions inclouen haver tingut un ictus, infart de miocardi o co\u00e0guls de sang, tenir lupus, migranya amb altres s\u00edmptomes, c\u00e0ncer de mama, problemes de fetge, sagnada vaginal desconeguda, etc.",
      "efectos_negativos_de_uso": "Entre els efectes adversos es troben mal de cap, dolor o tensi\u00f3 als pits, augment de pes, irregularitats menstruals, canvis en l\u2019estat d\u2019\u00e0nim, acne, quists ov\u00e0rics, pressi\u00f3 arterial alta, n\u00e0usees, v\u00f2mits, picor a la zona de la inserci\u00f3, entre d\u2019altres.",
      "ventajas": "Una vegada posat, no has d\u2019estar pendent de res. \u00c9s compatible amb la lact\u00e0ncia.",
      "inconvenientes": "Mol\u00e8sties locals despr\u00e9s de la inserci\u00f3, discreci\u00f3 en la percepci\u00f3 de portar-lo i una petita cicatriu en l\u2019avantbra\u00e7.",
      "precio": "Entre 150 i 200 euros la unitat (entre 2,5 i 3,3 euros al mes). Algunes comunitats ofereixen finan\u00e7ament."
   },
   "preservatius_femenins": {
      "funcionamiento": "Es un m\u00e9todo de barrera que evita que el semen u otros fluidos secretados por el pene entren en contacto con la otra persona. Tiene como objetivo evitar embarazos no planificados, la transmisi\u00f3n del VIH y/o otras infecciones de transmisi\u00f3n sexual.",
      "eficacia": "- Eficacia contraceptiva: Por cada 100 mujeres que utilizan este m\u00e9todo durante un a\u00f1o, 79 no quedan embarazadas. - Protecci\u00f3n ante infecciones de transmisi\u00f3n sexual: El riesgo de contagio con un uso correcto y sistem\u00e1tico se podr\u00eda reducir un 97%.",
      "cambios_en_la_regla": "No se han descrito cambios relativos a la regla.",
      "como_se_utiliza": "- Utiliza solo preservativos homologados por las autoridades sanitarias y la CEE. - Verifica la fecha de caducidad; duran 5 a\u00f1os despu\u00e9s de fabricarse. - Gu\u00e1rdalos en lugares frescos y secos para que no se deterioren. - Sigue adecuadamente los pasos para una utilizaci\u00f3n correcta: - Utiliza un preservativo nuevo en cada relaci\u00f3n sexual, incluso si la misma persona puede eyacular m\u00e1s de una vez sin retirar el preservativo. - Se puede colocar la mujer, hasta 8 horas antes de la relaci\u00f3n sexual. - No lo utilices junto con el preservativo masculino. - S\u00e1calo del paquete y sujeta la funda con el anillo de la parte abierta, colgando hacia abajo. - Estrecha el anillo de la parte de la funda entre los dedos pulgar e \u00edndice para introducirlo as\u00ed en la vagina, tan profundo como sea posible. Se puede empujar el anillo al fondo con el dedo introducido en el interior del preservativo. - Est\u00e1 lubricado por dentro y por fuera con un lubricante de silicona. - No es necesario retirarlo inmediatamente despu\u00e9s de la eyaculaci\u00f3n. Se retira retorciendo el anillo exterior sobre s\u00ed mismo para mantener el semen en el interior. - L\u00e1nzalo a la basura, no al inodoro.",
      "mal_uso_o_rotura": "Se puede recurrir a la anticoncepci\u00f3n de emergencia. Los anticonceptivos orales de emergencia son medicamentos que se dispensan en centros de atenci\u00f3n primaria, servicios de urgencias de hospitales y/o farmacias. Deben tomarse lo antes posible, con un poco de agua, y es mejor si pueden ir acompa\u00f1ados de alg\u00fan alimento. Como primera opci\u00f3n, hay levonorgestrel de 1,5 mg. Deben tomarse al mismo tiempo uno o dos comprimidos (seg\u00fan el preparado) en una toma \u00fanica, antes de las primeras 72 horas (3 d\u00edas) despu\u00e9s de la relaci\u00f3n sexual de riesgo. Otra opci\u00f3n es el comprimido de ulipristal de 30 mg, que debe tomarse antes de las 120 horas (5 d\u00edas) posteriores al coito, y tambi\u00e9n, para este periodo, existe la posibilidad de colocar un DIU de cobre.",
      "tiempo_en_fertilidad": "El preservativo no afecta la fertilidad de la mujer, porque no interfiere en el ciclo ov\u00e1rico.",
      "cuando_no_utilizarlo": "- No se conocen.",
      "efectos_negativos_de_uso": "- Ofrece doble protecci\u00f3n: ante un embarazo no deseado y ante el contagio del VIH u otras infecciones de transmisi\u00f3n sexual. - Se puede utilizar en las penetraciones vaginales y anales (sin anillo en el fondo). - Facilita que sea la mujer la que inicie la adopci\u00f3n de medidas de protecci\u00f3n. - Se puede colocar hasta 8 horas antes de la relaci\u00f3n sexual. - Se pueden tener diferentes eyaculaciones con la misma persona sin retirar el preservativo y no es necesario retirarlo inmediatamente despu\u00e9s de la eyaculaci\u00f3n. - No requiere receta m\u00e9dica. - Es un m\u00e9todo natural, no lleva hormonas. - Es m\u00e1s resistente que el preservativo masculino. - Viene lubricado. - No altera la flora bacteriana ni hay descritas reacciones al\u00e9rgicas. - Ha bajado de precio. - Con los \u00faltimos avances en tecnolog\u00eda, tiene diferentes presentaciones, gustos, olores, formas, texturas (acanaladas, estriadas, texturizadas y punteadas), sensaciones, materiales, sustancias a\u00f1adidas, as\u00ed como aplicadores, para mejorar su calidad y hacerlo m\u00e1s atractivo, aceptable y agradable.",
      "ventajas": "- Es un m\u00e9todo que depende del usuario, por lo que su eficacia depende de su correcto uso. - Puede disminuir el",
      "inconvenientes": "",
      "precio": ""
   },
   "dispositiu_intrauteri_hormonal": {
      "funcionamiento": "Provoca canvis en la mucosa uterina i fa que el fluix sigui m\u00e9s esp\u00e8s, creant una barrera que dificulta la mobilitat dels espermatozoides.",
      "eficacia": "De cada 100 dones que utilitzen aquest m\u00e8tode durant un any, te\u00f2ricament 99,8 no es queden embarassades; en l\u2019\u00fas real, l\u2019efic\u00e0cia \u00e9s pr\u00e0cticament la mateixa.",
      "cambios_en_la_regla": "Fa que les regles siguin menys doloroses i menys abundants. Algunes dones deixen de tenir la regla mentre el porten.",
      "como_se_utiliza": "Te\u2019l posen a la consulta ginecol\u00f2gica.",
      "mal_uso_o_rotura": "De cada 1.000 dones, 7 l\u2019expulsen, i a partir d\u2019aquest moment deixa de ser efica\u00e7.",
      "tiempo_en_fertilidad": "La fertilitat es pot recuperar tot just despr\u00e9s de treure el DIU.",
      "cuando_no_utilizarlo": "Algunes contraindicacions inclouen haver tingut un fill fa menys de 36 setmanes, avortament amb infecci\u00f3, ictus, infart de miocardi, co\u00e0guls de sang, lupus, migranya amb altres s\u00edmptomes, c\u00e0ncer de cervix, mama, ovari, anomalia anat\u00f2mica en l\u2019\u00fater, risc d'infeccions, VIH, cirrosi hep\u00e0tica, tumor al fetge.",
      "efectos_negativos_de_uso": "Tensi\u00f3 als pits, mal de cap, p\u00e8rdua de la regla, quists ov\u00e0rics, n\u00e0usees, v\u00f2mits, canvis d\u2019humor, borrissol, acne, dolor abdominal, p\u00e8rdua de pes, entre d\u2019altres.",
      "ventajas": "No cal estar-ne pendent una vegada posat. Podria disminuir el risc de c\u00e0ncer d\u2019endometri.",
      "inconvenientes": "Triga uns 7 dies a ser efectiu. Pot ser una mica dolorosa la inserci\u00f3, encara que \u00e9s r\u00e0pida i es fa a la consulta.",
      "precio": "Entre 150 i 180 euros la unitat (entre 2,5 i 3 euros al mes)."
   },
   "dispositiu_intrauteri_no_hormonal": {
      "funcionamiento": "El dispositivo lleva un filamento de cobre que genera una reacci\u00f3n inflamatoria local, paraliza los espermatozoides y dificulta la fecundaci\u00f3n del \u00f3vulo. Por otro lado, empeora el ambiente en el endometrio y dificulta la implantaci\u00f3n.",
      "eficacia": "De cada 100 mujeres que usan este m\u00e9todo durante un a\u00f1o, 99,2 no quedan embarazadas.",
      "cambios_en_la_regla": "Durante la menstruaci\u00f3n, es com\u00fan que aumente la cantidad de flujo menstrual y su duraci\u00f3n.",
      "como_se_utiliza": "Se debe colocar y retirar \u00fanicamente por personal m\u00e9dico especializado. Se recomienda una revisi\u00f3n entre las 4 y 12 semanas despu\u00e9s de la inserci\u00f3n. Dependiendo del tipo de DIU, puede permanecer entre 5 y 10 a\u00f1os, pero se puede extraer en cualquier momento.",
      "mal_uso_o_rotura": "Debes acudir a una visita m\u00e9dica para confirmarlo.",
      "tiempo_en_fertilidad": "La fertilidad vuelve a los niveles previos al extraer el DIU.",
      "cuando_no_utilizarlo": "Presentas anomal\u00edas uterinas como fibromas que pueden interferir en la colocaci\u00f3n o retenci\u00f3n del dispositivo, infecci\u00f3n p\u00e9lvica, c\u00e1ncer de \u00fatero o cuello uterino, alergia a alg\u00fan componente del dispositivo o trastorno que cause acumulaci\u00f3n excesiva de cobre.",
      "efectos_negativos_de_uso": "Dolor durante la colocaci\u00f3n del dispositivo, c\u00f3licos y dolores de espalda un d\u00eda despu\u00e9s de la inserci\u00f3n, menstruaciones m\u00e1s abundantes y largas, c\u00f3licos durante el per\u00edodo menstrual.",
      "ventajas": "M\u00e9todo reversible, protecci\u00f3n a largo plazo, discreto, no interfiere en el acto sexual, no se ve afectado por v\u00f3mitos o diarrea ni por el uso de antibi\u00f3ticos comunes, puede utilizarse durante la lactancia.",
      "inconvenientes": "Podr\u00eda no ser adecuado si tienes menstruaciones muy abundantes y no protege contra infecciones de transmisi\u00f3n sexual.",
      "precio": "Entre 30 y 50 euros por unidad. En algunas comunidades, est\u00e1 financiado."
   },
   "vasectomia": {
      "funcionamiento": "Consiste en cortar los conductos deferentes de los test\u00edculos, los cuales transportan los espermatozoides desde los test\u00edculos hacia el exterior, evitando su evacuaci\u00f3n con el semen durante la eyaculaci\u00f3n.",
      "eficacia": "De cada 100 hombres que se someten a este procedimiento, aproximadamente 99,85 pierden la capacidad de embarazar a una mujer.",
      "cambios_en_la_regla": "No se han descrito cambios en relaci\u00f3n con la eyaculaci\u00f3n o la micci\u00f3n.",
      "como_se_utiliza": "Cirug\u00eda m\u00ednimamente invasiva realizada por un especialista con anestesia local. No requiere hospitalizaci\u00f3n y la recuperaci\u00f3n generalmente dura hasta 2 semanas. Verificaci\u00f3n de la efectividad mediante an\u00e1lisis de semen.",
      "mal_uso_o_rotura": "La anticoncepci\u00f3n definitiva se considera permanente e irreversible, por lo que la fertilidad no puede recuperarse.",
      "tiempo_en_fertilidad": "Enumera condiciones m\u00e9dicas y situaciones espec\u00edficas en las que no se recomienda el procedimiento.",
      "cuando_no_utilizarlo": "En algunos casos, se han descrito hematomas o infecciones en el \u00e1rea de incisi\u00f3n, que suelen resolverse en unos pocos d\u00edas.",
      "efectos_negativos_de_uso": "Alta efectividad en anticoncepci\u00f3n masculina, m\u00e9todo definitivo, cirug\u00eda sencilla y m\u00ednimamente invasiva.",
      "ventajas": "Irreversible, no protege contra infecciones de transmisi\u00f3n sexual.",
      "inconvenientes": "Cubierto por la Seguridad Social. En cl\u00ednicas privadas, alrededor de 900 euros (precio aproximado).",
      "precio": ""
   },
   "lligadura_de_trompes": {
      "funcionamiento": "Es un procedimiento quir\u00fargico que liga, bloquea o extirpa las trompas de Falopio, los conductos que conectan los ovarios con el \u00fatero. Esto bloquea el paso de los \u00f3vulos, impidiendo su contacto con el semen y evitando el embarazo.",
      "eficacia": "De cada 100 mujeres que se someten al procedimiento en un a\u00f1o, aproximadamente 99,5 no quedan embarazadas.",
      "cambios_en_la_regla": "No se han descrito cambios en la menstruaci\u00f3n.",
      "como_se_utiliza": "Intervenci\u00f3n quir\u00fargica realizada por un profesional ginecol\u00f3gico, generalmente por laparoscopia, aunque existen otras t\u00e9cnicas. Por lo general, requiere anestesia general. La recuperaci\u00f3n var\u00eda de 1 a 2 d\u00edas hasta varias semanas. Efectividad inmediata.",
      "mal_uso_o_rotura": "Los m\u00e9todos anticonceptivos definitivos se consideran permanentes e irreversibles, por lo que la fertilidad no puede recuperarse.",
      "tiempo_en_fertilidad": "Enumera condiciones y situaciones en las que no se recomienda el procedimiento.",
      "cuando_no_utilizarlo": "Aunque la recuperaci\u00f3n suele ser r\u00e1pida y con pocas molestias, se han descrito algunas complicaciones relacionadas con la intervenci\u00f3n o la anestesia: dolor abdominal, dorsal o tor\u00e1cico, n\u00e1useas, v\u00f3mitos, hemorragias, hematomas o infecci\u00f3n.",
      "efectos_negativos_de_uso": "M\u00e9todo definitivo que elimina la necesidad de anticoncepci\u00f3n, recuperaci\u00f3n postoperatoria generalmente r\u00e1pida y sin grandes molestias, alta efectividad, reducci\u00f3n del riesgo de c\u00e1ncer de ovario.",
      "ventajas": "No protege contra infecciones de transmisi\u00f3n sexual, procedimiento definitivo y no reversible.",
      "inconvenientes": "Este tipo de intervenci\u00f3n est\u00e1 cubierto por la Seguridad Social. Algunas cl\u00ednicas privadas lo realizan por alrededor de 2.000 euros (precio aproximado).",
      "precio": ""
   },
   "anticoncepcio_postcoital_emergencia": {
      "funcionamiento": "Atura el proc\u00e9s d\u2019ovulaci\u00f3, dificulta la fecundaci\u00f3 de l\u2019\u00f2vul pels espermatozoides i/o, en cas que es produeixi, evita que l\u2019\u00f2vul s\u2019implanti a l\u2019\u00fater.",
      "eficacia": "Es dispensen en centres d\u2019atenci\u00f3 prim\u00e0ria (CAP), unitats d\u2019atenci\u00f3 a la salut sexual i reproductiva (ASSIR), centres de planificaci\u00f3 familiar, hospitals, serveis d\u2019urg\u00e8ncies hospitalaris i farm\u00e0cies.",
      "cambios_en_la_regla": "Indicat per relacions coitals sense m\u00e8tode anticonceptiu, violaci\u00f3 sense anticoncepci\u00f3 pr\u00e8via, \u00fas recent de medicacions que poden provocar malformacions en el fetus, \u00fas incorrecte o altres incidents amb els m\u00e8todes naturals, risc d\u2019ejaculaci\u00f3 anticipada, fallada de preservatiu, fallades en el compliment o incid\u00e8ncies d\u2019\u00fas d\u2019un m\u00e8tode hormonal, retirada imprevista d\u2019un DIU.",
      "como_se_utiliza": "- Levonorgestrel de 1,5 mg: Efica\u00e7 dins de les 72 hores, disminueix progressivament l'efic\u00e0cia en funci\u00f3 del temps. - Acetat d\u2019ulipristal de 30 mg i DIU de coure: Efica\u00e7os fins a 5 dies despr\u00e9s del coit.",
      "mal_uso_o_rotura": "- Levonorgestrel de 1,5 mg: S'ha de prendre al m\u00e9s aviat possible dins de les 72 hores posteriors al coit. - Acetat d\u2019ulipristal de 30 mg: S'ha de prendre una sola pastilla abans que passin 120 hores (5 dies) des del coit. - DIU de coure: Col\u00b7locat per un professional qualificat en un CAP, ASSIR o hospital abans que passin 120 hores (5 dies) des del coit.",
      "tiempo_en_fertilidad": "Medicaments: Possibles canvis en la data, abund\u00e0ncia i durada de la regla. DIU de coure: Pot provocar regles abundants.",
      "cuando_no_utilizarlo": "- Levonorgestrel de 1,5 mg: Certes malalties i al\u00b7l\u00e8rgies. - Acetat d\u2019ulipristal de 30 mg: Problemes amb el metabolisme de la lactosa, asma, embar\u00e0s i lact\u00e0ncia materna. - DIU de coure: Infecci\u00f3 genital o malformaci\u00f3 uterina.",
      "efectos_negativos_de_uso": "- Medicaments: N\u00e0usees, v\u00f2mits, fatiga, marejos, dolor abdominal, retards en la regla, trastorns en la sagnada. - DIU de coure: Mol\u00e8sties en la inserci\u00f3, regles abundants.",
      "ventajas": "Tornar a prendre el medicament si vomites durant les 3 hores posteriors a l\u2019administraci\u00f3, ja que no s\u2019ha absorbit completament.",
      "inconvenientes": "25\u20ac",
      "precio": ""
   },
   "metode_billings_fluidesa_moc_cervical": {
      "funcionamiento": "Se basa en l\u2019observaci\u00f3 de signes i s\u00edmptomes naturals de les fases m\u00e9s f\u00e8rtils i menys f\u00e8rtils del cicle menstrual, en particular en el cambio del moco cervical.",
      "eficacia": "Entre 86 i 79 dones de cada 100 no se quedan embarazadas.",
      "cambios_en_la_regla": "No afecta la naturaleza del ciclo menstrual ni utiliza sustancias que puedan modificarlo.",
      "como_se_utiliza": "Observar las caracter\u00edsticas del moco cervical durante varios ciclos, registr\u00e1ndolo en un gr\u00e1fico donde se distinga entre moco poco f\u00e9rtil (f) y moco muy f\u00e9rtil (F). Evitar relaciones sin protecci\u00f3n durante los d\u00edas f\u00e9rtilmente m\u00e1s activos.",
      "mal_uso_o_rotura": "Este m\u00e9todo no afecta la recuperaci\u00f3n de la fertilidad.",
      "tiempo_en_fertilidad": "Sin entrenamiento previo, y en situaciones como lactancia, etapa cercana a la menopausia, ciertos medicamentos, estr\u00e9s o enfermedades.",
      "cuando_no_utilizarlo": "No se esperan efectos adversos, ya que se basa en la observaci\u00f3n de los signos de fertilidad respetando la naturaleza del ciclo de cada mujer.",
      "efectos_negativos_de_uso": "Favorece el autoconocimiento del ciclo ov\u00e1rico, no tiene efectos secundarios, implica a la pareja en la anticoncepci\u00f3n y es aut\u00f3nomo y sin costo.",
      "ventajas": "Puede ser dif\u00edcil cumplir con los per\u00edodos de continencia, el moco se altera con el semen y/o lubricantes, y no protege contra infecciones de transmisi\u00f3n sexual.",
      "inconvenientes": "No tiene un costo econ\u00f3mico directo, pero requiere esfuerzo personal y entrenamiento.",
      "precio": ""
   },
   "metode_simptotermic": {
      "funcionamiento": "Es basa en l\u2019observaci\u00f3 de signes i s\u00edmptomes naturals de les fases m\u00e9s f\u00e8rtils i menys f\u00e8rtils del cicle menstrual, combinant el m\u00e8tode del calendari amb el m\u00e8tode mucot\u00e8rmic i la valoraci\u00f3 de la posici\u00f3 i consist\u00e8ncia del coll de l\u2019\u00fater.",
      "eficacia": "Entre 90 i 98 dones de cada 100 no es queden embarassades.",
      "cambios_en_la_regla": "Cap, ja que no interfereix gens en la naturalesa del cicle ni utilitza cap subst\u00e0ncia que el pugui modificar.",
      "como_se_utiliza": "1. Identificar el primer dia f\u00e8rtil amb el seguiment de la durada dels \u00faltims cicles, l'observaci\u00f3 del moc cervical i l'autopalpaci\u00f3 de la c\u00e8rvix. 2. Identificar l\u2019\u00faltim dia f\u00e8rtil amb la mesura de la temperatura basal. 3. Evitar relacions des del primer fins al darrer dia f\u00e8rtil.",
      "mal_uso_o_rotura": "Aquest m\u00e8tode no afecta la recuperaci\u00f3 de la fertilitat.",
      "tiempo_en_fertilidad": "No fas un entrenament previ, i en situacions com malaltia, febre, infecci\u00f3 vaginal, lact\u00e0ncia, etapa propera a la menopausa, treball per torns, estr\u00e8s, cicles de son interromputs, exc\u00e9s de son, efectes de begudes alcoh\u00f2liques, viatges freq\u00fcents, treball en diferents torns, trastorns ginecol\u00f2gics, i \u00fas de cert medicaments.",
      "cuando_no_utilizarlo": "Cap, ja que es basa en l\u2019observaci\u00f3 dels signes de fertilitat, respectant la naturalesa dels cicles de cada dona.",
      "efectos_negativos_de_uso": "Afavoreix l\u2019autoconeixement del cicle ov\u00e0ric, sense efectes secundaris, implica la parella en l\u2019anticoncepci\u00f3, \u00e9s aut\u00f2nom i sense cost.",
      "ventajas": "No protegeix davant d\u2019infeccions de transmissi\u00f3 sexual, pot ser complex per per\u00edodes d'abstin\u00e8ncia llargs. Pot complementar-se amb un m\u00e8tode de barrera.",
      "inconvenientes": "Sense cost econ\u00f2mic, requerint esfor\u00e7 personal per aprendre'l amb ajuda d'assessorament especialitzat.",
      "precio": ""
   },
   "anticonceptius_injectables_progestagens": {
      "funcionamiento": "Inhibeix l\u2019ovulaci\u00f3 i fa que el flux sigui m\u00e9s esp\u00e8s, creant una barrera que impedeix que els espermatozoides fecundin l\u2019\u00f2vul.",
      "eficacia": "Te\u00f2ricament, per cada 100 dones que utilitzen aquest m\u00e8tode durant un any, 99,7 no es queden embarassades; en l\u2019\u00fas real, l\u2019efic\u00e0cia es redueix a 94 de cada 100.",
      "cambios_en_la_regla": "Pot fer que la regla sigui menys abundant i dolorosa; fins i tot podria ser que es retir\u00e9s durant un temps.",
      "como_se_utiliza": "El personal d\u2019infermeria te l\u2019injecta per via intramuscular.",
      "mal_uso_o_rotura": "Per un dia no passa res, ja que t\u00e9 una durada de 3 mesos. Al cap de 3 mesos s\u2019ha de repetir la injecci\u00f3, per\u00f2 si es retarda un dia o dos no hi ha risc d\u2019embar\u00e0s.",
      "tiempo_en_fertilidad": "Despr\u00e9s de deixar l\u2019anticonceptiu injectable que cont\u00e9 nom\u00e9s progest\u00e0gens, pots tardar uns mesos a ser f\u00e8rtil com abans. Algunes dones poden tardar fins a 9 mesos a recuperar la fertilitat.",
      "cuando_no_utilizarlo": "Est\u00e0s en quarantena (despr\u00e9s d\u2019un part), has tingut ictus, infart de miocardi o co\u00e0guls de sang als pulmons, tens la tensi\u00f3 arterial alta, tens lupus, migranya amb altres s\u00edmptomes, etc.",
      "efectos_negativos_de_uso": "Fins a 70 dones de cada 100 presenten sagnades vaginals irregulars. 20 dones de cada 100 tenen mal de cap, 13 de cada 100 pateixen de marejos i 9 de cada 100 tenen n\u00e0usees i/o dolor o tensi\u00f3 en els pits. Despr\u00e9s de 3 anys d\u2019\u00fas, 80 dones de cada 100 deixen de tenir la regla, encara que reapareix si es deixa el m\u00e8tode.",
      "ventajas": "\u00c9s compatible amb la lact\u00e0ncia. No cal preocupar-se per res; solament de posar-se una injecci\u00f3 nova al cap de 3 mesos. Alguns preparats d\u2019aquest m\u00e8tode poden millorar l\u2019acne o propiciar el creixement del p\u00e8l en llocs poc freq\u00fcents.",
      "inconvenientes": "Els efectes secundaris no es poden aturar de cap manera, ja que el f\u00e0rmac s\u2019ha introdu\u00eft al cos i no es pot retirar.",
      "precio": "A partir de 2,50 euros per injecci\u00f3."
   },
   "anella_vaginal_progestagens": {
      "funcionamiento": "Des que es posa fins que es treu, l\u2019anella allibera hormones a la vagina que interfereixen en l\u2019ovulaci\u00f3 i fan que el moc cervical sigui m\u00e9s esp\u00e8s, impedint el pas als espermatozoides.",
      "eficacia": "Te\u00f2ricament, per cada 100 dones que utilitzen aquest m\u00e8tode durant un any, 98,77 no es queden embarassades.",
      "cambios_en_la_regla": "Pot provocar sagnades irregulars i allargar el temps que triga a venir la regla despr\u00e9s d\u2019un part.",
      "como_se_utiliza": "S\u2019introdueix a la vagina i l\u2019efecte dura 3 mesos. Es pot utilitzar ininterrompudament durant un any.",
      "mal_uso_o_rotura": "No conv\u00e9 treure l'anella fins que hagin passat 3 mesos. Si necessites treure-la durant m\u00e9s de 2 hores, utilitza un altre m\u00e8tode anticonceptiu durant els 7 dies seg\u00fcents.",
      "tiempo_en_fertilidad": "Un cop deixis l\u2019anella, tornes a ser f\u00e8rtil com abans.",
      "cuando_no_utilizarlo": "Encara no hi ha prou evid\u00e8ncia cient\u00edfica per identificar amb total seguretat les situacions en les quals se'n desaconsella l\u2019\u00fas.",
      "efectos_negativos_de_uso": "Unes 26 dones de cada 100 poden tenir mol\u00e8sties vaginals, i aproximadament 15 de cada 100 es queixen de sagnades vaginals irregulars.",
      "ventajas": "Pot allargar el temps sense regla despr\u00e9s d\u2019un part, ajudant a tractar l\u2019an\u00e8mia en alguns casos.",
      "inconvenientes": "Nom\u00e9s est\u00e0 indicada per a dones que donen el pit.",
      "precio": "Aquest m\u00e8tode no es pot utilitzar a Espanya, ja que encara no hi est\u00e0 comercialitzat."
   },
   "metode_ogino_knaus_metode_calendari_ritme": {
      "funcionamiento": "Determina el inicio y final del per\u00edodo f\u00e9rtil de la mujer mediante el seguimiento, durante un a\u00f1o, de la duraci\u00f3n en d\u00edas de los \u00faltimos 6 a 12 ciclos menstruales.",
      "eficacia": "Por cada 100 mujeres que lo utilizan durante un a\u00f1o, entre 76 y 86 no quedan embarazadas.",
      "cambios_en_la_regla": "No interfiere en la naturaleza del ciclo ni utiliza ninguna sustancia que pueda modificarlo, por lo tanto, no genera cambios en la regla.",
      "como_se_utiliza": "- Se realiza un seguimiento durante un a\u00f1o de la duraci\u00f3n en d\u00edas de los \u00faltimos 12 ciclos menstruales. - Una vez identificado el ciclo menstrual m\u00e1s corto y el m\u00e1s largo: - Se restan 18 d\u00edas al ciclo m\u00e1s corto para obtener el primer d\u00eda f\u00e9rtil. - Se restan 11 d\u00edas al ciclo m\u00e1s largo para obtener el \u00faltimo d\u00eda f\u00e9rtil. - Se recomienda evitar las relaciones sexuales sin protecci\u00f3n entre el primer y el \u00faltimo d\u00eda f\u00e9rtil.",
      "mal_uso_o_rotura": "Este m\u00e9todo no afecta la recuperaci\u00f3n de la fertilidad, ya que se basa en la observaci\u00f3n del ciclo y permite, adem\u00e1s, usar el conocimiento de los d\u00edas f\u00e9rtiles para planificar embarazos si as\u00ed se desea.",
      "tiempo_en_fertilidad": "- No has recibido un entrenamiento previo que permita conocer bien el m\u00e9todo y el funcionamiento de tu organismo. - Tienes ciclos ov\u00e1ricos muy irregulares, ya que puede ser complicado ponerlo en pr\u00e1ctica.",
      "cuando_no_utilizarlo": "- Favorece el autoconocimiento del ciclo ov\u00e1rico y su funcionamiento. - No tiene efectos secundarios. - Facilita la participaci\u00f3n e implicaci\u00f3n de la pareja en la anticoncepci\u00f3n. - Es un m\u00e9todo aut\u00f3nomo y sin costo.",
      "efectos_negativos_de_uso": "- No protege contra infecciones de transmisi\u00f3n sexual. - Puede ser complejo cumplir con los per\u00edodos de abstinencia, que en algunas parejas pueden ser muy largos. Sin embargo, este m\u00e9todo puede complementarse con un m\u00e9todo de barrera.",
      "ventajas": "No tiene m\u00e1s coste que el esfuerzo personal para calcular y abstenerse de tener relaciones sexuales en los d\u00edas indicados.",
      "inconvenientes": "",
      "precio": ""
   },
   "anticonceptius_orals_progestagens": {
      "funcionamiento": "Aquestes hormones eviten que els ovaris fabriquin \u00f2vuls i fan que el flux sigui m\u00e9s esp\u00e8s, impedint l\u2019embar\u00e0s. Tamb\u00e9 dificulten la mobilitat dels espermatozoides.",
      "eficacia": "Te\u00f2ricament, de 100 dones que utilitzen aquest m\u00e8tode durant un any, 99,86 no es queden embarassades; en l\u2019\u00fas real, l\u2019efic\u00e0cia es redueix a 91 de cada 100.",
      "cambios_en_la_regla": "Possibilitat de petites sagnades vaginals entre regles, regles irregulars o abs\u00e8ncia de regla durant alguns mesos (menys de 10 dones de cada 100).",
      "como_se_utiliza": "S\u00f3n pastilles que s\u2019han de prendre cada dia a la mateixa hora.",
      "mal_uso_o_rotura": "- Si el retard no arriba a les 3 hores, pren la p\u00edndola quan te\u2019n recordis. No cal prendre altres precaucions. - Per retard de m\u00e9s de 3 hores, segueix instruccions.",
      "tiempo_en_fertilidad": "Una vegada deixis les pastilles, tornes a ser f\u00e8rtil com abans.",
      "cuando_no_utilizarlo": "Antecedents m\u00e8dics espec\u00edfics com ictus, infarts, co\u00e0guls, lupus, migranyes amb altres s\u00edmptomes, c\u00e0ncer de mama recent, problemes de fetge o medicacions espec\u00edfiques.",
      "efectos_negativos_de_uso": "Inclouen baix risc de co\u00e0guls, n\u00e0usees, mal de cap, acne, dolor o tensi\u00f3 en els pits, quists ov\u00e0rics i erupcions cut\u00e0nies.",
      "ventajas": "S\u00f3n compatibles amb la lact\u00e0ncia.",
      "inconvenientes": "Possibilitat de petites sagnades vaginals entre regles.",
      "precio": "Entre 4 i 15 euros al mes. Alguns estan finan\u00e7ats."
   },
   "metode_lactancia_materna_amenorrea": {
      "funcionamiento": "Este m\u00e9todo natural se basa en que los altos niveles de prolactina (hormona que se segrega en la lactancia) evitan la ovulaci\u00f3n y la aparici\u00f3n de la regla.",
      "eficacia": "Por cada 100 mujeres que lo utilizan durante un a\u00f1o, entre 90 y 98 no quedan embarazadas, seg\u00fan fuentes consultadas. Sin embargo, varias publicaciones reportan una eficacia muy alta, cercana al 98%.",
      "cambios_en_la_regla": "La madre no debe tener la regla desde el parto.",
      "como_se_utiliza": "Se puede seguir este m\u00e9todo si se cumplen las siguientes condiciones: - El beb\u00e9 debe tener menos de 6 meses. - La lactancia materna debe ser exclusiva. - El beb\u00e9 debe mamar durante al menos 100 minutos diarios (5 veces al d\u00eda).",
      "mal_uso_o_rotura": "Este m\u00e9todo no afecta la recuperaci\u00f3n de la fertilidad.",
      "tiempo_en_fertilidad": "Ninguno, ya que respeta la naturaleza de los ciclos de cada mujer.",
      "cuando_no_utilizarlo": "- Favorece el autoconocimiento del ciclo ov\u00e1rico y su funcionamiento. - No tiene efectos secundarios. - Facilita la participaci\u00f3n e implicaci\u00f3n de la pareja en la anticoncepci\u00f3n. - Es un m\u00e9todo aut\u00f3nomo y sin costo.",
      "efectos_negativos_de_uso": "- Es dif\u00edcil de cumplir por los estrictos requisitos de lactancia. - La eficacia disminuye a los 3 meses postparto. - No protege contra las infecciones de transmisi\u00f3n sexual.",
      "ventajas": "No tiene m\u00e1s costo que el esfuerzo personal requerido por las condiciones del m\u00e9todo.",
      "inconvenientes": "",
      "precio": ""
   },
   "anella_vaginal": {
      "funcionamiento": "Aquestes hormones eviten que els ovaris fabriquin \u00f2vuls i fan que el fluix sigui m\u00e9s esp\u00e8s, creant una barrera que impedeix la fecundaci\u00f3 de l\u2019\u00f2vul.",
      "eficacia": "Te\u00f2ricament, de 100 dones que utilitzen aquest m\u00e8tode durant un any, 98,77 no es queden embarassades; en l\u2019\u00fas real, l\u2019efic\u00e0cia es redueix a 91 de cada 100.",
      "cambios_en_la_regla": "La regla ve cada 28 dies i \u00e9s menys dolorosa i menys abundant.",
      "como_se_utiliza": "S\u2019ha de portar posada durant 3 setmanes consecutives i retirar-la a la quarta setmana. Despr\u00e9s de la setmana de descans, es col\u00b7loca de nou i es repeteix el cicle.",
      "mal_uso_o_rotura": "Si l\u2019anella es surt i est\u00e0 fora del cos m\u00e9s de 3 hores, cal reempla\u00e7ar-la i utilitzar un altre m\u00e8tode anticonceptiu durant 7 dies.",
      "tiempo_en_fertilidad": "Una vegada deixis l\u2019anella, tornes a ser f\u00e8rtil com abans.",
      "cuando_no_utilizarlo": "Dones el pit, est\u00e0s en quarantena, ets fumadora major de 35 anys, tens antecedents m\u00e8dics espec\u00edfics o prens certes medicacions.",
      "efectos_negativos_de_uso": "Inclouen risc de co\u00e0guls, augment de pes, n\u00e0usees, problemes a la pell, dolor o tensi\u00f3 als pits, entre altres.",
      "ventajas": "No afectada per v\u00f2mits o diarrea, pot ajudar a regular la regla, millora l\u2019acne, fa que les regles siguin menys doloroses i abundants.",
      "inconvenientes": "Requereix vigil\u00e0ncia per a la correcta col\u00b7locaci\u00f3, alguns f\u00e0rmacs poden alterar-ne l\u2019efic\u00e0cia.",
      "precio": "Entre 11 i 20 euros al mes."
   },
   "pegat_anticonceptiu": {
      "funcionamiento": "Estas hormonas evitan que los ovarios fabriquen \u00f3vulos y hacen que el moco cervical sea m\u00e1s espeso, creando as\u00ed una barrera que impide que los espermatozoides fecunden el \u00f3vulo.",
      "eficacia": "Te\u00f3ricamente, de cada 100 mujeres que utilizan este m\u00e9todo durante un a\u00f1o, 99,7 no quedan embarazadas; en el uso real, la eficacia se reduce a 92 de cada 100. La efectividad del parche puede ser m\u00e1s baja en mujeres con un peso superior a los 90 kg.",
      "cambios_en_la_regla": "La regla viene cada 28 d\u00edas y es menos dolorosa y menos abundante.",
      "como_se_utiliza": "Se debe cambiar el parche cada semana y llevarlo durante 3 semanas consecutivas cada mes. La \u00faltima semana se descansa y viene la regla.",
      "mal_uso_o_rotura": "1. Si el parche que llevabas se ha despegado o te das cuenta de que te deber\u00edas haber puesto el primer parche o cambiado el que llevabas, y a\u00fan no han pasado 24 horas, ponte un parche nuevo, incluso puede ser el mismo, en el mismo lugar lo m\u00e1s pronto posible. Puedes estar tranquila, ya que se mantiene la eficacia anticonceptiva. Contin\u00faa con los cambios de parche como estaba previsto. 2. Si el parche que llevabas se ha despegado o te das cuenta de que te deber\u00edas haber puesto el primer parche o cambiado el que llevabas y han pasado m\u00e1s de 24 horas, p\u00e9gate un parche nuevo en el mismo lugar y comienza un ciclo nuevo de 4 semanas. Ten cuidado porque, en este caso, se ha perdido la eficacia anticonceptiva, por lo que debes seguir otro m\u00e9todo anticonceptivo durante los 7 d\u00edas siguientes al olvido. Si tienes dudas de c\u00f3mo actuar, consulta con tu profesional de la salud.",
      "tiempo_en_fertilidad": "Una vez dejes de colocarte los parches, vuelves a ser f\u00e9rtil como antes.",
      "cuando_no_utilizarlo": "- Est\u00e1s dando el pecho. - Est\u00e1s en cuarentena (despu\u00e9s de un parto). - Eres fumadora y tienes m\u00e1s de 35 a\u00f1os. - Alguna vez has tenido un ictus, infarto de miocardio o co\u00e1gulos de sangre en los pulmones o en las venas de las piernas. - Tienes prevista una operaci\u00f3n y debes guardar reposo durante una temporada larga. - Eres hipertensa. - Tienes lupus. - Padeces migra\u00f1a acompa\u00f1ada de otros s\u00edntomas. - Tienes c\u00e1ncer de mama o lo has tenido en los \u00faltimos 5 a\u00f1os. - Tienes una complicaci\u00f3n cr\u00f3nica de la diabetes. - Eres diab\u00e9tica desde hace m\u00e1s de 20 a\u00f1os. - Tienes problemas de h\u00edgado. - Tienes problemas en la ves\u00edcula biliar (consulta m\u00e9dica). - Tomas alg\u00fan tipo de medicaci\u00f3n (consulta m\u00e9dica).",
      "efectos_negativos_de_uso": "- 10 mujeres de cada 100 tienen n\u00e1useas o v\u00f3mitos. - 25 mujeres de cada 100.000 tienen riesgo de trombosis. - 5 mujeres de cada 100 presentan problemas en la piel como manchas, piel grasa, crecimiento del vello en lugares poco frecuentes o acn\u00e9. - 7 mujeres de cada 1.000 tardan un tiempo, no m\u00e1s de 6 meses, en tener la regla despu\u00e9s de dejar los parches. - 6 mujeres de cada 100 sienten dolor o tensi\u00f3n en los senos. - 2 mujeres de cada 100 padecen alteraciones del estado de \u00e1nimo. - 10 mujeres de cada 100 tienen dolor de cabeza y 5 mujeres de cada 100, tensi\u00f3n arterial alta.",
      "ventajas": "- La eficacia no se ve afectada por v\u00f3mitos o diarrea. - Puede ayudar a regular la regla. - Puede mejorar el acn\u00e9. - Hace que las reglas sean menos dolorosas y menos abundantes. - Si las reglas son muy abundantes, pueden evitar la anemia.",
      "inconvenientes": "- Se debe estar muy pendiente de ponerlo y quitarlo cuando toca. - Puede perder eficacia en mujeres obesas. - Puede moverse y despegarse (esto ocurre en una mujer de cada 100). - Algunos f\u00e1rmacos pueden alterar su eficacia.",
      "precio": "Entre 15 y 20 euros al mes."
   },
   "metode_temperatura_basal": {
      "funcionamiento": "La temperatura corporal oscila entre 36 \u00b0C y 36,6 \u00b0C. A las 25 horas de la salida del \u00f3vulo del ovario, se observa un aumento brusco de la temperatura basal corporal de 0,3 a 0,5 \u00b0C, manteni\u00e9ndose durante tres d\u00edas, marcando el inicio de la fase inf\u00e9rtil del ciclo, que dura hasta el primer d\u00eda de la menstruaci\u00f3n siguiente.",
      "eficacia": "Por cada 100 mujeres que lo usan durante un a\u00f1o, entre 75 y 88 no quedan embarazadas.",
      "cambios_en_la_regla": "Ninguno, ya que no interfiere en la naturaleza del ciclo ni usa sustancias que puedan modificarlo.",
      "como_se_utiliza": "- Se debe medir la temperatura basal v\u00eda rectal o vaginal a partir del quinto d\u00eda del ciclo menstrual, siempre a la misma hora y despu\u00e9s de un descanso continuado de 6-8 horas. - Se recomienda no tener relaciones sexuales sin protecci\u00f3n desde el primer d\u00eda de la menstruaci\u00f3n hasta que la temperatura basal corporal se eleve durante 3 d\u00edas seguidos (fase f\u00e9rtil).",
      "mal_uso_o_rotura": "Este m\u00e9todo no afecta la recuperaci\u00f3n de la fertilidad.",
      "tiempo_en_fertilidad": "- No haces un entrenamiento previo que permita conocer bien el m\u00e9todo y el funcionamiento de tu organismo. - Est\u00e1s en alguna de estas situaciones: enfermedad o fiebre, lactancia o etapa pr\u00f3xima a la menopausia, trabajo por turnos o estr\u00e9s, entre otros.",
      "cuando_no_utilizarlo": "No hay, ya que se basa en la observaci\u00f3n de los signos de fertilidad, respetando la naturaleza de los ciclos de cada mujer.",
      "efectos_negativos_de_uso": "- Favorece el autoconocimiento del ciclo ov\u00e1rico y su funcionamiento. - No tiene efectos secundarios. - Facilita la participaci\u00f3n e implicaci\u00f3n de la pareja en la anticoncepci\u00f3n. - Es un m\u00e9todo aut\u00f3nomo y sin costo.",
      "ventajas": "No protege contra las infecciones de transmisi\u00f3n sexual.",
      "inconvenientes": "El term\u00f3metro y el esfuerzo personal. Hay term\u00f3metros en el mercado que permiten la transmisi\u00f3n autom\u00e1tica de datos de temperatura a una aplicaci\u00f3n a trav\u00e9s de Bluetooth. La aplicaci\u00f3n puede generar curvas de temperatura basal y analizar de forma inteligente la menstruaci\u00f3n, la ovulaci\u00f3n y las fases f\u00e9rtiles.",
      "precio": ""
   },
   "caputxo_cervical": {
      "funcionamiento": "Es un m\u00e9todo de barrera que disminuye la posibilidad de que el semen u otros fluidos secretados por el pene penetren en la cavidad uterina. No protege contra las infecciones de transmisi\u00f3n sexual.",
      "eficacia": "Por cada 100 mujeres que lo utilizan durante un a\u00f1o junto con un espermicida, entre 68 (si ya tienen hijos) y 84 (si nunca los han tenido) no quedan embarazadas. Es m\u00e1s eficaz si la mujer no ha tenido hijos.",
      "cambios_en_la_regla": "No se han descrito cambios en relaci\u00f3n con la regla.",
      "como_se_utiliza": "- Requiere orientaci\u00f3n profesional sobre el modelo y la talla adecuados (peque\u00f1os, medianos y grandes). - Antes de usarlo por primera vez, practica la introducci\u00f3n y verifica su ubicaci\u00f3n. - Se puede insertar desde 15 minutos hasta 42 horas antes de la relaci\u00f3n sexual. - Para un uso correcto: - Aplica una cucharadita de espermicida y exti\u00e9ndelo con un dedo por la parte hueca y plana del borde. - Separa los labios con los dedos de una mano e introd\u00facelo, de modo que el lado que tiene la c\u00fapula y la cinta est\u00e9n hacia abajo. - Empuja el caputxo hasta el fondo. - Una vez colocado, aseg\u00farate de que el cuello quede cubierto. - No lo retires antes de las 6 horas despu\u00e9s de la penetraci\u00f3n para permitir que haga efecto el espermicida, y no lo dejes m\u00e1s de 48-72 horas, seg\u00fan el modelo. - Ret\u00edralo sujetando suavemente el anillo de la parte delantera. - Al sacarlo, l\u00edmpialo con jab\u00f3n neutro y d\u00e9jalo secar al aire. - Gu\u00e1rdalo en la caja o recipiente habitual hasta un nuevo uso. Verifica, antes de cada uso, que la goma no se haya deteriorado (dura unos 2 a\u00f1os). - Gu\u00e1rdalo en un lugar seco, a una temperatura entre 4 \u00b0C y 25\u00b0C.",
      "mal_uso_o_rotura": "Se puede recurrir a los anticonceptivos de emergencia. Los anticonceptivos orales de emergencia son medicamentos que se dispensan en centros de atenci\u00f3n primaria, servicios de urgencias de hospitales y/o farmacias. Deben tomarse lo antes posible, con un poco de agua, y es mejor si van acompa\u00f1ados de un alimento. Como primera opci\u00f3n, hay levonorgestrel de 1,5 mg. Deben tomarse al mismo tiempo uno o dos comprimidos (seg\u00fan el preparado) en una toma \u00fanica, antes de las primeras 72 horas (3 d\u00edas) despu\u00e9s de la relaci\u00f3n sexual de riesgo. Otra opci\u00f3n es el comprimido de ulipristal de 30 mg, que debe tomarse antes de las 120 horas (5 d\u00edas) posteriores al coito, y tambi\u00e9n, para este per\u00edodo, existe la posibilidad de que se coloque un DIU de cobre.",
      "tiempo_en_fertilidad": "El caputxo cervical no afecta la fertilidad de la mujer porque no interfiere en el ciclo ov\u00e1rico.",
      "cuando_no_utilizarlo": "- Tienes alergia a la silicona o al espermicida. - No han pasado al menos 6 meses desde el nacimiento del \u00faltimo hijo. - Hay riesgo de contagio de infecciones de transmisi\u00f3n sexual. - El embarazo es una posibilidad poco o nada asumible en tu situaci\u00f3n actual o personal. - Tienes infecciones vaginales o urinarias frecuentes. - Tienes anomal\u00edas anat\u00f3micas en la vagina o has tenido un prolapso en la zona. - Si est\u00e1s con la regla o presentas sangrado vaginal. - Si est\u00e1s con una infecci\u00f3n vaginal, del cuello del \u00fatero o p\u00e9lvica. - Si tienes antecedentes de enfermedad inflamatoria p\u00e9lvica, s\u00edndrome de shock t\u00f3xico, c\u00e1ncer de cuello uterino u otros problemas que afecten la estructura del cuello del \u00fatero o de la vagina.",
      "efectos_negativos_de_uso": "- Si se utiliza con mucha frecuencia, el espermicida puede provocar irritaciones en la vagina y aumentar el riesgo de contraer una infecci\u00f3n de transmisi\u00f3n sexual. - Si se deja demasiado tiempo, podr\u00eda producir cambios en el flujo o mal olor. - Se describe un mayor riesgo de infecciones de orina. - Algunas usuarias pueden presentar cambios celulares anormales en el cuello del \u00fatero.",
      "ventajas": "- Es un m\u00e9todo que depende de la mujer, facilita que sea la mujer la que inicie la adopci\u00f3n de medidas de protecci\u00f3n. - Hay diferentes tallas. - No interrumpe la relaci\u00f3n sexual. - Es discreto. - No contiene hormonas. - Se puede utilizar durante la lactancia. - Se pueden tener diferentes eyaculaciones con la misma persona sin retirarlo, aunque se recomienda volver a aplicar espermicida, con aplicador, y no es necesario retirarlo inmediatamente despu\u00e9s de la eyaculaci\u00f3n.",
      "inconvenientes": "- No protege contra las infecciones de transmisi\u00f3n sexual. - Tiene una eficacia contraceptiva moderada. - Se necesita asesoramiento profesional, por lo que puede retrasarse la utilizaci\u00f3n por primera vez, una vez decidido el m\u00e9todo. - Se debe cambiar el caputxo en caso de embarazo reciente.",
      "precio": "Este m\u00e9todo no est\u00e1 comercializado en Espa\u00f1a, pero s\u00ed en otros pa\u00edses como Estados Unidos, donde se comercializa como Fem cap. Se puede comprar por Internet y el precio oscila entre los 40 y 60 euros."
   },
   "metode_ciclotermic": {
      "funcionamiento": "Utiliza dos m\u00e9todos combinados para determinar el inicio del per\u00edodo f\u00e9rtil de la mujer: el seguimiento de la duraci\u00f3n en d\u00edas de los \u00faltimos 6 a 12 ciclos menstruales (m\u00e9todo de Ogino-Knaus, m\u00e9todo del ritmo o m\u00e9todo del calendario) y el conocimiento exacto del final del per\u00edodo f\u00e9rtil (m\u00e9todo de la temperatura basal).",
      "eficacia": "Por cada 100 mujeres que lo utilizan durante un a\u00f1o, entre 76 y 86 no quedan embarazadas.",
      "cambios_en_la_regla": "Ninguno, ya que no interfiere en absoluto en la naturaleza del ciclo ni utiliza ninguna sustancia que pueda modificarlo.",
      "como_se_utiliza": "- Seguimiento de la duraci\u00f3n en d\u00edas de los \u00faltimos 6 a 12 ciclos menstruales. - Para reconocer el \u00faltimo d\u00eda f\u00e9rtil, se utiliza el m\u00e9todo de la temperatura basal, midiendo la temperatura basal v\u00eda rectal o vaginal a partir del quinto d\u00eda del ciclo menstrual y siguiendo ciertos criterios hasta determinar el \u00faltimo d\u00eda f\u00e9rtil.",
      "mal_uso_o_rotura": "Este m\u00e9todo no afecta la recuperaci\u00f3n de la fertilidad.",
      "tiempo_en_fertilidad": "- No has realizado un entrenamiento previo que permita conocer bien el m\u00e9todo y el funcionamiento de tu organismo. - Est\u00e1s en alguna de estas situaciones: enfermedad o fiebre, infecciones vaginales, lactancia o etapa pr\u00f3xima a la menopausia, entre otros.",
      "cuando_no_utilizarlo": "Ninguno, ya que es un m\u00e9todo que se basa en la observaci\u00f3n de los signos de fertilidad respetando la naturaleza de los ciclos de cada mujer.",
      "efectos_negativos_de_uso": "- Favorece el autoconocimiento del ciclo ov\u00e1rico y su funcionamiento. - No tiene efectos secundarios. - Facilita la participaci\u00f3n e implicaci\u00f3n de la pareja en la anticoncepci\u00f3n. - Es un m\u00e9todo aut\u00f3nomo y sin costo.",
      "ventajas": "No protege contra las infecciones de transmisi\u00f3n sexual. Puede ser complejo de cumplir debido a los per\u00edodos de abstinencia, que en algunas parejas pueden ser muy largos. No obstante, este m\u00e9todo se puede complementar con un m\u00e9todo de barrera.",
      "inconvenientes": "El term\u00f3metro y el esfuerzo personal. Existen term\u00f3metros en el mercado que permiten la transmisi\u00f3n autom\u00e1tica de los datos de temperatura a una aplicaci\u00f3n a trav\u00e9s de Bluetooth. La aplicaci\u00f3n puede generar curvas de temperatura basal y analizar las fases f\u00e9rtiles de las mujeres",
      "precio": ""
   },
   "diafragma": {
      "funcionamiento": "Es un m\u00e9todo de barrera que disminuye la posibilidad de que el semen u otros fluidos secretados por el pene penetren en la cavidad uterina. No protege contra la transmisi\u00f3n del VIH ni la mayor\u00eda de las infecciones de transmisi\u00f3n sexual.",
      "eficacia": "Por cada 100 mujeres que utilizan este m\u00e9todo junto con un espermicida en sus relaciones, 85 mujeres no quedan embarazadas.",
      "cambios_en_la_regla": "No se han descrito cambios relativos a la regla.",
      "como_se_utiliza": "- Se requiere asesoramiento profesional para orientarte sobre el modelo, tama\u00f1o adecuado y la forma de utilizarlo. - Antes de usarlo por primera vez, practica c\u00f3mo introducirlo y verifica su ubicaci\u00f3n. - Puede insertarse hasta 6 horas antes de la relaci\u00f3n sexual y puede dejarse un m\u00e1ximo de 24 horas, pero no retirarlo antes de las 7 horas despu\u00e9s de la penetraci\u00f3n para permitir que el espermicida haga efecto. - Colocaci\u00f3n: - Aplica una cucharadita de espermicida y exti\u00e9ndelo con un dedo por toda la cavidad del diafragma. - Separa los labios con los dedos de una mano y con la otra presiona el diafragma entre dos dedos e ins\u00e9rtalo profundamente en la vagina. Ajusta con un dedo hasta dejar la parte delantera del anillo detr\u00e1s del hueso p\u00fabico y verifica al mismo tiempo, con el dedo, que el cuello del \u00fatero ha quedado protegido. - Ret\u00edralo sujetando suavemente la parte delantera del anillo. - Al extraerlo, l\u00edmpialo con jab\u00f3n neutro y d\u00e9jalo secar al aire. - Gu\u00e1rdalo en la caja o recipiente habitual hasta un nuevo uso. Verifica, antes de cada uso, que la goma no se haya deteriorado (dura unos 2 a\u00f1os). - Gu\u00e1rdalo en un lugar seco, con una temperatura entre 4 y 25 \u00b0C.",
      "mal_uso_o_rotura": "Se puede recurrir a la anticoncepci\u00f3n de emergencia. Los anticonceptivos orales de emergencia son medicamentos que se dispensan en centros de atenci\u00f3n primaria, servicios de urgencias de hospitales y/o farmacias. Deben tomarse lo antes posible, con un poco de agua, y es mejor si van acompa\u00f1ados de alg\u00fan alimento. Como primera opci\u00f3n, hay levonorgestrel de 1,5 mg. Deben tomarse al mismo tiempo uno o dos comprimidos (seg\u00fan el preparado) en una toma \u00fanica, antes de las primeras 72 horas (3 d\u00edas) despu\u00e9s de la relaci\u00f3n sexual de riesgo. Otra opci\u00f3n es el comprimido de ulipristal de 30 mg, que debe tomarse antes de las 120 horas (5 d\u00edas) posteriores al coito, y tambi\u00e9n, para este per\u00edodo, existe la posibilidad de que se coloque un DIU de cobre.",
      "tiempo_en_fertilidad": "El diafragma no afecta la fertilidad de la mujer, ya que no interfiere en el ciclo ov\u00e1rico.",
      "cuando_no_utilizarlo": "- Tienes alergia al l\u00e1tex, a la silicona o al espermicida. - No han pasado al menos 6 meses desde el nacimiento del \u00faltimo hijo. - Tienes riesgo de contagio de infecciones de transmisi\u00f3n sexual. - El embarazo es una posibilidad poco o nada asumible en tu situaci\u00f3n actual o personal. - Tienes infecciones vaginales o urinarias frecuentes o antecedente de choque s\u00e9ptico. - Tienes anomal\u00edas anat\u00f3micas en la vagina o el cuello, o has tenido un prolapso en la zona.",
      "efectos_negativos_de_uso": "- Si se utiliza con mucha frecuencia, el espermicida puede provocar irritaciones en la vagina y aumentar el riesgo de contraer una infecci\u00f3n de transmisi\u00f3n sexual. - Si se deja demasiado tiempo, podr\u00eda producir cambios en el flujo o mal olor. - Se describe un mayor riesgo de infecciones de orina.",
      "ventajas": "- Viene en diferentes tama\u00f1os (los di\u00e1metros van desde los 50 mm hasta los 105 mm); 75 mm es una medida bastante com\u00fan. - Tiene un costo bajo. - Facilita que sea la mujer la que inicie la adopci\u00f3n de medidas de protecci\u00f3n, una ventaja frente a la reticencia al uso del preservativo. - Es discreto. - No interrumpe la relaci\u00f3n sexual. - No contiene hormonas. - Se puede utilizar durante la lactancia. - Se pueden tener diferentes eyaculaciones con la misma persona sin retirarlo, aunque se recomienda volver a aplicar espermicida.",
      "inconvenientes": "- No protege contra las infecciones de transmisi\u00f3n sexual. - Se necesita asesoramiento profesional para decidir el tama\u00f1o y saber c\u00f3mo utilizarlo, lo que puede retrasar su uso por primera vez, una vez decidido el m\u00e9todo. - Es necesario cambiar el diafragma en caso de cirug\u00eda p\u00e9lvica, cambio considerable de peso o embarazo reciente. - La eficacia depende de la colocaci\u00f3n y ajuste correctos del dispositivo, por lo que es importante usar la talla adecuada a la anatom\u00eda, evitando molestias f\u00edsicas.",
      "precio": "Hay diferentes modelos y presentaciones, y el precio puede variar; se sit\u00faa cerca de los 50 euros."
   },
   "anticonceptius_orals_combinats": {
      "funcionamiento": "Estas hormonas evitan que los ovarios fabriquen \u00f3vulos y, al no haber \u00f3vulos, se impide el embarazo.",
      "eficacia": "Por cada 100 mujeres que utilizan este m\u00e9todo durante un a\u00f1o, te\u00f3ricamente, 99,7 no quedan embarazadas; en el uso real son 91.",
      "cambios_en_la_regla": "Con la mayor\u00eda de preparados, la regla viene cada 28 d\u00edas y es menos dolorosa y menos abundante. Actualmente, tambi\u00e9n hay preparados que permiten tener menos reglas al a\u00f1o.",
      "como_se_utiliza": "Son p\u00edldoras que se deben tomar cada d\u00eda.",
      "mal_uso_o_rotura": "- Si han pasado menos de 12 horas desde la hora de toma habitual, t\u00f3mala tan pronto como te acuerdes y contin\u00faa tomando el resto de p\u00edldoras de forma habitual. No es necesario seguir ning\u00fan otro procedimiento. - Si han pasado m\u00e1s de 12 horas de la hora de toma habitual, o si te has olvidado dos tomas o m\u00e1s, t\u00f3mala lo antes posible y luego contin\u00faa con el resto de p\u00edldoras de forma habitual. Adem\u00e1s, debes utilizar un m\u00e9todo de barrera durante los 7 d\u00edas siguientes al olvido.",
      "tiempo_en_fertilidad": "Una vez dejas las pastillas, vuelves a ser f\u00e9rtil como antes.",
      "cuando_no_utilizarlo": "- Das el pecho. - Est\u00e1s en la cuarentena (despu\u00e9s de un parto). - Eres fumadora y tienes m\u00e1s de 35 a\u00f1os. - Alguna vez has tenido un ictus, infarto de miocardio o co\u00e1gulos de sangre en los pulmones o en las venas de las piernas. - Tienes prevista una operaci\u00f3n y debes guardar reposo durante un tiempo largo. - Eres hipertensa. - Tienes lupus. - Padeces de migra\u00f1a acompa\u00f1ada de otros s\u00edntomas. - Tienes c\u00e1ncer de mama o lo has tenido en los \u00faltimos 5 a\u00f1os. - Tienes una complicaci\u00f3n cr\u00f3nica de la diabetes. - Eres diab\u00e9tica desde hace m\u00e1s de 20 a\u00f1os. - Tienes problemas de h\u00edgado. - Tienes problemas en la ves\u00edcula biliar (consulta m\u00e9dica). - Tomas alg\u00fan tipo de medicaci\u00f3n (consulta m\u00e9dica).",
      "efectos_negativos_de_uso": "- En general, la probabilidad de que tengas alg\u00fan efecto secundario depende de la dosis y el tipo de hormonas que contengan los diferentes preparados. - Entre 5 y 25 mujeres de cada 100.000 tienen riesgo de sufrir una trombosis. - Despu\u00e9s de 6 meses de uso, 8 mujeres de cada 100 aumentan su peso en unos 2 kg. - 10 mujeres de cada 100 tienen n\u00e1useas o v\u00f3mitos. - 5 mujeres de cada 100 presentan problemas en la piel como manchas, piel grasa, crecimiento del vello en lugares poco frecuentes o acn\u00e9. - 7 mujeres de cada 1.000 tardan un tiempo, no m\u00e1s de 6 meses, en tener la regla despu\u00e9s de dejar las pastillas. - 6 mujeres de cada 100 tienen dolor o tensi\u00f3n en los senos. - 2 mujeres de cada 100 sufren alteraciones del estado de \u00e1nimo. - 10 mujeres de cada 100 tienen dolor de cabeza, y unas 5 de cada 100 tienen presi\u00f3n arterial alta.",
      "ventajas": "- Pueden ayudar a regular la regla. - Algunas pastillas mejoran el acn\u00e9. - 50 mujeres de cada 100 o m\u00e1s tienen reglas menos abundantes. - Si tienes reglas muy abundantes, pueden evitar que tengas anemia. - Pueden reducir el riesgo de padecer un c\u00e1ncer de ovario y/o de \u00fatero.",
      "inconvenientes": "- A largo plazo, y si las tomas durante muchos a\u00f1os, pueden aumentar discretamente el riesgo de tener un c\u00e1ncer de mama, especialmente si se comienzan a tomar antes de los 20 a\u00f1os. - Hay que ser muy constante en las tomas y es f\u00e1cil que alg\u00fan d\u00eda te las puedas olvidar. - Aunque son muy efectivas en condiciones ideales, la eficacia real se ve afectada porque no todas las mujeres que las usan las toman correctamente. - Algunos medicamentos pueden alterar su eficacia.",
      "precio": "Entre 4 y 18 euros al mes. Algunas p\u00edldoras est\u00e1n totalmente financiadas."
   },
   "metod_ mucotermic": {
      "funcionamiento": "Utiliza dos m\u00e9todos combinados para determinar el inicio del per\u00edodo f\u00e9rtil de la mujer: el seguimiento de las caracter\u00edsticas del moco cervical (m\u00e9todo de Billings) y el conocimiento exacto del final del per\u00edodo f\u00e9rtil (m\u00e9todo de la temperatura basal).",
      "eficacia": "Por cada 100 mujeres que lo utilizan, entre 75 y 94 no quedan embarazadas.",
      "cambios_en_la_regla": "Ninguno, ya que no interfiere en absoluto en la naturaleza del ciclo ni utiliza ninguna sustancia que pueda modificarlo.",
      "como_se_utiliza": "- Observaci\u00f3n de las caracter\u00edsticas del moco cervical y registro en un gr\u00e1fico o esquema. - Uso del m\u00e9todo de la temperatura basal para identificar el \u00faltimo d\u00eda f\u00e9rtil, con registro de temperatura v\u00eda rectal o vaginal y seguimiento de criterios espec\u00edficos para determinar el \u00faltimo d\u00eda f\u00e9rtil.",
      "mal_uso_o_rotura": "Este m\u00e9todo no afecta la recuperaci\u00f3n de la fertilidad.",
      "tiempo_en_fertilidad": "- No has realizado un entrenamiento previo que permita conocer bien el m\u00e9todo y el funcionamiento de tu organismo. - Est\u00e1s en alguna de estas situaciones: enfermedad o fiebre, infecci\u00f3n vaginal, lactancia o etapa pr\u00f3xima a la menopausia, entre otros.",
      "cuando_no_utilizarlo": "Ninguno, ya que es un m\u00e9todo que se basa en la observaci\u00f3n de los signos de fertilidad respetando la naturaleza de los ciclos de cada mujer.",
      "efectos_negativos_de_uso": "- Favorece el autoconocimiento del ciclo ov\u00e1rico y su funcionamiento. - No tiene efectos secundarios. - Facilita la participaci\u00f3n e implicaci\u00f3n de la pareja en la anticoncepci\u00f3n. - Es un m\u00e9todo aut\u00f3nomo y sin costo.",
      "ventajas": "No protege contra las infecciones de transmisi\u00f3n sexual. Puede ser complejo de cumplir debido a los per\u00edodos de abstinencia, que en algunas parejas pueden ser muy largos. No obstante, este m\u00e9todo se puede complementar con un m\u00e9todo de barrera.",
      "inconvenientes": "El precio del term\u00f3metro. Es un m\u00e9todo que requiere esfuerzo personal. Existen term\u00f3metros en el mercado que pueden transmitir los datos de temperatura autom\u00e1ticamente a una aplicaci\u00f3n mediante Bluetooth, generando curvas de temperatura basal y an\u00e1lisis de fases f\u00e9rtiles.",
      "precio": ""
   },
   "esponja_vaginal": {
      "funcionamiento": "Act\u00faa como barrera bloqueando la entrada al cuello y/o destruyendo los espermatozoides. No protege contra las infecciones de transmisi\u00f3n sexual.",
      "eficacia": "Por cada 100 mujeres que la utilizan durante un a\u00f1o junto con un espermicida, entre 76 (si ya tienen hijos) y 88 (si no los tienen) no quedan embarazadas. Es m\u00e1s eficaz si la mujer no ha tenido hijos.",
      "cambios_en_la_regla": "No se han descrito cambios relativos a la regla.",
      "como_se_utiliza": "- Utiliza una esponja nueva cada vez y sigue adecuadamente los pasos para una utilizaci\u00f3n correcta: - Ins\u00e9rtala inmediatamente o hasta 24 horas antes de la relaci\u00f3n sexual. - L\u00e1vate las manos antes de colocarla. - Una vez fuera del envase, humedece la esponja con agua y esc\u00farrela hasta que est\u00e9 espumosa. - Desliza la esponja dentro de la vagina, emp\u00fajala hasta donde te alcancen los dedos. La esponja se desdobla y cubre el cuello del \u00fatero una vez se suelta. - Una vez colocada la esponja, se pueden mantener relaciones sexuales durante las siguientes 24 horas. - Para retirarla, l\u00e1vate las manos e introduce un dedo en la vagina y, cuando llegues a la cinta, tira de ella poco a poco hacia afuera. - Desecha la esponja usada en la basura.",
      "mal_uso_o_rotura": "Se puede recurrir a la anticoncepci\u00f3n de emergencia. Los anticonceptivos orales de emergencia son medicamentos que se dispensan en centros de atenci\u00f3n primaria, servicios de urgencias de hospitales y/o farmacias. Deben tomarse lo antes posible, con un poco de agua, y es mejor si pueden ir acompa\u00f1ados de un alimento. Como primera opci\u00f3n, hay levonorgestrel de 1,5 mg. Deben tomarse al mismo tiempo uno o dos comprimidos (seg\u00fan el preparado) en una toma \u00fanica, antes de las primeras 72 horas (3 d\u00edas) despu\u00e9s de la relaci\u00f3n sexual de riesgo. Otra opci\u00f3n es el comprimido de ulipristal de 30 mg, que se debe tomar antes de las 120 horas (5 d\u00edas) posteriores al coito, y tambi\u00e9n, para este per\u00edodo, existe la posibilidad de que se coloque un DIU de cobre.",
      "tiempo_en_fertilidad": "No afecta la fertilidad de la mujer porque no interfiere en el ciclo ov\u00e1rico.",
      "cuando_no_utilizarlo": "- Tienes alergia al espermicida (nonoxinol-9) o al poliuretano. - Padeces infecciones de orina frecuentes. - Presentas una infecci\u00f3n vaginal. - Te han diagnosticado s\u00edndrome de shock t\u00f3xico alguna vez. - En los \u00faltimos 6 meses, has tenido un hijo o has sufrido un aborto. - Est\u00e1s con la menstruaci\u00f3n. - Hay riesgo de contraer una infecci\u00f3n de transmisi\u00f3n sexual. - Tienes claro que un embarazo no entra en tus planes.",
      "efectos_negativos_de_uso": "- Puede provocar dolor o irritaci\u00f3n vaginal (por efecto del espermicida). - Aumenta el riesgo de padecer una infecci\u00f3n urinaria o vaginal. - Aumenta el riesgo de padecer el s\u00edndrome de shock t\u00f3xico.",
      "ventajas": "- No necesita receta m\u00e9dica. - Es un m\u00e9todo natural, no contiene hormonas. - No interrumpe la relaci\u00f3n sexual. - Se encuentra en tiendas por Internet, farmacias y/o parafarmacias. - Es f\u00e1cil de usar y ni la mujer ni la pareja la sienten una vez colocada durante la relaci\u00f3n sexual. - Puede ser una alternativa anticonceptiva durante la lactancia.",
      "inconvenientes": "- Es un m\u00e9todo que depende del usuario, por lo que la eficacia depende del uso correcto y algunas mujeres pueden tener dificultades para coloc\u00e1rsela. - No protege contra las enfermedades de transmisi\u00f3n sexual e incluso puede aumentar el riesgo de contraerlas, ya que el espermicida que contiene puede irritar la vagina y facilitar la entrada de g\u00e9rmenes.",
      "precio": "Hay diferentes modelos y presentaciones, y el precio se sit\u00faa cerca de los 5 euros por unidad."
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
    "1": '''A partir del mensaje del usuario busca que enfermedad es la  más parecida a la que se esta preguntando de las siguientes y solo vas a devolver las palabras siguientes en un json con key = "disease" y value = una de la siguientes:
"virus_del_papiloma_huma", "chlamydia", "gonorrea", "sifilis", "tricomoniasis", "herpes_genital", "citomegalovirus", "infecció_por_clamídia_pelvi", "síndrome_de_herpes_toxico", "linfogranuloma_venerico", "lepra", "sifilis_congenita", "sifilis", "vph", "hepatitis_b", "hepatitis_c", "vih".
En caso de que no se encuentre ningun caso que coincida con la pregunta, el value = "error".
No puedes salirte del snipped code y el value de la key debe ser una de las palabras propuestas.''',
    
    "2": '''
A partir del mensaje del usuario sobre pornografía, responde la pregunta de manera objetiva, educativa e informativa, basandote en las siguientes bases de conocimiento:
La pornografia impacta sobre la autoestima ya que la persona que la consume se compara con lo que ve. 
La persona puede tener dificultades para vincularse sexual y afectivamente con otras personas.
Pueden haber casos de disfuncion erectil o dificultades para llegar al orgasmo.
Se refuerzan los estereotipos de genero donde las mujeres se consideran objetos sexuales y estan en posiciones denigradas.
En algunos casos se muestra porno duro donde hay violencia juntamente con sexo. Esto es preocupante ya que se puede llegar a erotizar y normalizar en situaciones de la vida cuotidiana. Esto es sobretodo muy importante de concienciar a adolescentes.
Aunque haya todos estos riesgos y aspectos negativos, la pornografia tambien tiene una cara buena, ya que con un buen uso puede ser una fuente de autoconocimiento.

A parte de responder preguntas, de vez en cuando recuerda que existe un cuestionario de pornografia para poder educarse correctamente sobre el ambito. Esta parte no la vas a repetir si ya lo has enviado en el mensaje anterior.

No puedes salirte del snipped code y el value de la key debe ser una de las palabras propuestas.
    ''',
    "3": '''Eres un experto que solo va a responder preguntas relacionadas con anticonceptivos. En ningún momento te vas a arriesgar dando consejos de medicación, sino que vas a ser el maximo de objetivo respondiendo en todo momento las preguntas del user, y recomendando que en caso que tener patologías parecidas acudir a una consulta con un médico.

Basándote en la pregunta del user vas a escojer el metodo anticonceptivo es más parecido al que se esta preguntando de los siguientes y solo vas a devolver las palabras siguientes en un json con key = "protection" y value = una de la siguientes:

"preservatius_ masculins", "implant_contraceptiu_subdermic", "preservatius_femenins", "dispositiu_intrauteri_hormonal", "dispositiu_intrauteri_no_hormonal", "vasectomia", "lligadura_de_trompes", "anticoncepcio_postcoital_emergencia", "metode_billings_fluidesa_moc_cervical", "metode_simptotermic", "anticonceptius_injectables_progestagens", "anella_vaginal_progestagens", "metode_ogino_knaus_metode_calendari_ritme", "anticonceptius_orals_progestagens", "metode_lactancia_materna_amenorrea", "anella_vaginal", "pegat_anticonceptiu", "metode_temperatura_basal", "caputxo_cervical", "metode_ciclotermic", "diafragma", "anticonceptius_orals_combinats", "metod_ mucotèrmic", "esponja_vaginal".

En caso de que no se encuentre ningun caso que coincida con la pregunta, el value = "error".
No puedes salirte del snipped code y el value de la key debe ser una de las palabras propuestas.
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
    "disease": '''Teniendo en cuenta la enfermedad de la que estamos informando, utiliza su informacion como sintomas, prevencion y tratamiento e informacion extra (maximo 200 palabras de informacion extra) para responder la pregunta sobre el tema formulada por el usuario. La respuesta tiene que ser un texto informativo que resuelva e informe de manera objetiva la pregunta del usuario. Recuerdale al usuario que en casos de tener simptomas o tener consultas mas complejas y personales debe acudir a un medico de manera presencial (solo recordar y enviar este recordatorio si no lo has enviado en los ultimos 3 mensajes).
No puedes salirte del snipped code.'''
}

class Prompts:
    def get_prompt(self, type, key):
        if type == "prompts": return prompts[key]
        elif type == "disease": return disease[key]
        return protection[key]
        