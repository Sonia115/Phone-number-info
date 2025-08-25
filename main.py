import phonenumbers
import opencage
import folium

from myphone import number

from phonenumbers import geocoder, carrier, parse

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)


service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

key = '06904ee445354ecc99456281c505ac8c'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")

pepnumber = parse(number)

print("location:", geocoder.description_for_number(pepnumber, "en"))
print("carrier:", carrier.name_for_number(pepnumber, "en"))