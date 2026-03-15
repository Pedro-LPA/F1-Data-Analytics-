import requests 
import json
import pandas as pd

dados_f1 = requests.get("https://api.jolpi.ca/ergast/f1/drivers.json")
dados_convertidos = dados_f1.json()

df = pd.DataFrame(dados_convertidos)
df