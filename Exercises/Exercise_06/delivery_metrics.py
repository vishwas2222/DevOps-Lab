
from http.server import BaseHTTPRequestHandler, HTTPServer
from prometheus_client import Counter, Gauge, Histogram, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST
import random
import threading
import time

total_deliveries = Counter(
    "total_deliveries",
    "Total number of deliveries processed"
)

pending_deliveries = Gauge(
    "pending_deliveries",
    "Number of deliveries pending"
)

on_the_way_deliveries = Gauge(
    "on_the_way_deliveries",
    "Number of deliveries on the way"
)

average_delivery_time = Histogram(
    "average_delivery_time",
    "Delivery processing time in seconds"
)

pending_deliveries.set(5)
on_the_way_deliveries.set(3)


def simulate_deliveries():
    while True:
        delivery_time = random.uniform(10, 60)

        with average_delivery_time.time():
            time.sleep(delivery_time / 100)

        total_deliveries.inc()

        pending = max(0, int(pending_deliveries._value.get()) - 1)
        pending_deliveries.set(pending)

        on_the_way_deliveries.inc()

        time.sleep(5)

        on_the_way_deliveries.dec()
        pending_deliveries.inc()


class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/metrics":
            output = generate_latest()
            self.send_response(200)
            self.send_header("Content-Type", CONTENT_TYPE_LATEST)
            self.end_headers()
            self.wfile.write(output)

        elif self.path == "/":
            message = b"Delivery metrics application is running."
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(message)

        else:
            self.send_error(404, "Not Found")

    def log_message(self, format_string, *args):
        print(format_string % args)


if __name__ == "__main__":
    threading.Thread(
        target=simulate_deliveries,
        daemon=True
    ).start()

    server = HTTPServer(("0.0.0.0", 8000), MetricsHandler)
    print("Delivery metrics available on port 8000")
    server.serve_forever()
