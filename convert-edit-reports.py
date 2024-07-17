import pandas as pd

def eliminar_columna_convertir_guardar(input_csv, output_xlsx, columna_eliminar):
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(input_csv)
    
    # Eliminar la columna especificada
    if columna_eliminar in df.columns:
        df.drop(columns=[columna_eliminar], inplace=True)
    else:
        print(f"La columna '{columna_eliminar}' no existe en el archivo CSV.")
        return
    
    # Guardar el DataFrame en un archivo Excel (.xlsx)
    df.to_excel(output_xlsx, index=False, engine='openpyxl')
    print(f"Archivo guardado como {output_xlsx}")

# Ejemplo de uso
input_csv = 'datos.csv'
output_xlsx = 'datos_sin_columna.xlsx'
columna_eliminar = 'ColumnaAEliminar'

eliminar_columna_convertir_guardar(input_csv, output_xlsx, columna_eliminar)
