from multiprocessing import connection
import time
import requests
from werkzeug.security import generate_password_hash, check_password_hash
import json
import pandas as pd
import sqlite3

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

#create data base
def create_data_base(data_base):
   conection = sqlite3.connect(data_base)
   try:
      conection.execute('''
                        CREATE TABLE time (
                           id INTEGER primary key autoincrement,
                           total TEXT,
                           promedio TEXT,
                           min TEXT,
                           max TEXT)
                        ''')
      print('Data base created')
   except sqlite3.OperationalError:
      print('Table already exists')
   conection.close()

#save data base time operation
def save_operation(data_base,data):
   conection = sqlite3.connect(data_base)
   try:
      conection.execute('INSERT INTO time (total, promedio, min, max) VALUES (?, ?, ?, ?)', (data['total'], data['promedio'], data['min'], data['max']))
      conection.commit()
   except sqlite3.OperationalError as e:
      print('Error', e)
   conection.close()

#get data time sqlite
def get_data_time(data_base):
   conection = sqlite3.connect(data_base)
   cursor = conection.execute('SELECT total, promedio, min, max FROM time')
   for i in cursor:
      print(i) # -> (total, promedio, min, max)
   conection.close()

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
   time_operation = operaciones(data_generate)
   saveJSON(json.dumps(data_generate, indent=2))
   create_data_base('data.db')
   save_operation('data.db', time_operation)
   print(get_data_time('data.db'))


if __name__ == '__main__':
   main()
