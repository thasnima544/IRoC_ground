from flask import Flask, render_template
import pandas as pd
from pathlib import Path

app = Flask(__name__)

ROOT = Path(__file__).resolve().parent.parent

DATASET = ROOT / "datasets" / "mission_003"

IMAGE_LOG = DATASET / "metadata" / "image_log.csv"
SENSOR_LOG = DATASET / "logs" / "sensor.csv"
TRAJECTORY = ROOT / "trajectories" / "trajectory.csv"

MATCHED_IMAGE = "img_000081.png"
MATCH_SCORE = 125

@app.route("/")
def dashboard():

    image_count = 0
    sensor_count = 0

    roll = 0
    pitch = 0
    yaw = 0
    distance = 0

    x = 0
    y = 0
    z = 0

    if IMAGE_LOG.exists():
        images = pd.read_csv(IMAGE_LOG)
        image_count = len(images)

    if SENSOR_LOG.exists():

        sensor = pd.read_csv(SENSOR_LOG)

        sensor_count = len(sensor)

        if sensor_count > 0:

            latest = sensor.iloc[-1]

            roll = round(float(latest["roll"]), 3)
            pitch = round(float(latest["pitch"]), 3)
            yaw = round(float(latest["yaw"]), 3)

            if "distance" in sensor.columns:
                distance = round(float(latest["distance"]), 2)

    if TRAJECTORY.exists():

        traj = pd.read_csv(TRAJECTORY)

        if len(traj) > 80:

            pose = traj.iloc[80]

            x = round(float(pose["x"]), 2)
            y = round(float(pose["y"]), 2)

            if "z" in pose:
                z = round(float(pose["z"]), 2)

    confidence = min(
        95,
        int(MATCH_SCORE / 1.3)
    )

    return render_template(

        "index.html",

        image_count=image_count,
        sensor_count=sensor_count,

        roll=roll,
        pitch=pitch,
        yaw=yaw,
        distance=distance,

        matched_image=MATCHED_IMAGE,
        match_score=MATCH_SCORE,
        confidence=confidence,

        x=x,
        y=y,
        z=z

    )

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )