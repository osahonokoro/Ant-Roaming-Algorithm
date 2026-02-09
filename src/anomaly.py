from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    model = IsolationForest(contamination=0.1)
    model.fit(data)
    return model.predict(data)
