cmake_minimum_required(VERSION 3.15)
project(mainproject CXX)

add_executable(mainproject mainproject.cpp main.cpp)

install(TARGETS mainproject DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
