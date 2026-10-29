# Pipeline ETL — Calidad del Vino

## Descripción

Este proyecto implementa un pipeline ETL utilizando Python y Pandas para procesar datos de calidad de vinos tintos.

El objetivo es extraer datos desde un archivo CSV, realizar operaciones de limpieza y transformación, y exportar los resultados a un archivo Parquet preparado para futuros análisis de Machine Learning.

## Fuente de datos

Se utiliza el dataset Wine Quality del repositorio UCI Machine Learning Repository.

https://archive.ics.uci.edu/dataset/186/wine+quality

Archivo utilizado: `winequality-red.csv`.

El dataset contiene 1.599 registros originales con características fisicoquímicas de vinos tintos y una variable de calidad.

## Etapas del pipeline

### 1. Extracción

El módulo `src/extract.py` lee el archivo CSV utilizando Pandas. Se definen tipos de datos adecuados para optimizar el consumo de memoria.

### 2. Transformación

El módulo `src/transform.py` realiza las siguientes operaciones:

- Normalización de nombres de columnas.
- Eliminación de registros duplicados.
- Identificación de valores nulos.
- Eliminación de registros sin la variable objetivo `quality`.
- Imputación de valores numéricos faltantes mediante la mediana.

### 3. Carga

El módulo `src/load.py` exporta los datos procesados a `output/vinos_procesados.parquet`.

Se utiliza Parquet por su almacenamiento columnar, compresión y eficiencia para el procesamiento de datos, especialmente en proyectos de Machine Learning.

## Instalación

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Descargar el archivo `winequality-red.csv` desde la fuente indicada y guardarlo dentro de la carpeta `data/`.

## Ejecución

Desde la carpeta principal del proyecto, ejecutar:

```bash
python main.py
```

El programa ejecutará automáticamente las etapas de extracción, transformación y carga.

## Resultado

El pipeline genera el archivo `output/vinos_procesados.parquet`, que contiene los datos limpios y estructurados para su posterior utilización en modelos de Machine Learning.

## Tecnologías utilizadas

- Python
- Pandas
- PyArrow
- GitHub
