import json
import requests
import time

# Esperamos que ngrok ya esté corriendo
time.sleep(3)

# Obtenemos el túnel actual
r = requests.get("http://localhost:4040/api/tunnels")
data = r.json()
url = data['tunnels'][0]['public_url']

# Actualizamos el JSON
with open("current_url.json", "w") as f:
    json.dump({"url": url}, f, indent=2)

print(f"✅ URL actualizada: {url}")
