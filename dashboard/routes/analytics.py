from flask import (
    Blueprint,
    render_template,
    jsonify
)

from dashboard.services.dataset_service import (
    DatasetService
)

analytics_bp = Blueprint(
    "analytics",
    __name__
)

service = DatasetService()


@analytics_bp.route(
    "/analytics"
)
def analytics_page():

    return render_template(
        "analytics.html"
    )


@analytics_bp.route(
    "/analytics/sensors"
)
def sensor_data():

    return jsonify(

        service
        .get_sensor_data()

    )


@analytics_bp.route(
    "/analytics/battery"
)
def battery_data():

    return jsonify(

        service
        .get_battery_data()

    )