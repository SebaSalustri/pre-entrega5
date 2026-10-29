
from src.extract import extraer_datos
from src.transform import transformar_datos
from src.load import cargar_datos


def main():

    # EXTRACT
    print("Iniciando extracción...")
    df = extraer_datos(
        r"C:\Users\sebas\Desktop\pipeline-etl-vinos\data\winequality-red.csv"
    )

    # TRANSFORM
    print("\nIniciando transformación...")
    df_limpio = transformar_datos(df)

    # LOAD
    print("\nIniciando carga...")
    cargar_datos(
        df_limpio,
        "output/vinos_procesados.parquet"
    )

    print("\nPipeline ETL finalizado correctamente.")


if __name__ == "__main__":
    main()
