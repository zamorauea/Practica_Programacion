import numpy as np

# Declaración de variables tridimensionales y asignación de valores de texto
array_2x3x3 = np.array([
    [["texto11", "texto12", "texto13"],
     ["texto21", "texto22", "texto23"],
     ["texto31", "texto32", "texto33"]],

    [["texto41", "texto42", "texto43"],
     ["texto51", "texto52", "texto53"],
     ["texto61", "texto62", "texto63"]]
])

array_5x5x4 = np.array([
    [["texto111", "texto112", "texto113", "texto114"],
     ["texto121", "texto122", "texto123", "texto124"],
     ["texto131", "texto132", "texto133", "texto134"],
     ["texto141", "texto142", "texto143", "texto144"],
     ["texto151", "texto152", "texto153", "texto154"]],

    [["texto211", "texto212", "texto213", "texto214"],
     ["texto221", "texto222", "texto223", "texto224"],
     ["texto231", "texto232", "texto233", "texto234"],
     ["texto241", "texto242", "texto243", "texto244"],
     ["texto251", "texto252", "texto253", "texto254"]],

    [["texto311", "texto312", "texto313", "texto314"],
     ["texto321", "texto322", "texto323", "texto324"],
     ["texto331", "texto332", "texto333", "texto334"],
     ["texto341", "texto342", "texto343", "texto344"],
     ["texto351", "texto352", "texto353", "texto354"]],

    [["texto411", "texto412", "texto413", "texto414"],
     ["texto421", "texto422", "texto423", "texto424"],
     ["texto431", "texto432", "texto433", "texto434"],
     ["texto441", "texto442", "texto443", "texto444"],
     ["texto451", "texto452", "texto453", "texto454"]],

    [["texto511", "texto512", "texto513", "texto514"],
     ["texto521", "texto522", "texto523", "texto524"],
     ["texto531", "texto532", "texto533", "texto534"],
     ["texto541", "texto542", "texto543", "texto544"],
     ["texto551", "texto552", "texto553", "texto554"]]
])

array_3x6x1 = np.array([
    [["texto1111"],
     ["texto1121"],
     ["texto1131"],
     ["texto1141"],
     ["texto1151"],
     ["texto1161"]],

    [["texto1211"],
     ["texto1221"],
     ["texto1231"],
     ["texto1241"],
     ["texto1251"],
     ["texto1261"]],

    [["texto1311"],
     ["texto1321"],
     ["texto1331"],
     ["texto1341"],
     ["texto1351"],
     ["texto1361"]]
])

# Imprimir los arrays para verificar los valores asignados
print("Array 2x3x3:")
print(array_2x3x3)
print("Array 5x5x4:")
print(array_5x5x4)
print("Array 3x6x1:")
print(array_3x6x1)
