import requests
from werkzeug.security import generate_password_hash, check_password_hash
import json
import pandas as pd
import time

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
         aux['region'] = i['region']
         aux['language'] = i['languages']
         name = i['name']['common']
         data_json[name] = aux
      except:
         pass
   print('Time: ', end - start)
   return data_json

#execution time
def time():
   pass

#encrypt data whith sha1
def encryptSHA1(country):
   encrypt = generate_password_hash(country, 'sha1')
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
   generateJSON(data)




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

n = time.time()
main()
end = time.time()
print('Time: ', end - n)
# if __name__ == '__main__':
#    n = time.time()
#    main()
#    end = time.time()
#    print('Time: ', end - n)
