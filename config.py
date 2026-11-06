"""
=========================================================
COSMIC_GROUND Configuration
IRoC-U 2026
Team Bitstream

Central configuration file used throughout the project.
=========================================================
"""

from pathlib import Path

# =====================================================
# PROJECT PATHS
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parent

DATASETS_DIR = PROJECT_ROOT / "datasets"
DATABASE_DIR = PROJECT_ROOT / "database"
MAPS_DIR = PROJECT_ROOT / "maps"
TRAJECTORIES_DIR = PROJECT_ROOT / "trajectories"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
LOGS_DIR = PROJECT_ROOT / "logs"

FEATURE_DIR = DATABASE_DIR / "descriptors"

SLAM_RESULTS_DIR = PROJECT_ROOT / "slam_results"

# =====================================================
# CREATE DIRECTORIES
# =====================================================

for directory in [

    DATASETS_DIR,

    DATABASE_DIR,

    MAPS_DIR,

    TRAJECTORIES_DIR,

    OUTPUTS_DIR,

    LOGS_DIR,

    FEATURE_DIR,

    SLAM_RESULTS_DIR

]:
    directory.mkdir(
        parents=True,
        exist_ok=True
    )

# =====================================================
# DATABASE
# =====================================================

SQLITE_DB = DATABASE_DIR / "mission.db"

# =====================================================
# CAMERA SETTINGS
# =====================================================

CAMERA_INDEX = 0

CAMERA_DEVICE = "/dev/video0"

FRAME_WIDTH = 1280

FRAME_HEIGHT = 800

FPS = 60

IMAGE_FORMAT = "png"

IMAGE_PREFIX = "img"

AUTO_EXPOSURE = True

SAVE_IMAGES = True

SHOW_CAMERA = False

# =====================================================
# PIXHAWK / MAVLINK
# =====================================================

PIXHAWK_PORT = "/dev/ttyACM0"

PIXHAWK_BAUD = 115200

HEARTBEAT_TIMEOUT = 30

PRINT_MAVLINK = False

# =====================================================
# MISSION SETTINGS
# =====================================================

MISSION_PREFIX = "mission_"

CAPTURE_RATE = 10

CAPTURE_INTERVAL = 1 / CAPTURE_RATE

SAVE_DEBUG_IMAGES = False

# =====================================================
# IMAGE SETTINGS
# =====================================================

IMAGE_EXTENSIONS = [

    ".jpg",

    ".jpeg",

    ".png"

]

# =====================================================
# ORB FEATURE SETTINGS
# =====================================================

ORB_NFEATURES = 5000

ORB_SCALE_FACTOR = 1.2

ORB_LEVELS = 8

MATCH_RATIO = 0.75

MIN_MATCH_COUNT = 20

# =====================================================
# TRAJECTORY SETTINGS
# =====================================================

FLOW_SCALE_FACTOR = 0.01

DEFAULT_ALTITUDE = 1.0

TRAJECTORY_OUTPUT = (
    TRAJECTORIES_DIR /
    "trajectory.csv"
)

# =====================================================
# ORB-SLAM3 SETTINGS
# =====================================================

USE_SLAM = True

ORB_SLAM3_DIR = PROJECT_ROOT / "ORB_SLAM3"

VOCABULARY_PATH = (
    ORB_SLAM3_DIR /
    "Vocabulary" /
    "ORBvoc.txt"
)

CAMERA_YAML = (
    ORB_SLAM3_DIR /
    "Examples" /
    "Monocular" /
    "camera.yaml"
)

SLAM_EXECUTABLE = (
    ORB_SLAM3_DIR /
    "Examples" /
    "Monocular" /
    "mono_tum"
)

SLAM_OUTPUT_DIR = SLAM_RESULTS_DIR

# =====================================================
# DATASET FILES
# =====================================================

IMAGE_INDEX_FILE = "image_index.csv"

SENSOR_FILE = "sensor.csv"

ESP_STATUS_FILE = "esp_status.csv"

MISSION_EVENTS_FILE = "mission_events.csv"

METADATA_FILE = "metadata.json"

# =====================================================
# CSV HEADERS
# =====================================================

IMAGE_HEADERS = [

    "timestamp",

    "image_name"

]

SENSOR_HEADERS = [

    "timestamp",

    "image_name",

    "roll",

    "pitch",

    "yaw",

    "flow_comp_m_x",

    "flow_comp_m_y",

    "flow_rate_x",

    "flow_rate_y",

    "flow_x",

    "flow_y",

    "ground_distance",

    "quality",

    "sensor_id"

]

# =====================================================
# FEATURE DATABASE
# =====================================================

LOCALIZATION_RESULTS = (

    OUTPUTS_DIR /

    "localization_results.csv"

)

# =====================================================
# DASHBOARD
# =====================================================

DASHBOARD_HOST = "0.0.0.0"

DASHBOARD_PORT = 5000

# =====================================================
# LOGGING
# =====================================================

LOG_LEVEL = "INFO"

LOG_FILE = LOGS_DIR / "cosmic.log"

# =====================================================
# DEBUG
# =====================================================

SHOW_KEYPOINTS = False

SHOW_MATCHES = False

PRINT_TELEMETRY = False

# =====================================================
# SORTIE 2 SETTINGS
# =====================================================

ENABLE_SORTIE_2 = False

SEND_WAYPOINTS = False

WAYPOINT_ALTITUDE = 2.0

MISSION_SPEED = 1.0

# =====================================================
# COLORS
# =====================================================

SUCCESS_COLOR = (0, 255, 0)

WARNING_COLOR = (0, 255, 255)

ERROR_COLOR = (0, 0, 255)

# =====================================================
# VERSION
# =====================================================

PROJECT_NAME = "COSMIC_GROUND"

VERSION = "2.0"

AUTHOR = "Team Bitstream"

# =====================================================
# STARTUP MESSAGE
# =====================================================

print("=" * 60)
print(PROJECT_NAME)
print("Version :", VERSION)
print("Project Root :", PROJECT_ROOT)
print("=" * 60)