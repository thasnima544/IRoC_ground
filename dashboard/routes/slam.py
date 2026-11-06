from flask import (
    Blueprint,
    render_template,
    jsonify
)

from dashboard.services.slam_service import (
    SlamService
)

slam_bp = Blueprint(
    "slam",
    __name__
)

service = SlamService()


@slam_bp.route(
    "/slam"
)
def slam_page():

    return render_template(
        "slam.html"
    )


@slam_bp.route(
    "/slam/keyframes"
)
def keyframes():

    return jsonify(

        service
        .get_keyframes()

    )


@slam_bp.route(
    "/slam/map"
)
def slam_map():

    return jsonify(

        service
        .get_map_data()

    )


@slam_bp.route(
    "/slam/history"
)
def localization_history():

    return jsonify(

        service
        .get_localization_history()

    )