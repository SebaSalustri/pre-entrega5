
import pandas as pd

def extraer_datos(ruta):
    tipos = {
        "fixed acidity": "float32",
        "volatile acidity": "float32",
        "citric acid": "float32",
        "residual sugar": "float32",
        "chlorides": "float32",
        "free sulfur dioxide": "float32",
        "total sulfur dioxide": "float32",
        "density": "float32",
        "pH": "float32",
        "sulphates": "float32",
        "alcohol": "float32",
        "quality": "Int64"
    }

    df = pd.read_csv(
        ruta,
        sep=";",
        dtype=tipos
    )

    print("Datos extraídos:", df.shape)
    return df
