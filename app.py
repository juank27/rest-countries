import time
import requests
from werkzeug.security import generate_password_hash, check_password_hash
import json
import pandas as pd

#get data
def getData(url):
   r = requests.get(url)
   if r.status_code == 200:
      return r.json()
   return None

#generate json
def generateJSON(data, time=time):
   data_json = {}
   for i in data:
      try:
         start = time.time()
         aux = {}
         aux['region'] = i['region']
         name = i['name']['common']
         encrypt = encryptSHA1(keys(i['languages']))
         aux['language'] = encrypt
         aux['time'] = (time.time() - start)
         data_json[name] = aux
      except:
         pass
   return data_json

#keys
def keys(language):
   concat_lenguage = ''
   for i in language:
      value = language[i]
      concat_lenguage += value + '-'
   return concat_lenguage

#execution time
def time():
   pass

#encrypt data whith sha1
def encryptSHA1(language):
   encrypt = generate_password_hash(language, 'sha1')
   return encrypt

#veryfy encrypt
def verifySHA1(encrypt, country):
   encrypt_result = check_password_hash(encrypt, country)
   return encrypt_result

#Create DataFrame
def createDataFrame(data, time=time):
   df = pd.DataFrame(columns=['Region', 'City Name', 'Language', 'Time'])
   aux = 1
   for i in data:
      df.loc[aux] = [data[i]['region'], i, data[i]['language'], data[i]['time']]
      aux += 1
   return df

#save result
def saveResult(data):
   pass

#save json
def saveJSON(data):
   file = open('data.json', 'w')
   file.write(data)
   file.close()

#operations time
def operaciones(data):
   aux = {}
   n = 0
   for i in data:
      aux[n] = data[i]['time']
      n += 1
   serie = pd.Series(aux)
   result = {
      'total': serie.sum(),
      'promedio': serie.mean(),
      'min': serie.min(),
      'max': serie.max(),
   }
   return result

#main
def main():
   data = getData('https://restcountries.com/v3.1/all')
   data_generate = generateJSON(data)
   print(createDataFrame(data_generate))
   print(operaciones(data_generate))
   saveJSON(json.dumps(data_generate, indent=2))


if __name__ == '__main__':
   main()
