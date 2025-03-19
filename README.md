# API de Predicción de Fraude

Esta API permite predecir si una transacción es fraudulenta utilizando un modelo de Regresión Logística previamente entrenado y guardado en `mejor_modelo_logistic_regression.pkl`.

## Requisitos

Antes de ejecutar la API, asegúrate de tener instaladas las siguientes dependencias:

```bash
pip install fastapi uvicorn joblib pandas numpy requests
```

## Iniciar la API

Ejecuta el siguiente comando para iniciar la API con FastAPI:

```bash
uvicorn api:app --reload
```

La API estará disponible en `http://127.0.0.1:8000/`.

## Endpoints Disponibles

### `GET /`

**Descripción:** Endpoint de prueba para verificar que la API está activa.

**Ejemplo de uso:**

```bash
curl -X 'GET' 'http://127.0.0.1:8000/'
```

**Respuesta esperada:**

```json
{"message": "API de Predicción de Fraude Activa"}
```

### `POST /predict`

**Descripción:** Recibe una transacción en formato JSON y devuelve si es fraudulenta junto con la probabilidad.

**Ejemplo de entrada:**

```json
{
    "Monto": 250.50,
    "HistorialFraudes": 2,
    "MomentoDia": "Tarde",
    "TipoTransaccion": "Compra",
    "Ubicación": "Ciudad A"
}
```

**Ejemplo de solicitud con `curl`:**

```bash
curl -X 'POST' 'http://127.0.0.1:8000/predict' \
-H 'Content-Type: application/json' \
-d '{"Monto": 250.50, "HistorialFraudes": 2, "MomentoDia": "Tarde", "TipoTransaccion": "Compra", "Ubicación": "Ciudad A"}'
```

**Ejemplo de respuesta esperada:**

```json
{
    "fraud_prediction": 0,
    "fraud_probability": 0.25
}
```

## Notas

- Puedes probar la API visualmente en `http://127.0.0.1:8000/docs`, donde FastAPI genera documentación interactiva.
- El modelo utilizado en esta API fue entrenado previamente y guardado como `mejor_modelo_logistic_regression.pkl`.
