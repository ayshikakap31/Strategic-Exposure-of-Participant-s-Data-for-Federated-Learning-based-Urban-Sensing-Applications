# Brightkite Dataset

This repository contains files from the Brightkite Dataset, used for research and analysis in urban sensing and federated learning privacy preservation. The dataset represents GPS trajectory data for individual users, including latitude, longitude, and timestamp information. Each user’s movement and location data provide insights into spatial-temporal patterns valuable for studies in location-based services, trajectory analysis, and privacy protection.

## Dataset Overview

The Brightkite dataset includes user check-in data collected from the Brightkite social network, capturing user movements across various locations. The data includes:

Latitude and Longitude: Geographic coordinates of the user’s location.
Timestamp: The time associated with each check-in or recorded GPS point.

## Files Overview
Each user has two types of files:

user_<ID>.csv: The original dataset file collected for each user, containing raw GPS and check-in data.
user_<ID>_latlontime.csv: The preprocessed dataset with structured latitude, longitude, and time columns for further analysis.
