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

        m_server->set_open_handler(bind(&WebsocketServer::on_open,this,websocketpp::lib::placeholders::_1));
        m_server->set_close_handler(bind(&WebsocketServer::on_close,this,websocketpp::lib::placeholders::_1));

        m_server->listen(m_port);
        m_server->start_accept();
        m_server->run();

    } catch (websocketpp::exception const& e) {
        std::cout << e.what() << std::endl;
    } catch (...) {
        std::cout << "Something wrong with WebSocket++ ..." << std::endl;
    }
}

void WebsocketServer::on_open(websocketpp::connection_hdl hdl) {
    m_connections.insert(hdl);
}

void WebsocketServer::on_close(websocketpp::connection_hdl hdl) {
    m_connections.erase(hdl);
}

void WebsocketServer::sendToAll(const std::string& message) {
    for (const auto& it : m_connections) {
        m_server->send(it,message,websocketpp::frame::opcode::text);
    }
}

