cmake_minimum_required(VERSION 3.15)
project(lib2 CXX)

add_library(lib2 src/lib2.cpp)
target_include_directories(lib2 PUBLIC include)

set_target_properties(lib2 PROPERTIES PUBLIC_HEADER "include/lib2.h")
install(TARGETS lib2)
