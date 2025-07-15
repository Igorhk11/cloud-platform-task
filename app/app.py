from prometheus_client import start_http_server, Gauge
import requests
import time

# Prometheus metrics
url_up = Gauge('sample_external_url_up', 'URL availability', ['url'])
url_response_ms = Gauge('sample_external_url_response_ms', 'Response time in ms', ['url'])

# URLs to check
urls = [
    "https://httpstat.us/503",
    "https://httpstat.us/200"
]

def check_urls():
    for url in urls:
        try:
            start = time.time()
            response = requests.get(url, timeout=5)
            latency = (time.time() - start) * 1000  # ms
            url_response_ms.labels(url=url).set(latency)
            url_up.labels(url=url).set(1 if response.status_code == 200 else 0)
        except requests.RequestException:
            url_up.labels(url=url).set(0)
            url_response_ms.labels(url=url).set(-1)

if __name__ == "__main__":
    start_http_server(8000)
    print("Metrics available at http://0.0.0.0:8000/metrics")
    while True:
        check_urls()
        time.sleep(10)
