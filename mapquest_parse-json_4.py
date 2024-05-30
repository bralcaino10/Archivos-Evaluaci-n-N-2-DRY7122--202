import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "zXDtRa9fLYvxQQ2yshv1o4yC3HWDBjlt"


rendimiento_combustible = 14 

while True:
    orig = input("Ubicación de Inicio: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destino: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("Estado de la API: " + str(json_status) + " = Llamada de ruta exitosa.\n")
        print("=============================================")
        print("Direcciones desde " + orig + " hasta " + dest)
        print("Duración del Viaje:   " + json_data["route"]["formattedTime"])
        print("Kilómetros:      " + str("{:.2f}".format((json_data["route"]["distance"]) * 1.61)))

        if "fuelUsed" in json_data["route"]:
            fuel_used = json_data["route"]["fuelUsed"]
            print("Combustible Usado (Ltr): " + str("{:.2f}".format(fuel_used * 3.78)))
        else:
            
            distancia_km = json_data["route"]["distance"] * 1.61
            combustible_estimado = distancia_km / rendimiento_combustible
            print("Combustible Usado Estimado (Ltr): " + str("{:.2f}".format(combustible_estimado)))

        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"]) * 1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Código de Estado: " + str(json_status) + "; Entradas de usuario inválidas para una o ambas ubicaciones.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Código de Estado: " + str(json_status) + "; Falta una entrada para una o ambas ubicaciones.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("Para el Código de Estado: " + str(json_status) + "; Consulte:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")