from flask import Flask, render_template
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('sensor_data.csv')

    features = ['MeanTemp', 'Variance', 'SpikeCount']
    X = df[features]
    X_scaled = StandardScaler().fit_transform(X)

    db = DBSCAN(eps=1.2, min_samples=3).fit(X_scaled)
    df['Cluster'] = db.labels_

    df['Anomaly'] = df['Cluster'].apply(lambda x: 'Yes' if x == -1 else 'No')


    fig = px.scatter_3d(
        df, x='MeanTemp', y='Variance', z='SpikeCount',
        color=df['Cluster'].astype(str),
        symbol='Anomaly',
        hover_data=['SensorID'],
        title='Sensor Anomaly Clustering with DBSCAN'
    )
    plot_html = fig.to_html(full_html=False)

    return render_template('index.html', plot=plot_html, data=df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
