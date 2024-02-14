from datetime import datetime
import os
import cv2



try:
   
    # Set the directory where the images are located
    ejemplo_dir = os.path.join('Fotos copy')

    # Get the list of files in the directory
    contenido = os.listdir(ejemplo_dir)

    # List to hold image filenames
    imagenes = []

    # Loop over the files in the directory
    for fichero in contenido:
        # Check if it's a file and has a .jpg or .jpeg extension
        if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.lower().endswith(('.jpg', '.jpeg', 'JPG', 'JPEG')):
            imagenes.append(fichero)

    # Create the target directory if it doesn't exist
    target_dir = 'Fotos_180x240'
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Current date is fetched but not used in this snippet
    fecha = datetime.now()
    i=0
    # Loop over the image filenames
    for imagen in imagenes:
        # Construct the full file path
        ruta = os.path.join(ejemplo_dir, imagen)
       

        # Read the image from file
        img = cv2.imread(ruta)
        

        # If the image is not 300x400, resize and save
        if img is not None and img.shape != (300, 400, 3):
            # Clean up the filename, here is a simple example of removing spaces
            imagen = imagen.replace(" ", "").replace("copy", "").replace("-Copy", "").replace("copia", "").replace("Copy", "").replace(" copy", "")

            # Resize the image to 300x300
            img2 = cv2.resize(img, (180, 240))

            # Save the image to the new directory
            cv2.imwrite(os.path.join(target_dir, imagen), img2)

            print(i," " +imagen)
        else:
            print(i," " +imagen)
        
        i+=1
except Exception as e:
    print(e)
    with open("Error_de_Calidad_imagen.txt", 'a') as f:
        f.write("ERROR!: "+str(e)+"\n")
        









