# Mi proyecto de Streamlit

#### El objetivo de este proyecto  es la creación y gestión de entornos virtuales en Python

# Instrucciones para completar el proyecto

#### Crea una cuenta en github.com.
#### Crea un nuevo repositorio git con un archivo README.md y un archivo .gitignore
#### Crea una cuenta en render.com.
#### Realizar un análisis exploratorio de datos. Para lograrlo, necesitarás tener instalados los paquetes pandas y plotly-express. 
#### Además, necesitarás el paquete streamlit para desarrollar una aplicación web.

# Entorno virtual

#### Crea un nuevo entorno virtual y asígnarle un nombre significativo que esté relacionado con el conjunto de datos con el que se trabajar.

# Descargar archivo de datos

#### Descarga el conjunto de datos de anuncios de coches (vehicles_us.csv) o encuentra tu propio dataset en formato CSV.
#### Coloca el conjunto de datos en el directorio del proyecto.

# Análisis exploratorio de datos

#### Crea un directorio llamado notebooks en el directorio de tu proyecto.
#### Crea un Jupyter notebook llamado EDA.ipynb en VS Code y guárdalo en el directorio notebooks de tu proyecto. Recuerda que .ipynb es una extensión de archivo para Jupyter Notebooks.
#### Abre el Jupyter notebook EDA.ipynb y experimenta con plotly-express para crear visualizaciones para el análisis exploratorio básico del conjunto de datos dentro del notebook. 

# Desarrollo del cuadro de mandos de la aplicación web

#### Crea un archivo app.py en la raíz del directorio de tu proyecto. Para crear un archivo .py, haz clic en "New File" (Nuevo archivo) en VS Code y guárdalo en el directorio del proyecto con el nombre deseado y la extensión .py.
#### Importa streamlit como st, pandas y plotly_express al principio del archivo.
#### Lee el archivo CSV del conjunto de datos en un DataFrame. El código será el mismo que tenías en el Jupyter Notebook al explorar el conjunto de datos.
#### Ahora, vamos a crear el contenido de nuestra aplicación basada en Streamlit.

#### Al menos un encabezado (puedes utilizar st.header() para hacerlo. En la lección de aplicaciones web te mostramos cómo crear un encabezado).
#### Crea un botón que, al hacer clic en él, construya un histograma plotly-express. Para hacerlo, considera utilizar las funciones st.write() y st.plotly_chart()
#### Recuerda confirmar y empujar todos los cambios a tu repositorio cuando hayas terminado tu trabajo. 

# Visualizacion de datos

#### Mientras desarrollas tu aplicación añadiendo un nuevo componente de Streamlit, puedes ejecutar el comando streamlit run app.py desde la terminal para ver el resultado.
#### Es una buena práctica confirmar y enviar tu trabajo a un repositorio remoto en GitHub a medida que vas alcanzando ciertos objetivos en el desarrollo de la aplicación (por ejemplo, añades un componente que funciona y la aplicación se ejecuta sin errores). ¡Así que no te olvides de escribir un mensaje de confirmación significativo!