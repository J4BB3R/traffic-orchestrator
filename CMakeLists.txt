cmake_minimum_required(VERSION 3.13 FATAL_ERROR)

project(traffic-orchestrator)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_compile_options("-Wall")
add_compile_options("-Werror")
add_compile_options("-Wextra")
add_compile_options("-O0")
add_compile_options("-g")

add_executable(${PROJECT_NAME} traffic-orchestrator.cpp)