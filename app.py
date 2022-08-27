import requests
from werkzeug.security import generate_password_hash, check_password_hash
import json
import pandas as pd

def getData(url):
   r = requests.get(url)
   if r.status_code == 200:
      return r.json()
   return None

import time
#generate json
def generateJSON(data, time=time):
   data_json = {}
   for i in data:
      try:
         start = time.time()
         aux = {}
         aux['region'] = i['region']
         name = i['name']['common']
         encrypt= encryptSHA1(keys(i['languages']))
         aux['language'] = encrypt
         aux['time'] = ("{:.6f}".format(time.time() - start))
         data_json[name] = aux
         #print(data_json)
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

#veryfy
def verifySHA1(encrypt,country):
   encrypt_result = check_password_hash(encrypt, country)
   return encrypt_result

#Create DataFrame
#https://pandas.pydata.org/docs/reference/api/pandas.concat.html
#https://www.youtube.com/watch?v=HXaZfvkF16I
def createDataFrame():
   #df = pd.DataFrame(columns=['Region', 'City Name', 'Language', 'Time'])
   df = pd.DataFrame()
   df['first_name'] = ['Josy', 'Vaughn', 'Neale', 'Teirtza']
   df['last_name'] = ['Clarae', 'Halegarth', 'Georgievski', 'Teirtza']
   df['gender'] = ['Female', 'Male', 'Male', 'Female']
   print(df)

#save result
def saveResult(data):
   pass

#save json
def saveJSON(data):
   file = open('data.json', 'w')
   file.write(data)
   file.close()

def main():
   data = getData('https://restcountries.com/v3.1/all')
   data_generate = json.dumps(generateJSON(data), indent=3)
   saveJSON(data_generate)




# #print(data)
# data2 = json.dumps(generateJSON(data), indent=3)
# encrypt = encryptSHA1('Argentina')
# print(check_password_hash(encrypt, 'Argentina'))

# #saveJSON(data2)

#createDataFrame()

'''
#este me funciona para generar eel JSOn y pasarlo a un documento
response_json = json.loads(data)
response_json = json.dumps(response_json, indent=3)
print(response_json)
'''
# import time

# start = time.time()



# end = time.time()

# print(format(end-start))

if __name__ == '__main__':
   main()
