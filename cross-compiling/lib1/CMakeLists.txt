cmake_minimum_required(VERSION 3.15)
project(lib1 CXX)

add_library(lib1 src/lib1.cpp)
target_include_directories(lib1 PUBLIC include)

set_target_properties(lib1 PROPERTIES PUBLIC_HEADER "include/lib1.h")
install(TARGETS lib1)
