# rest-countries

Desarrollo de una aplicación en Python que genera un DataFrame con datos **Region**, **City**, **Name**, **Languaje**, Time con la librería PANDAS.
| Region | City Name | Language | Time |
|--|--|--|--|
| Europe| Finland|sha1$fkr5rzLNRf2oA901$521c24960009b0b9d796893b... | 0.000122 |
| Americas| Guatemala| sha1$aItFgNyJmQ3pvmRh$7e3c63fe58b4b900999a743e...| 0.000047 |

- Los datos fueron obtenidos de [https://restcountries.com/](https://restcountries.com/).
- Se encripto el lenguaje en SHA1, para este se utilizo la librería werkzeug, creando una función para generar
el SHA1 y o otra función para verificar el origen de la encriptación.

>Para la encriptación del lenguaje, se utilizo una función para concatenar donde exista mas de un lenguaje y es separado por **-**

- La columna Time es generada automáticamente , y es el tiempo que tarda en generarse una fila, es decir obtener datos, concatenar el lenguaje y ser encriptado.

- Con uso de la librería PANDAS  se calculo el tiempo total, el tiempo promedio, el tiempo mínimo y el máximo que tardo en procesar todas las filas de la tabla.

- Los datos de resultado del tiempo total, promedio, etc, se almacenaron en **sqlite**; En una base de datos llamada data.db y una tabla time, con campos **id** tipo **Integer y llave peimaria autoincrementable**, **total** tipo **TEXT**, **promedio** tipo **TEXT**,  **min** tipo **TEXT**, **max** tipo **TEXT**

> Para hacer un correcto uso de **sqlite**, se crearon funciones para :
>
> - Crear la base de datos.
> - Guardar los datos.
> - Obtener los datos para ser mostrados.

- Se genero un archivo JSON llamado **data.json**, el cual contiene los datos presentados en el DataFrame.

- Se incluyó un archivo **requirements.txt**, donde se evidencian las librerías utilizadas para el desarrollo.
