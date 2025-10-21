import requests, time

API_URL = "http://library.demo.local/api/v1/books"
HEADERS = {"accept": "application/json"}

MAX_PAGES = 100
MAX_RETRIES = 5
BASE_SLEEP = 0.5

total = 0
page = 0

print("=== LISTA COMPLETA DE LIBROS ===\n")

while page < MAX_PAGES:
    url = f"{API_URL}?includeISBN=true&sortBy=author&page={page}"

    for attempt in range(MAX_RETRIES):
        resp = requests.get(url, headers=HEADERS)

        if resp.status_code == 200:
            libros = resp.json()
            if not libros:
                print(f"\n📚 Total de libros encontrados: {total}")
                exit(0)

            for b in libros:
                total += 1
                print(f"{total:03d}. ID: {b['id']:<6} | Título: {b['title']:<38} | Autor: {b['author']:<22} | ISBN: {b.get('isbn','-')}")
            time.sleep(BASE_SLEEP)  
            break  

        elif resp.status_code == 429:
    
            retry_after = resp.headers.get("Retry-After")
            wait = float(retry_after) if retry_after else BASE_SLEEP * (2 ** attempt)
            print(f"⏳ 429 en página {page}, esperando {wait:.1f}s y reintentando…")
            time.sleep(wait)
            continue

        else:
            print(f"⚠️ Error en página {page}: {resp.status_code}")
            exit(1)

    else:
        # si agotamos reintentos
        print(f"❌ No se pudo obtener la página {page} tras {MAX_RETRIES} reintentos.")
        exit(1)

    page += 1
