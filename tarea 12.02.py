 # crear matrix 3 d para guardar datos
 # primera dimension:ciudades (3 ciudades )
 # segunda dimension:semanas (3 semanas )
 # tercera dimension:dias de la semana (7 dias de la semana )
 > temperaturas =[
    [# ciudades 1 Edimburgo
      [semana 1
    { "day": "lunes","tem": 13},
    { "day": "martes", "tem":10},
    { "day": "miercoles", "tem":16},
    { "day": "jueves", "tem": 12},
    { "day":  "viernes","tem": 7},
    { "day":   "sabado"," tem": 18},
    { "day":  "domingo","tem": 19},
     ],
        [semana 2
         {"day": "lunes", "tem": 15},
         {"day": "martes", "tem": 17},
         {"day": "miercoles","tem": 16},
         {"day": "jueves", "tem": 11},
         {"day": "viernes", "tem":8},
         {"day": "sabado", " tem": 10},
         {"day": "domingo", "tem": 13},
         ],
        [semana 3
         {"day": "lunes", "tem": 17},
         {"day": "martes", "tem": 15},
         {"day": "miercoles","tem": 21},
         {"day": "jueves", "tem": 19},
         {"day": "viernes", "tem":24},
         {"day": "sabado", " tem": 17},
         {"day": "domingo", "tem": 20},
         ],
          [#ciudades 2 paris
        [semana 1
    {"day":"lunes","tem":20},
    { "day":"martes","tem":18},
    { "day":"miercoles","tem":21},
    { "day":"jueves","tem": 22},
    { "day":"viernes","tem": 20},
    { "day":"sabado","tem": 17},
    { "day": "domingo","tem": 19},
    ],
    [semana 2
     {"day": "lunes", "tem": 23},
     {"day": "martes", "tem": 17},
     {"day": "miercoles", "tem": 22},
     {"day": "jueves", "tem": 21},
     {"day": "viernes", "tem": 21},
     {"day": "sabado", "tem": 24},
     {"day": "domingo", "tem": 25},
      ],
    [semana 3
    {"day": "lunes", "tem": 24},
    {"day": "martes", "tem": 19},
    {"day": "miercoles", "tem": 23},
     {"day": "jueves", "tem": 20},
    {"day": "viernes", "tem": 14},
    {"day": "sabado", "tem": 26},
    {"day": "domingo", "tem": 28},
    ],

              [#ciudad 3 cuenca
      [semana 1
    {"day":"lunes","tem":11},
    { "day":"martes","tem":18},
    { "day":"miercoles","tem":22},
    { "day":"jueves","tem": 23},
    { "day":"viernes","tem": 24},
    { "day":"sabado","tem": 23},
    { "day": "domingo","tem": 24},
    ],
      [semana 2
     {"day":"lunes","tem":19},
     { "day":"martes","tem":23},
     { "day":"miercoles","tem":25},
     { "day":"jueves","tem": 24},
     { "day":"viernes","tem": 28},
     { "day":"sabado","tem": 27},
     { "day": "domingo","tem": 23},
     ],
    [semana 3
     {"day": "lunes", "tem": 25},
    {"day": "martes", "tem": 27},
     {"day": "miercoles", "tem": 16},
    {"day": "jueves", "tem": 14},
    {"day": "viernes", "tem": 12},
    {"day": "sabado", "tem": 10},
    {"day": "domingo", "tem": 15},
     ],
       # calcular el promedio de las temperaturas para cada ciudad y semana
      for ciudad in temperaturas :
       for semana in ciudad :
           suma=0
           for dia in semana :
               suma += dias ["temp"]
          print(suma)


           wile true :
           print("seleccione una ciudad ")
              print(" 1.ciudad 1")
                print(" 2.ciudad 2")
                  print(" 3.ciudad 3")
                 print(" 4 .salir")
                  opcion= imput("ingrese la opcion deseada  ")
                  if opcion == "1":
                      ciudad = temperaturas [0]
                  else : ciudad = temperaturas [1]
                  print(ingrese la opcion deseada )
                  continue

