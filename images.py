from PIL import Image
import os

BASE_DIR = "img/"

def image_converter(base_image, image):
   try:
       
       image_fondo = Image.open(base_image)
       image_empleado = Image.open(image)
       rescala = image_empleado.resize((280, 350), Image.LANCZOS) 
       image_fondo.paste(rescala, (180,150))
    #    image_fondo.paste(image_empleado, (230,150))
       image_fondo.save('resultados\\'+ image)
       print("Done")
   except Exception as e:
       print(e)
   
   
   
   
   
   
if __name__ == "__main__":
    
    base_image = BASE_DIR + "fondo.jpg"
    image = 'Fotos'
    
    for img in os.listdir(image):
        image_path = os.path.join(image, img)
        print(image_path)
        image_converter(base_image, image_path)
    
    
    # image_converter(base_image, "img/ARLUCIANO.jpg")