import pandas as pd
import django
django.setup()
from pedido.views import *

data = pd.read_csv("datos.csv")
dates = pd.to_datetime(data['Fecha'],format="%d/%m")
for i in range(len(dates)):
    dates[i] = dates[i].replace(year=2018)
data['Fecha'] = dates

for i in range(len(data)):
    new_pedido( data['Fecha'][i], data['Paciente'][i],data['Nro Afiliado'][i],data['DNI'][i],
                data['Medicacion'][i], data['Forma'][i],data['Dosis'][i],data['Medico'][i],
                data['Farmacia'][i], data['Direccion'][i])

    #print data['Fecha'][i], data['Paciente'][i],data['Medicacion'][i],data['Farmacia'][i]

