import matplotlib.pyplot as plt
import numpy as np


pontos_turisticos = [
    "Avenida Beira Mar",
    "Praia do Futuro",
    "Centro Dragão do Mar",
    "Mercado Central",
    "Parque do Cocó",
    "Praia de Iracema",
    "Feirinha da Beira Mar",
    "Catedral Metropolitana",
    "Museu do Ceará",
    "Estátua de Iracema"
]


faixa_etaria_0_17 = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
faixa_etaria_18_35 = [150, 135, 120, 105, 90, 75, 60, 45, 30, 15]
faixa_etaria_36_50 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
faixa_etaria_51_65 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
faixa_etaria_66_plus = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]


barWidth = 0.85
r = np.arange(len(pontos_turisticos))
    
plt.figure(figsize=(14, 8))
plt.barh(r, faixa_etaria_0_17, color='skyblue', edgecolor='grey', height=barWidth, label='0-17 anos')
plt.barh(r, faixa_etaria_18_35, left=faixa_etaria_0_17, color='lightgreen', edgecolor='grey', height=barWidth, label='18-35 anos')
plt.barh(r, faixa_etaria_36_50, left=np.add(faixa_etaria_0_17, faixa_etaria_18_35), color='orange', edgecolor='grey', height=barWidth, label='36-50 anos')
plt.barh(r, faixa_etaria_51_65, left=np.add(np.add(faixa_etaria_0_17, faixa_etaria_18_35), faixa_etaria_36_50), color='pink', edgecolor='grey', height=barWidth, label='51-65 anos')
plt.barh(r, faixa_etaria_66_plus, left=np.add(np.add(np.add(faixa_etaria_0_17, faixa_etaria_18_35), faixa_etaria_36_50), faixa_etaria_51_65), color='purple', edgecolor='grey', height=barWidth, label='66+ anos')

plt.xlabel('Número de Visitantes (milhares)')
plt.title('Pontos Turísticos Mais Movimentados de Fortaleza por Faixa Etária')
plt.yticks(r, pontos_turisticos)
plt.legend(loc='upper right')
plt.gca().invert_yaxis()  
plt.tight_layout()

plt.savefig('pontos_turisticos_fortaleza_faixa_etaria.png')


plt.show()
