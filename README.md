**COSMIC_GROUND**
### Vision-Based Localization, Mission Processing & Ground Station System
**IRoC-U 2026 | Team Bitstream**

---

## 🌌 Overview

**COSMIC_GROUND** is the ground-station software component of the COSMIC system, developed for the **Indian Rover Challenge – University (IRoC-U) 2026**.

It is designed to process mission data collected by the onboard system, synchronize visual and sensor information, extract image features, reconstruct rover trajectories, and support visual localization using image retrieval and ORB-SLAM3.

The system bridges onboard data acquisition and ground-side analysis by organizing mission images, telemetry, localization results, and trajectory information into a unified processing pipeline.

Rather than treating camera frames and sensor logs as independent datasets, COSMIC_GROUND brings them together to support mission reconstruction and visual analysis.

## 🎯 Project Objectives

- Develop a structured ground-station architecture for rover mission data.
- Capture and organize camera frames with timestamp information.
- Synchronize visual data with sensor telemetry.
- Extract and store ORB image descriptors for visual feature matching.
- Perform image-based localization using reference or seed images.
- Integrate ORB-SLAM3 for visual SLAM processing.
- Reconstruct and visualize rover trajectories.
- Provide a centralized dashboard for mission monitoring and analysis.

## ⚙️ Core Modules

### 1. Mission Data Acquisition

The ground station supports camera-frame capture and structured mission-data storage.

- Camera capture through OpenCV.
- Configurable image resolution and frame rate.
- Timestamp-based image naming.
- Mission-specific image storage.
- Support for onboard sensor and telemetry datasets.

### 2. Dataset Management & Synchronization

The dataset management layer organizes the collected mission information.

It handles:

- Mission image indexing.
- Sensor data loading.
- Timestamp synchronization between images and telemetry.
- Mission metadata management.
- Structured dataset preparation for downstream processing.

### 3. ORB Feature Extraction

COSMIC_GROUND uses **Oriented FAST and Rotated BRIEF (ORB)** for image-feature extraction.

ORB provides distinctive local image features that can be used for efficient image matching.

The feature-processing pipeline includes:

- Keypoint detection.
- Binary descriptor extraction.
- Descriptor storage.
- Reference-image comparison.
- Feature matching for visual recognition.

### 4. Image-Based Localization

The localization subsystem compares incoming or mission images against reference visual information.

Its processing modules support:

- Seed-image-based localization.
- ORB descriptor matching.
- Reference-image retrieval.
- Coordinate lookup.
- Localization result generation.

This provides a visual approach to identifying previously observed locations.

### 5. Visual SLAM Integration
The system includes an ORB-SLAM3 integration layer for visual simultaneous localization and mapping.

The SLAM subsystem is organized around:
- Camera configuration loading.
- ORB vocabulary management.
- Frame management.
- SLAM execution.
- Trajectory and result processing.
ORB-SLAM3 is used as the visual SLAM engine rather than being reimplemented within the project.
6. Trajectory Reconstruction
Sensor and visual information are used in the mission-processing workflow to generate trajectory data.

The trajectory module supports:
- Sensor-data processing.
- Trajectory generation.
- Position-data storage.
- Trajectory visualization.
- Mission-path analysis.
7. Ground Station Dashboard
A Flask-based web dashboard provides a centralized interface for mission information and analysis.

The dashboard includes processing and visualization support for:
- Mission image count.
- Sensor sample count.
- Roll, pitch and yaw.
- Distance information.
- Matched image information.
- Feature matching score.
- Localization information.
- Trajectory coordinates.
**🛠️ Technology Stack**
Category	Technologies
Programming Language	Python
Computer Vision	OpenCV
Feature Extraction	ORB
Visual SLAM	ORB-SLAM3
Backend	Flask
Data Processing	Pandas
Database	SQLite
Data Formats	CSV, JSON
Frontend	HTML, CSS, JavaScript
Hardware Interface	USB Camera / MAVLink-compatible telemetry integration
