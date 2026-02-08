import time
import json
import random
import argparse
import multiprocessing
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "rpi/telemetry"

def rpi_client(cid):
    client = mqtt.Client(client_id=f"rpi_{cid}")
    client.connect(BROKER, PORT, 60)

    while True:
        payload = {
            "device_id": f"rpi_{cid}",
            "temperature": round(random.uniform(20, 45), 2),
            "cpu_load": round(random.uniform(10, 90), 2),
            "timestamp": int(time.time())
        }
        client.publish(TOPIC, json.dumps(payload))
        time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--clients", type=int, default=1)
    args = parser.parse_args()

    processes = []
    for i in range(args.clients):
        p = multiprocessing.Process(target=rpi_client, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

