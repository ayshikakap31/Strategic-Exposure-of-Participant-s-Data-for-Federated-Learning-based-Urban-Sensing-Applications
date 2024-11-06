# Strategic-Exposure-of-Participant-s-Data-for-Federated-Learning-based-Urban-Sensing-Applications
This repository contains supplementary material for the following work:
- **Title**: "Computation and communication efficient approach for federated learning based urban sensing applications against inference attacks"
- **Authors**: Ayshika Kapoor, Dheeraj Kumar
- **Journal**: Pervasive and Mobile Computing
- **Paper**: [paper.pdf](https://github.com/ayshikakap31/Strategic-Exposure-of-Participant-s-Data-for-Federated-Learning-based-Urban-Sensing-Applications/blob/b52d6373ac5a6715f19ecad4f7de4c370545b62f/Paper.pdf)

For contact, feel free to reach out to "ayshika.kapoor" at gmail dot com.

---

## Overview
- **Goal**:
  - Develop a framework that reduces privacy risks in federated learning for urban sensing applications by strategically controlling the exposure of sensitive and non-sensitive data.
  - Achieve a balance between privacy protection and minimizing computational and communication overheads, which are essential for resource-constrained mobile devices involved in urban sensing.
  - Introduce an adaptive strategy that determines when to use secure multi-party computation (SMC) for transmitting sensitive data points and when to allow direct model updates for non-sensitive locations, enhancing both privacy and efficiency.
  - Employ spatiotemporal entropy and KL divergence as metrics to identify sensitive data points, thereby protecting user privacy without sacrificing model accuracy.
- **Mechanisms**:
  - The framework uses spatiotemporal entropy to assess the sensitivity of data points. Higher entropy indicates less sensitive locations, allowing for direct model updates, while lower entropy signals sensitive areas, prompting the use of secure transmission methods.
  - KL divergence is applied as a metric to detect significant deviations in location data patterns. A higher KL divergence from a flat histogram indicates sensitive, frequently visited locations, triggering secure multi-party computation (SMC) for these data points.
  - An adaptive mechanism dynamically determines whether to transmit data directly or via SMC. This strategic exposure of non-sensitive data minimizes computation and communication costs while protecting sensitive information.
  - To evaluate the proposed methodology against inference attacks, clustering techniques such as DBSCAN, EDDBSCAN and SNN+ have been implemented.
- **Datasets**:
  We perform extensive empirical evaluation on two real-world datasets:
  ### 1. Geolife GPS Trajectory Dataset
  This GPS trajectory dataset was collected in (Microsoft Research Asia) Geolife project by 182 users in a period of over five years (from April 2007 to August 2012). A GPS trajectory of this dataset is represented by a sequence of time-stamped points, each of which contains the information of latitude, longitude and altitude. This dataset contains 17,621 trajectories with a total distance of 1,292,951 kilometers and a total duration of 50,176 hours. These trajectories were recorded by different GPS loggers and GPS- phones, and have a variety of sampling rates. 91 .5 percent of the trajectories are logged in a dense representation, e.g. every 1~ seconds or every 5~10 meters per point.
  This dataset recoded a broad range of users’ outdoor movements, including not only life routines like go home and go to work but also some entertainments and sports activities, such as shopping, sightseeing, dining, hiking, and cycling. This trajectory dataset can be used in many research fields, such as mobility pattern mining, user activity recognition, location-based social networks, location privacy, and location recommendation.
  Although this dataset is wildly distributed in over 30 cities of China and even in some cities located in the USA and Europe, the majority of the data was created in Beijing, China.
  
  **Access**: [Microsoft Research Geolife Project](https://www.microsoft.com/en-us/research/project/geolife-building-social-networks-using-human-location-history/)
  ### 2. Brightkite Dataset
  Brightkite was once a location-based social networking service provider where users shared their locations by checking-in. The friendship network was collected using their public API, and consists of 58,228 nodes and 214,078 edges. The network is originally directed but the collectors have constructed a network with undirected edges when there is a friendship in both ways. The collectors have also collected a total of 4,491,143 checkins of these users over the period of Apr. 2008 - Oct. 2010.
  
  **Access**: [SNAP: Stanford Network Analysis Project](https://snap.stanford.edu/data/loc-brightkite.html)
---

## Citation

If you use this code or any part of this work in your research, please cite our paper:

A. Kapoor and D. Kumar, “Computation and Communication Efficient Approach for Federated Learning based Urban Sensing Applications against Inference Attacks,” _Pervasive and Mobile Computing_, 98, p. 101875, 2024.
