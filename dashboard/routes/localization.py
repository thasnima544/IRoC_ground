from pathlib import Path

from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    current_app
)

from dashboard.services.localization_service import (
    LocalizationService
)

localization_bp = Blueprint(
    "localization",
    __name__
)

service = LocalizationService()


@localization_bp.route(
    "/localization"
)
def localization_page():

    return render_template(
        "localization.html"
    )


@localization_bp.route(
    "/localize",
    methods=["POST"]
)
def localize():

    if "image" not in request.files:

        return jsonify({

            "success": False,

            "message":
                "No image uploaded"

        })

    image = request.files["image"]

    upload_dir = Path(
        current_app.config[
            "UPLOAD_FOLDER"
        ]
    )

    upload_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    image_path = (
        upload_dir /
        image.filename
    )

    image.save(
        image_path
    )

    result = (

        service.localize(
            str(image_path)
        )

    )

    return jsonify(result)