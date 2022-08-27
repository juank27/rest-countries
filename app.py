import requests
import json

def getData(url):
   r = requests.get(url)
   if r.status_code == 200:
      return r.json()
   return None

#generate json
def generateJSON(data):
   data_json = {}
   for i in data:
      try:
         aux = {}
         #data_json[i['name']['common']] = i['name']['common']
         #print(i['region'])
         #print(i['subregion'])
         aux['region'] = i['region']
         aux['language'] = i['languages']
         name = i['name']['common']
         data_json[name] = aux
      except:
         pass
   return data_json

#execution time
def time():
   pass

#encrypt data whith sha1
def encriptarSHA1(country):
   pass


#Create DataFrame
def createDataFrame(data):
   pass

#save result
def saveResult(data):
   pass

#save json
def saveJSON(data):
   pass


data = getData('https://restcountries.com/v3.1/all')
#print(data)

print('---------------------------------------------------------------')
region = data[0]['region']
country = data[0]['name']['common']
language = data[0]['languages']
print(region)
print(country)
print(language)
print('---------------------------------------------------------------')
print('Ejecucion organizada')
print(json.dumps(generateJSON(data), indent=3))

'''
#este me funciona para generar eel JSOn y pasarlo a un documento
response_json = json.loads(data)
response_json = json.dumps(response_json, indent=3)
print(response_json)
'''

