import requests
from datetime import datetime

def obtener_dolar():
    try:
        response = requests.get("https://api.bluelytics.com.ar/v2/latest")
        data = response.json()
        return data["blue"]["value_sell"] # Precio de venta del dólar blue
    except:
        # Si falla la conexión, usa un valor por defecto
        return 1000

def conversor():
    print("\n--- CONVERSOR PRO (Datos en tiempo real) ---")
    
    precio_dolar = obtener_dolar()
    
    ahora = datetime.now()
    fecha_formateada = ahora.strftime("%d/%m/%Y")
    hora_formateada = ahora.strftime("%H:%M:%S")
    
    print(f"Cotización actual del Dólar Blue: ${precio_dolar}")
    print(f"Fecha: {fecha_formateada} | Hora: {hora_formateada}")
    
    try:
        pesos = float(input("Pesos a convertir: "))
        dolares = pesos / precio_dolar
        print(f">>> Tienes: ${dolares:.2f} USD")
        
    except ValueError:
        print("❌ Error: Por favor, ingresa solo números.")
    except ZeroDivisionError:
        print("❌ Error: La cotización no puede ser cero.")
       
conversor()