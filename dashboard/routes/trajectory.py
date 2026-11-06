from flask import (
    Blueprint,
    render_template,
    jsonify
)

from dashboard.services.trajectory_service import (
    TrajectoryService
)

trajectory_bp = Blueprint(
    "trajectory",
    __name__
)

service = (
    TrajectoryService()
)


@trajectory_bp.route(
    "/trajectory"
)
def trajectory_page():

    return render_template(
        "trajectory.html"
    )


@trajectory_bp.route(
    "/trajectory/data"
)
def trajectory_data():

    return jsonify(

        service
        .get_trajectory()

    )


@trajectory_bp.route(
    "/trajectory/stats"
)
def trajectory_stats():

    return jsonify(

        service
        .get_statistics()

    )