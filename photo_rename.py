import os
import pandas as pd

path = 'Fotos copy'
excel_file = 'carga_imagenes.xlsx'
df_nuevos_nombres = pd.read_excel(excel_file)

for img in os.listdir(path):
    if str(img.lower()) in df_nuevos_nombres["codigo_img"].values:
        # Obtener el nuevo nombre de usuario
        new_username = df_nuevos_nombres.loc[df_nuevos_nombres["codigo_img"].str.lower() == img.lower(), "filename"].values[0]
        
        # Obtener la ruta completa del archivo actual y el nuevo nombre
        old_path = os.path.join(path, img)
        new_path = os.path.join(path, new_username)
        
        try:
            # Renombrar el archivo
            os.rename(old_path, new_path)
            print(f"Renombrado: {img} -> {new_username}")
        except OSError as e:
            print(f"Error al renombrar {img}: {e}")
    else:
        print(f"No coincide: {img}")


    