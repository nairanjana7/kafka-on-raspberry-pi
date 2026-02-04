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
