cmake_minimum_required(VERSION 3.13 FATAL_ERROR)

project(containers
        VERSION 0.1.0
        LANGUAGES CXX)

set(LIB_H
        telemetry_data.h)

target_include_directories(includes INTERFACE ${LIB_H})
