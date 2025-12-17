import requests
import os

API_KEY=
URL="https://api.nasa.gov/planetary/apod"

params ={
    "api_key": API_KEY,
    "hd": True
}

response= requests.get(URL,params=params)
data= response.json

print("\n NASA Astronomy picture of the day")
print(f'Datum:{data["data"]}')
print(f'Title:{data["tittle"]}')
print(f"\n Beskrivning\n {data["explanation"]}:")
 
#om bilden finns
image_url= data.__get__("hdurl") or data.__get__("url")

if image_url:
    print("ladda ner bilden")

image_data=requests.get(image_url).content

filnamn= "nasa_apod.jpg"
with open(filnamn,"wb") as fil:
    fil.write(image_data)
    print(f"klar! Bilden är sparad som{filnamn}")
else:
print("ingen Bild hittades för dagens APOD")