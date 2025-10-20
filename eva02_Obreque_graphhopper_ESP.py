import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
key = "4ad8de29-9e1c-4d1c-a894-0cf0f23f6776"  # <-- tu API key de GraphHopper

# ---------------------------------------------------------
# Geocoding (misma función, solo mensajes en español)
# ---------------------------------------------------------
def geocoding(location, key):
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": location, "limit": "1", "key": key})

    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code

    if json_status == 200 and json_data.get("hits"):
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0].get("osm_value", "")

        country = json_data["hits"][0].get("country", "")
        state = json_data["hits"][0].get("state", "")

        if state and country:
            new_loc = f"{name}, {state}, {country}"
        elif country:
            new_loc = f"{name}, {country}"
        else:
            new_loc = name

        print(f"✔ Geocodificación de '{new_loc}' (tipo: {value})")
    else:
        lat = "null"
        lng = "null"
        new_loc = location
        if json_status != 200:
            print(f"✖ Geocoding status: {json_status}\nMensaje: {json_data.get('message','')}")
        else:
            print("✖ No se encontraron resultados para la ubicación.")
    return json_status, lat, lng, new_loc

# ---------------------------------------------------------
# Bucle principal (textos en español + salida con 2 decimales)
# ---------------------------------------------------------
while True:
    print("\n===============================================")
    print(" Perfiles de vehículo disponibles:")
    print(" - auto, bicicleta, caminando")
    print(" (escriba 's' o 'salir' para terminar)")
    print("===============================================")

    profile_map = {
        "auto": "car",
        "bicicleta": "bike",
        "caminando": "foot"
    }

    vehicle = input("Ingrese el perfil de vehículo que utilizará: ").strip().lower()
    if vehicle in ("s", "salir", "q", "quit"):
        print("Saliendo… ¡Hasta luego!")
        break

    if vehicle in profile_map:
        vehicle = profile_map[vehicle]
    else:
        print("Perfil no válido. Se usará 'auto'.")
        vehicle = "car"

    loc1 = input("Dirección de origen: ").strip()
    if loc1.lower() in ("s", "salir", "q", "quit"):
        print("Saliendo… ¡Hasta luego!")
        break

    orig = geocoding(loc1, key)

    loc2 = input("Dirección de destino: ").strip()
    if loc2.lower() in ("s", "salir", "q", "quit"):
        print("Saliendo… ¡Hasta luego!")
        break

    dest = geocoding(loc2, key)

    print("-------------------------------------------------")
    if orig[0] == 200 and dest[0] == 200:
        op = "&point=" + str(orig[1]) + "%2C" + str(orig[2])
        dp = "&point=" + str(dest[1]) + "%2C" + str(dest[2])

        # Agregamos locale=es para instrucciones en español
        params = {"key": key, "vehicle": vehicle, "locale": "es"}
        paths_url = route_url + urllib.parse.urlencode(params) + op + dp

        # Una sola llamada (se reutiliza respuesta y status)
        resp = requests.get(paths_url)
        paths_status = resp.status_code
        paths_data = resp.json()

        print(f"Estado de la API de rutas: {paths_status}")
        print("-------------------------------------------------")
        print(f"Direcciones desde '{orig[3]}' hasta '{dest[3]}'")
        print("-------------------------------------------------")

        if paths_status == 200:
            # Distancias y tiempos con máximo 2 decimales
            metros = paths_data["paths"][0]["distance"]
            seg_tot = paths_data["paths"][0]["time"] / 1000.0

            km = metros / 1000.0
            miles = km / 1.61
            horas_dec = seg_tot / 3600.0

            # Formato HH:MM:SS (además, mostramos horas decimales con 2 decimales)
            sec = int(seg_tot % 60)
            minu = int((seg_tot // 60) % 60)
            hora = int(seg_tot // 3600)

            print(f"Distancia total: {km:.2f} km / {miles:.2f} millas")
            print(f"Duración (hh:mm:ss): {hora:02d}:{minu:02d}:{sec:02d}")
            print(f"Duración (horas): {horas_dec:.2f} h")
            print("-------------------------------------------------")
            print("Narrativa del viaje (paso a paso):")
            for step in paths_data["paths"][0]["instructions"]:
                texto = step["text"]          # ya viene en español por locale=es
                dist_step_km = step["distance"] / 1000.0
                dist_step_mi = dist_step_km / 1.61
                print(f"- {texto}  ({dist_step_km:.2f} km / {dist_step_mi:.2f} mi)")
            print("=================================================")
        else:
            print("✖ Error en rutas:", paths_data.get("message", "Desconocido"))
            print("*************************************************")
    else:
        print("✖ No fue posible geocodificar origen/destino.")
