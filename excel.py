import pandas as pd
import os


dir_file = os.path.join('report.xlsx')

excel_file = pd.read_excel(dir_file)



excel_file["filename"] = excel_file["username"].astype(str) + ".jpg"
excel_file["codigo_img"] = excel_file["codigo_empleado"].astype(str) + ".jpg"

excel_file.to_excel("Carga_imagenes.xlsx", index=False)