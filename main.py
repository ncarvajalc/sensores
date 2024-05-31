from fastapi import FastAPI

# Example metrics data with three dictionaries
metrics = [
    {"title": "Humedad de Suelo", "value": "10%"},
    {"title": "Temperatura ambiente", "value": "20°C"},
    {"title": "Humedad Ambiente", "value": "50%"},
]

# Adding two more sets of metrics for diversity
metrics2 = [
    {"title": "Humedad de Suelo", "value": "15%"},
    {"title": "Temperatura ambiente", "value": "19°C"},
    {"title": "Humedad Ambiente", "value": "55%"},
]

metrics3 = [
    {"title": "Humedad de Suelo", "value": "20%"},
    {"title": "Temperatura ambiente", "value": "19°C"},
    {"title": "Humedad Ambiente", "value": "60%"},
]

# Store all metrics in an array
all_metrics = [metrics, metrics2, metrics3]

# Initialize the FastAPI application
app = FastAPI()

# CORS enable all domains
@app.middleware("http")
async def add_cors_header(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.get("/mediciones")
async def get_metrics():
    """Return the array of metrics data."""
    return {"metrics": all_metrics}

@app.get("/")
async def read_root():
    return {"Hello": "World"}
