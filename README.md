# Apache Kafka on Raspberry Pi 4/5 (8GB RAM)

## 📌 Problem Statement
Deploy an Apache Kafka broker on Raspberry Pi 4/5 (8GB RAM, 4 cores) and validate
producer–consumer message flow.

---

## 🧠 Conceptual Overview
- Kafka broker runs on Raspberry Pi in **KRaft (ZooKeeper-less) mode**
- Raspberry Pi acts as an **edge Kafka node**
- Producers publish events to Kafka topics
- Consumers read events independently

---

## 🏗 Architecture
Producer → Kafka Broker (Raspberry Pi) → Consumer

---

## ⚙️ Technical Setup
- Device: Raspberry Pi 4/5 (8GB RAM, Quad Core)
- OS: Ubuntu Server 22.04
- Java: OpenJDK 17
- Kafka Version: 4.1.1 (KRaft Mode)

---

## 🚀 Steps Performed

1. Installed Java 17
2. Downloaded Apache Kafka
3. Generated KRaft UUID
4. Formatted storage
5. Started Kafka broker
6. Created topic
7. Ran producer
8. Consumed messages

---

## ✅ Verification
- Messages produced successfully
- Messages consumed using `--from-beginning`
- Logs stored on disk

---

## 📌 Conclusion
Kafka can be deployed on Raspberry Pi 4/5 (8GB RAM) for:
- Edge analytics
- IoT gateways
- Learning & prototyping

---

## 🔮 Future Work
- ESP32 → MQTT → Kafka integration
- Multi-node Raspberry Pi Kafka cluster

## Concurrency Test Results

To evaluate the scalability of the pipeline, concurrent Raspberry Pi producers were simulated using a multiprocessing-based load generator. Each simulated device published telemetry data (temperature, CPU load, timestamp) at a rate of approximately 1 message per second via MQTT.

| Concurrent Producers | Observed Behavior |
|----------------------|-------------------|
| 5                    | Stable ingestion, minimal latency |
| 50                   | Smooth message flow, no message loss |
| 100                  | Kafka absorbed load without backpressure |
| 200                  | Consumers continued processing independently |
| 350                  | System remained stable with sustained throughput |

Kafka successfully buffered incoming events using its append-only log, allowing producers and consumers to remain decoupled even under increased load.


## Observed Behavior at 350 Producers

At 350 concurrent Raspberry Pi producers, the system demonstrated the following characteristics:

- No producer-side failures or disconnects were observed
- MQTT broker continued to accept connections without instability
- Kafka broker sustained continuous ingestion of events
- Consumers processed messages in real time without blocking
- Alerting logic remained functional under sustained load

This confirms that Kafka effectively decouples high-volume event ingestion from downstream processing, making the architecture suitable for real-world IoT and edge analytics use cases where burst traffic and high concurrency are expected.
