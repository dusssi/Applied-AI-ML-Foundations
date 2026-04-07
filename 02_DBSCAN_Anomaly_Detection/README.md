# 🕵️ Assignment 2 — DBSCAN for Anomaly Detection

---

## 🎯 Objective

Detect anomalous patterns in network traffic data using DBSCAN and compare its performance with KMeans clustering.

---

## 🛠️ Techniques Used

* DBSCAN Clustering
* KMeans (for Comparison)
* Feature Scaling

---

## 📊 Output

### 🔹 Anomaly Detection (DBSCAN)

<img width="335" height="64" alt="Anomaly Count" src="https://github.com/user-attachments/assets/10918681-64c0-41f2-b389-8b5aa10fecfc" />

### 🔹 DBSCAN Clustering Visualization

<img width="1233" height="524" alt="DBSCAN Visualization" src="https://github.com/user-attachments/assets/0afccf2d-666c-4689-8a5d-8c5a81bba04c" />

### 🔹 KMeans Comparison

<img width="629" height="200" alt="KMeans Comparison" src="https://github.com/user-attachments/assets/31447f59-f595-48a8-a94c-b4647a5f4623" />

---

## 📌 Results

* Identified noise points (labeled as `-1`) as anomalies
* Compared clustering behavior of DBSCAN and KMeans
* Observed that DBSCAN isolates outliers instead of forcing them into clusters

---

## ⚡ Key Insight

> DBSCAN is more effective for anomaly detection because it identifies noise explicitly,
> while KMeans assigns every data point to a cluster.

---
