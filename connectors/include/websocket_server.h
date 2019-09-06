/*
//          ______ ___  ___  ____ ___
//      __ / / / // _ )/ _ )|_  // _ \
//     / // /_  _/ _  / _  |/_ </ , _/
//     \___/ /_//____/____/____/_/|_|
//
//   Created by J4BB3R on 27/08/19.
*/

#ifndef TRAFFIC_ORCHESTRATOR_WEBSOCKET_SERVER_H
#define TRAFFIC_ORCHESTRATOR_WEBSOCKET_SERVER_H

#include <websocketpp/config/asio_no_tls.hpp>
#include <websocketpp/server.hpp>

class WebsocketServer {
public:
    WebsocketServer();
    ~WebsocketServer() {
        delete m_server;
    }
private:
    int m_port{8081}; // Default ones
    websocketpp::server<websocketpp::config::asio>* m_server;
};


#endif //TRAFFIC_ORCHESTRATOR_WEBSOCKET_SERVER_H
