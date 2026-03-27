cmake_minimum_required(VERSION 3.30)

project(cryptopp-pem)

find_package(cryptopp REQUIRED)

add_library(cryptopp-pem 
    pem_common.cpp
    pem_read.cpp
    pem_write.cpp
    x509cert.cpp)

target_sources(cryptopp-pem INTERFACE FILE_SET HEADERS FILES
    pem.h
    pem_common.h
    x509cert.h)

target_link_libraries(cryptopp-pem PRIVATE
    cryptopp::cryptopp
)

install(TARGETS cryptopp-pem
    FILE_SET HEADERS DESTINATION include/cryptopp)