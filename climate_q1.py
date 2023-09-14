import matplotlib.pyplot as plt
import sqlite3 

connection = sqlite3.connect('climate.db')
cur = connection.cursor()

years = []
co2 = []
temp = []

yearInsert = (" SELECT YEAR FROM ClimateData; ")

for row in cur.execute(yearInsert):
    years.append(row)
    
co2Insert = (" SELECT CO2 FROM ClimateData; ")

for row in cur.execute(co2Insert):
    co2.append(row)
    
TempInsert = (" SELECT Temperature FROM ClimateData; ")

for row in cur.execute(TempInsert):
    temp.append(row)
    
  
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 


connection.close()