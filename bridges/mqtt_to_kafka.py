import json
import paho.mqtt.client as mqtt
from kafka import KafkaProducer

MQTT_TOPIC = "rpi/telemetry"
KAFKA_TOPIC = "rpi-events"

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    producer.send(KAFKA_TOPIC, data)
    print("Forwarded to Kafka:", data)

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe(MQTT_TOPIC)
client.on_message = on_message

print("MQTT → Kafka bridge running...")
client.loop_forever()
