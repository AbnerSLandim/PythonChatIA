import os
import pandas as pd
from pandasai import SmartDataframe

os.environ["PANDASAI_API_KEY"] = '$2a$10$soLVqGBJEVUlkOi68YKFMemJEtcMnG5rFdg3YPbqWyXUo2DrSWlj6'


























vendas_por_pais = pd.DataFrame({
    "países": ["Estados Unidos", "Reino Unido", "França", "Alemanha", "Italia", "Espanha", "Canada", "Australia", "Japão", "China"],
    "vendas": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]
})


agent = SmartDataframe(vendas_por_pais)

print(agent.chat('Imprimir tabela'))

print(agent.chat('Quais os 3 países que mais venderam?'))
print(agent.chat('Quais os 3 países que menos venderam?'))
print(agent.chat('Quantas vendas a China teve a mais que o Japão?'))


