
import pandas as pd

def transformar_datos(df):
    df = df.copy()

    # Normalizar nombres de columnas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )

    # Eliminar registros duplicados
    duplicados = df.duplicated().sum()
    df = df.drop_duplicates()

    print("Duplicados eliminados:", duplicados)

    # Revisar valores nulos
    print("Valores nulos:")
    print(df.isnull().sum())

    # Eliminar filas sin variable objetivo
    df = df.dropna(subset=["quality"])

    # Imputar valores faltantes de variables predictoras
    columnas_numericas = df.select_dtypes(
        include="number"
    ).columns.drop("quality")

    for columna in columnas_numericas:
        mediana = df[columna].median()
        df[columna] = df[columna].fillna(mediana)

    print("Datos transformados:", df.shape)

    return df
