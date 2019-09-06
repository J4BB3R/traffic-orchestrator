/*
//          ______ ___  ___  ____ ___
//      __ / / / // _ )/ _ )|_  // _ \
//     / // /_  _/ _  / _  |/_ </ , _/
//     \___/ /_//____/____/____/_/|_|
//
//   Created by J4BB3R on 27/08/19.
*/

#include <websocket_server.h>
#include <iostream>

WebsocketServer::WebsocketServer() {
    try {
        m_server = new websocketpp::server<websocketpp::config::asio>();

        m_server->set_access_channels(websocketpp::log::alevel::all);
        m_server->clear_access_channels(websocketpp::log::alevel::frame_payload);

        m_server->init_asio();

        m_server->listen(m_port);
        m_server->start_accept();
        m_server->run();

    } catch (websocketpp::exception const& e) {
        std::cout << e.what() << std::endl;
    } catch (...) {
        std::cout << "Something wrong with WebSocket++ ..." << std::endl;
    }
}

