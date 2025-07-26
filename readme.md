# 📊 ML Model Monitoring with Prometheus & Grafana

This is a sample project to demonstrate how to monitor a Machine Learning model using **Prometheus** and **Grafana**.

The goal is to show how model metrics such as latency, throughput, and accuracy can be exposed, scraped, and visualized using industry-standard observability tools.

> ⚠️ This project is for learning and demonstration purposes only.

---

## 🧠 What This Project Includes

- A basic Python app that simulates predictions from a ML model.
- Exposed metrics using `prometheus_client`.
- A Prometheus configuration to scrape metrics from the model.
- A Grafana dashboard to visualize model performance in real time.

---

## ⚙️ Requirements

Make sure you have the following installed:

- [Docker](https://www.docker.com/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)


---

## 🛠️ Installation & Setup

### 1. Clone this repository

```bash
git clone https://github.com/franruedaesq/ml-monitoring-demo.git
cd ml-monitoring-demo

