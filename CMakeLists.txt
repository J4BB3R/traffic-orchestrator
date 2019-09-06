cmake_minimum_required(VERSION 3.13 FATAL_ERROR)

project(traffic-orchestrator
        VERSION 0.1.0
        LANGUAGES CXX)

include(FetchContent)
FetchContent_Declare(asio
        URL https://github.com/chriskohlhoff/asio/archive/asio-1-12-2.zip # Need 1.12.2 overwise some problems will occurs.
        SOURCE_DIR ${CMAKE_BINARY_DIR}/asio)

FetchContent_GetProperties(asio)
if (NOT EXISTS ${CMAKE_BINARY_DIR}/lib/asio)
    message("[INFO] We're downloading the Asio library ...")
    FetchContent_Populate(asio)
    message("[INFO] The source code is available at -> " ${asio_SOURCE_DIR})
    file(COPY ${asio_SOURCE_DIR}/asio/include/asio DESTINATION ${CMAKE_BINARY_DIR}/lib)
    file(COPY ${asio_SOURCE_DIR}/asio/include/asio.hpp DESTINATION ${CMAKE_BINARY_DIR}/lib)
    file(REMOVE_RECURSE ${asio_SOURCE_DIR})
endif ()

add_compile_options("-DASIO_STANDALONE")
add_compile_options("-DASIO_HAS_STD_THREAD")

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_compile_options("-Wall")
#add_compile_options("-Werror")
add_compile_options("-Wextra")
add_compile_options("-O0")
add_compile_options("-g")

set(CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR}/lib)

add_library(includes INTERFACE)

add_subdirectory(containers)
add_subdirectory(connectors)

add_executable(${PROJECT_NAME} traffic-orchestrator.cpp)

target_link_libraries(${PROJECT_NAME} connectors
                                        pthread
                                        includes)