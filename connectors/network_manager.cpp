/*
//          ______ ___  ___  ____ ___ 
//      __ / / / // _ )/ _ )|_  // _ \
//     / // /_  _/ _  / _  |/_ </ , _/
//     \___/ /_//____/____/____/_/|_| 
//                                 
//   Created by J4BB3R on 02/09/19.
*/

#include <network_manager.h>

NetworkManager::NetworkManager() {
    m_websocket = new WebsocketServer();
}

NetworkManager::~NetworkManager() {
    delete m_tcp_iface;
    delete m_udp_iface;
    delete m_websocket;
}
