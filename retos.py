import matplotlib.pyplot as plt

# Data for plotting
labels = [
    "ODS 1: Fin de la pobreza",
    "ODS 2: Hambre cero",
    "ODS 4: Educación de calidad",
    "ODS 8: Trabajo decente y crecimiento económico",
    "ODS 9: Industria, innovación e infraestructura",
    "ODS 10: Reducción de las desigualdades",
    "ODS 11: Ciudades y comunidades sostenibles",
    "ODS 12: Producción y consumo responsables",
    "ODS 16: Paz, justicia e instituciones sólidas"
]
sizes = [8.00, 4.00, 4.00, 12.00, 4.00, 4.00, 16.00, 4.00, 44.00]
colors = [
    "#E5243B",  # ODS 1
    "#DDA63A",  # ODS 2
    "#C5192D",  # ODS 4
    "#A21942",  # ODS 8
    "#FF3A21",  # ODS 9
    "#DD1367",  # ODS 10
    "#FD6925",  # ODS 11
    "#BF8B2E",  # ODS 12
    "#00689D"   # ODS 16
]

# Plotting the pie chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title of the pie chart
plt.title('Porcentaje de cada ODS dentro del conjunto de retos')

# Save the plot as an image file
plt.savefig("ods_percentage_pie_chart_colored.png")

# Show the plot
plt.show()
