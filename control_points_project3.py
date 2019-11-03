# Control points for making routes
control_points = [[-43, 25],     # 0: Intersection of Pirogova and Univer Prospect
                  [-60, 4],      # 1: Turning point in the forest
                  [-64, 1],      # 2: Exit off the forest
                  [-65, -3],     # 3: Khan-Buz location
                  [-39, 20],     # 4: Midpoint point on Ilyicha St (before Teahuppo)
                  [-39, 19],     # 5: Turning point from Ilyicha to Teahuppo
                  [-43, 11],     # 6: Turning point straight to Teahuppo
                  [-42, 10],     # 7: Correcting way to Teahuppo
                  [-41, 10],     # 8: Teahuppo location
                  [-30, 29],     # 9: Turning point to Co.mein from Univer Porspect
                  [-30, 28],     # 10: Co.mein location
                  [-27, 4],      # 11: Turning point from Ilyicha to Rybaris
                  [-30, 3],      # 12: Rybaris location
                  [-19, -6],     # 13: Turning point from Ilyicha to Vilka-Lozhka
                  [-21, -8],     # 14: Crossroads to Vilka and Pechki
                  [-22, -9],     # 15: Vilka-Lozhka location
                  [-21, -11],    # 16: Pechki-Lavochki location
                  [-64, -4],     # 17: Uncle Dohner location
                  [-40, 9],      # 18: Spot&Choose location
                  [-34, 13],     # 19: Turning point from Ilyicha to Pochta
                  [-37, 11],     # 20: Sparks location
                  [-34, 6],      # 21: Turning point before Fabrika Pizza
                  [-35, 5],      # 22: Fabrika Pizza and Pick-Up Coffee
                  [-25, 1],      # 23: Turning point from Ilyicha to Shurubor
                  [-28, -1],     # 24: Shurubor location
                  [0, -32],      # 25: Intersection of Ilyicha and Morskoy
                  [-4, -35],     # 26: Turning point from Morskoy to Kuzina
                  [-5, -34],     # 27: Kuzina and Puerto location
                  [-15, -43.5],  # 28: Turning point from Morskoy to Clever
                  [-16, -42],    # 29: Clever location
                  [32, -7],      # 30: Turning point from Morskoy to Coffee Collective
                  [31, -6],      # 31: Coffee Collective location
                  [42, 0],       # 32: Turning point from Morskoy to Cinnabon
                  [41, 1],       # 33: Cinnabon location
                  [45, 3],       # 34: Turning point from Morskoy to Dudnik
                  [45, 4],       # 35: Dudnik location
                  [54, 10],      # 36: Turning point from MOrskoy to Myasoroob
                  [53, 11],      # 37: Myasoroob and Coffee Academy location
                  [-22, 31.5],   # 38: Point before turning to Art-Pub
                  [-15.5, 24],   # 39: Second point before turn to
                  [7, 20],       # 40: Turning point just before the Pub
                  [16, 20]]      # 41: Art-Pub location

# Dictionary of routes based on control points
paths = {'Khan-Buz': [0, 1, 2, 3],
         'Uncle Dohner': [0, 1, 2, 3, 17],
         'Teahuppo': [0, 4, 5, 6, 7, 8],
         'Spot&Choose': [0, 4, 5, 6, 7, 18],
         'Co.mein': [0, 9, 10],
         'Rybaris': [0, 11, 12],
         'Vilka-Lozhka': [0, 11, 13, 14, 15],
         'Pechki-Lavochki': [0, 11, 13, 14, 16],
         'Sparks': [0, 4, 19, 20],
         'Fabrika Pizza': [0, 4, 19, 20, 21, 22],
         'Pick-Up Coffee': [0, 4, 19, 20, 21, 22],
         'Shurubor': [0, 11, 23, 24],
         'Kuzina': [0, 25, 26, 27],
         'Puerto': [0, 25, 26, 27],
         'Clever': [0, 25, 28, 29],
         'Coffee Collective': [0, 25, 30, 31],
         'Cinnabon': [0, 25, 32, 33],
         'Dudnik': [0, 25, 34, 35],
         'Myasoroob': [0, 25, 36, 37],
         'Coffee Academy': [0, 25, 36, 37],
         'Art-Pub': [0, 38, 'c', 39, 'c', 40, 41],
         'Murchim': []}

circles = [[-15, 70],
           [15, 60]]