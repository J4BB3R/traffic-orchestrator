//
//          ______ ___  ___  ____ ___ 
//      __ / / / // _ )/ _ )|_  // _ \
//     / // /_  _/ _  / _  |/_ </ , _/
//     \___/ /_//____/____/____/_/|_| 
//                                 
//   Created by J4BB3R on 28/08/19.
//

#ifndef TRAFFIC_ORCHESTRATOR_TELEMETRY_DATA_H
#define TRAFFIC_ORCHESTRATOR_TELEMETRY_DATA_H

struct Telemetry_Paquet {
    std::string uuid;
    int64_t time;
    Gps_Point coordinates;
    long lane_id;
    double speed;
    double accelleration;
    double heading;
    double yaw_rate;
};

struct GPS_Point {
    double latitude;
    double longitude;
};

#endif //TRAFFIC_ORCHESTRATOR_TELEMETRY_DATA_H
