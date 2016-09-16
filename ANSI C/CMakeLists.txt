cmake_minimum_required(VERSION 3.6)
project(ex_14)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c90 -Wall -Werror -pedantic")

set(SOURCE_FILES test.c)
add_executable(ex_14 ${SOURCE_FILES})
target_link_libraries(ANCI_C m)
