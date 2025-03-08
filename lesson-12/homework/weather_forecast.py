from bs4 import BeautifulSoup

with open('weather.html','r') as file:
    html_docs=file.read()

soup=BeautifulSoup(html_docs,'html.parser')

table_rows=soup.find_all('tr')[1:]

forecasts=[]

#Output all the value 
for row in table_rows:
    columns=row.find_all('td')
    days=columns[0].text
    temp=columns[1].text
    condition=columns[2].text
    # print(f"{days}, {temp}, {condition}")
    forecasts.append({"Day": days, "Temperature": temp, "Condition": condition})

#to find the highest temperature 
highest_temp_entry = max(forecasts, key=lambda forecast: int(forecast['Temperature'].replace('В°C', '')))

#function to output the sunny days
def sunny_days():
    """returns sunny days"""
    for forecast in forecasts:
        if forecast['Condition']=='Sunny':
            print(f"{forecast}")



for forecast in forecasts:
    print(forecast)

print(f"Day with highest temperature {highest_temp_entry["Day"]} and temperature is {highest_temp_entry["Temperature"]}")

print("Sunny days:")
sunny_days()





