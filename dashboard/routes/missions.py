from flask import Blueprint, render_template, jsonify

from dashboard.services.dataset_service import (
    DatasetService
)

missions_bp = Blueprint(
    "missions",
    __name__
)

dataset_service = DatasetService()


@missions_bp.route("/")
def home():

    missions = (
        dataset_service.get_all_missions()
    )

    latest = (
        dataset_service.get_latest_mission()
    )

    stats = (
        dataset_service.get_dashboard_stats()
    )

    return render_template(
        "index.html",
        missions=missions,
        latest=latest,
        stats=stats
    )


@missions_bp.route(
    "/missions"
)
def missions():

    return jsonify(

        dataset_service
        .get_all_missions()

    )


@missions_bp.route(
    "/mission/<mission_id>"
)
def mission_details(
        mission_id):

    data = (

        dataset_service
        .get_mission_details(
            mission_id
        )

    )

    return jsonify(data)