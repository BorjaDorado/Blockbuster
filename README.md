# Blockbuster

[![180713133656-bend-oregon-blockbuster-inside.jpg](https://i.postimg.cc/hG0m1qf2/180713133656-bend-oregon-blockbuster-inside.jpg)](https://postimg.cc/KKR4mw7T)

Este proyecto tiene como ***objetivo*** principal ***crear una base de datos relacional en MySQL*** a través de una serie de CSV que contienen datos de un videoclub.

## Proceso

### Limpieza de datos

En esta fase del proyecto, se realizó la limpieza de los archivos CSV. Se identificaron dataframes relacionados entre sí por una o más columnas y se eliminaron las columnas irrelevantes, manteniendo solo las conexiones necesarias. Además, se reorganizaron algunas columnas para mejorar la consistencia de los datos.

Se crearon nuevas entidades como Customers y Staff que son fundamentales en cualquier negocio. También se agregó la columna 'stock' en la entidad Inventory para llevar un registro del inventario disponible.

Se realizaron cambios en los tipos de datos, especialmente en las fechas, y se eliminaron columnas innecesarias que contenían valores nulos.

### Importación d los datos

Posteriormente, se cargaron los datos en la base de datos de MySQL y se creó el Diagrama de Entidad-Relación (ERD) correspondiente.

#### Aclaración/Nota

Dentro de la carpeta de data, encontrarás varios archivos CSV que tienen el mismo nombre pero diferente codificación. Esto se debe a problemas al importar los archivos en MySQL Workbench, donde algunas tablas no fueron leídas correctamente.

