cmake_minimum_required(VERSION 3.15)
project(mainproject CXX)

add_executable(mainproject src/mainproject.cpp src/main.cpp)
target_include_directories(mainproject PUBLIC include)

install(TARGETS mainproject)
