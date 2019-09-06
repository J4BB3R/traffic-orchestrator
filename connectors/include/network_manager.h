/*
//          ______ ___  ___  ____ ___ 
//      __ / / / // _ )/ _ )|_  // _ \
//     / // /_  _/ _  / _  |/_ </ , _/
//     \___/ /_//____/____/____/_/|_| 
//                                 
//   Created by J4BB3R on 02/09/19.
*/

#ifndef TRAFFIC_ORCHESTRATOR_NETWORK_MANAGER_H
#define TRAFFIC_ORCHESTRATOR_NETWORK_MANAGER_H

#include "websocket_server.h"
#include "udp_interface.h"
#include "tcp_interface.h"

class NetworkManager {
public:
    NetworkManager();
    ~NetworkManager();
private:
    WebsocketServer* m_websocket;
    UDPInterface* m_udp_iface;
    TCPInterface* m_tcp_iface;
};


#endif //TRAFFIC_ORCHESTRATOR_NETWORK_MANAGER_H
