from prometheus_client import start_http_server, Summary, Counter, Gauge
import time
import random

# Define custom metrics
REQUEST_TIME = Summary('app_request_processing_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('app_request_count', 'Total number of requests processed')
TEMPERATURE = Gauge('app_temperature_celsius', 'Current simulated temperature in Celsius')

@REQUEST_TIME.time()
def process_request():
    """Simulate request processing."""
    time.sleep(random.uniform(0.1, 1.0))  # Simulate processing time
    TEMPERATURE.set(random.uniform(20, 35))  # Simulate temperature
    REQUEST_COUNT.inc()

if __name__ == '__main__':
    # Start Prometheus metrics HTTP server on port 8000
    start_http_server(8000)
    print("✅ Metrics available at http://<EC2-IP>:8000/metrics")

    # Infinite loop to generate metrics
    while True:
        process_request()

