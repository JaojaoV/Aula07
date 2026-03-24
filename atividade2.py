# ao invés de 'import xml.etree.ElementTree as ET'
import csv
import io

class SistemaCSV:
  def get_dados_csv(self):
    return "nome,idade\nJoao,30"

class InterfaceJSON:
    def get_dados(self):
        pass

import json

class CSVparaJSONAdapter(InterfaceJSON):
  def __init__(self, sistema_csv):
    self.sistema_csv = sistema_csv

  def get_dados(self):
    csv_data = self.sistema_csv.get_dados_csv()
    root = io.StringIO(csv_data)

    leitor = csv.DictReader(root)
    dados = next(leitor)

    return json.dumps(dados)

sistema_legado = SistemaCSV()
adaptador = CSVparaJSONAdapter(sistema_legado)

print(adaptador.get_dados())