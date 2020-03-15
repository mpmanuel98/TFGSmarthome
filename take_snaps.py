import modules.azure_faceapi as AFA
import modules.foscam_webcams as FWC
import modules.spacelynk_server as SS
import modules.sony_tv as ST
import face_recognition as FR
import requests
import xml.etree.ElementTree as ET
import io
import time
from PIL import Image
import cv2
import numpy as np


##########################################
################## URLs ##################
##########################################

# URL de acceso a la camara del salon
url_salon = "http://192.168.7.225:8894/cgi-bin/CGIProxy.fcgi?"

# URL de acceso a la camara del distribuidor
url_distribuidor = "http://192.168.7.224:8893/cgi-bin/CGIProxy.fcgi?"

# URL de acceso a la camara de la cocina
url_cocina = "http://192.168.7.223:8892/cgi-bin/CGIProxy.fcgi?"

# URL de acceso a la camara del dormitorio
url_dormitorio = "http://192.168.7.222:8891/cgi-bin/CGIProxy.fcgi?"

# URL de acceso a la camara en mi casa
url_pruebas_casa = "http://192.168.1.50:88/cgi-bin/CGIProxy.fcgi?"

"""
for i in range(1, 1000):
    name = "test" + str(i)
    name = name + ".jpeg"
    FWC.take_and_save_snap(url_pruebas_casa, name)
    time.sleep(1)
"""

for i in range(1, 1000):
    #Obtenemos un frame de la camara IP
    frame = FWC.take_snap(url_pruebas_casa)

    #Abrimos la imagen
    pil_image = Image.open(io.BytesIO(frame))
    image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    face_list = FR.detect_face(image)

    if face_list is not None:
        for face in face_list:
            im = Image.fromarray(face)
            im.save("images_taken/image" + str(i) + ".png")