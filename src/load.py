
from pathlib import Path

def cargar_datos(df, ruta):
    archivo = Path(ruta)

    # Crear carpeta de salida
    archivo.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Exportar a Parquet
    df.to_parquet(
        archivo,
        engine="pyarrow",
        index=False
    )

    print("Archivo Parquet generado:", archivo)
