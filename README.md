# DB_Scan_
# DBSCAN-Based Anomaly Detection in Sensor Data (Flask App)
```
This project demonstrates how to use the DBSCAN clustering algorithm to detect anomalies in sensor data. The web app is built using Flask and visualizes the clusters using Plotly.
```
# Project Structure
```
dbscan_sensor_anomaly/
├── app.py
├── sensor_data.csv
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```
# Features
```
Unsupervised anomaly detection using DBSCAN

Visualization of clustered and anomalous points

Interactive Plotly plot embedded in the web UI

Highlights anomalies in red

Lightweight Flask backend
```
# Dataset
```
sensor_data.csv contains 30 rows of synthetic sensor readings:

Mean	StdDev	MaxValue	MinValue	SpikeCount
49.5	5.2	60.1	40.2	3
...	...	...	...	...
```
```
Normal readings form dense clusters.

Anomalous readings appear sparse and isolated.
```
# How to Run the App
```
1. Clone the repository or download the files.
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the Flask app:
```
python app.py
```
# Requirements
```
See requirements.txt:
flask
pandas
scikit-learn
plotly
```
# Algorithms Used
```
DBSCAN (Density-Based Spatial Clustering of Applications with Noise):

Detects clusters of varying shapes.

Marks points in low-density areas as anomalies (label = -1).

Does not require specifying number of clusters.
```
# Customization Ideas
```
Change the clustering features (e.g., add MaxValue, SpikeCount)

Enable user to upload their own sensor dataset

Tune eps and min_samples dynamically via UI sliders

Add a time-series anomaly visualization for real-time data
```
# ScreenShots
![alt text](<Screenshot 2025-08-03 164339.png>)
![alt text](<Screenshot 2025-08-03 164358.png>)
