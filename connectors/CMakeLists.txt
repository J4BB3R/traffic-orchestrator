cmake_minimum_required(VERSION 3.13 FATAL_ERROR)

project(connectors
        VERSION 0.1.0
        LANGUAGES CXX)

include(FetchContent)

FetchContent_Declare(websocketpp
        URL https://github.com/zaphoyd/websocketpp/archive/master.zip
        SOURCE_DIR ${CMAKE_BINARY_DIR}/websocketpp)

FetchContent_GetProperties(websocketpp)
if (NOT EXISTS ${CMAKE_BINARY_DIR}/lib/websocketpp)
    message("[INFO] We're downloading the WebSocket++ library ...")
    FetchContent_Populate(websocketpp)
    message("[INFO] The source code is available at -> " ${websocketpp_SOURCE_DIR})
    file(COPY ${websocketpp_SOURCE_DIR}/websocketpp DESTINATION ${CMAKE_BINARY_DIR}/lib)
    file(REMOVE_RECURSE ${websocketpp_SOURCE_DIR})
endif ()

set(LIB_H
        include/protocol.h
        include/tcp_interface.h
        include/udp_interface.h
        include/websocket_server.h
        include/network_manager.h)

set(LIB_SRC
        protocol.cpp
        tcp_interface.cpp
        udp_interface.cpp
        websocket_server.cpp
        network_manager.cpp)

add_library(${PROJECT_NAME} SHARED ${LIB_SRC})

target_include_directories(includes INTERFACE ${LIB_H}
                            ${CMAKE_BINARY_DIR}/lib) # Not the prettiest but it works

target_link_libraries(${PROJECT_NAME} includes)

set_target_properties(${PROJECT_NAME} PROPERTIES
        VERSION ${PROJECT_VERSION}
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")

target_include_directories(${PROJECT_NAME}
        PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>)
