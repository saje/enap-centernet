import json
import requests
import time
import urllib.request
import os.path


'''
print(len([
        "Animal", 
        "Basural", 
        "Bus", 
        "Camión", 
        "Chasis", 
        "Cilindro", 
        "Entrada", 
        "Escombro", 
        "Estructura",
        "GHorquilla",
        "Juegos",
        "Maquinaria", 
        "MConstrucción", 
        "PalletCaja", 
        "Persona", 
        "Pickup", 
        "Piscina", 
        "Poste", 
        "SAdvertencia", 
        "Tractor", 
        "Troncos", 
        "Tuberia", 
        "Vehículo", 
        "Zanja", 
          ]))


   
with open("VIA-KAUEL-J_coco.json") as json_file:
    data=json.load(json_file)
    for i in data["images"]:
      nombre="enap_images/{}".format(i["coco_url"].split("/")[8])
      if not os.path.isfile(nombre):
        myurl=i["coco_url"]
        myreq=urllib.request.urlopen(i["coco_url"])
        print(i["coco_url"].split("/")[8])
        mydata = myreq.read()
        with open(nombre, 'wb') as ofile:
          ofile.write(mydata)
largo=len(data["images"])
print(f"Descargue {largo}")      
'''

valid_ids = [
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 
      14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 
      24, 25, 27, 28, 31, 32, 33, 34, 35, 36, 
      37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 
      48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 
      58, 59, 60, 61, 62, 63, 64, 65, 67, 70, 
      72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 
      82, 84, 85, 86, 87, 88, 89, 90]
num_classes=24
print({v:i for i,v in enumerate(valid_ids)})
print([(v // 32 * 64 + 64, (v // 8) % 4 * 64, v % 8 * 32) \
                      for v in range(1, num_classes + 1)])