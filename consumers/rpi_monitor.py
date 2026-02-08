import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "rpi-events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    group_id="rpi-monitor-group",
    auto_offset_reset="latest"
)

print("Kafka consumer started...")

for msg in consumer:
    data = msg.value
    if data["temperature"] > 40:
        print("[ALERT]", data)
