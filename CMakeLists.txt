PROJECT(ben)
CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

find_package( PkgConfig )

# We need C++11
# SET(ENV{CXX} "g++-4.8")
# SET(ENV{CXX} /usr/bin/g++-4.8)
# SET(CMAKE_CXX_COMPILER GNU VERSION 4.8)
# SET(CMAKE_CXX_COMPILER /usr/bin/g++-4.8)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
ADD_DEFINITIONS("-Wall")

# find boost
FIND_PACKAGE(Boost 1.46 COMPONENTS system thread python numpy)
SET(Boost_USE_STATIC_LIBS OFF)
SET(Boost_USE_MULTITHREADED ON)
SET(Boost_USE_STATIC_RUNTIME OFF)
INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIRS})
LINK_DIRECTORIES(${Boost_LIBRARY_DIRS})

# find eigen
INCLUDE_DIRECTORIES(/usr/include/eigen3)
pkg_check_modules( EIGEN3 REQUIRED eigen3 )
include_directories( ${EIGEN3_INCLUDE_DIRS} )
LINK_DIRECTORIES(${EIGEN3_LIBRARY_DIRS})

# find python
FIND_PACKAGE(PythonLibs 2.7 REQUIRED)
INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_DIRS})
LINK_DIRECTORIES(${PYTHON_LIBRARIES})

# we have an extensive script to find numpy
INCLUDE(FindNumPy.cmake)
INCLUDE_DIRECTORIES(${NUMPY_INCLUDE_DIRS})
LINK_DIRECTORIES(${NUMPY_LIBRARY_DIRS})

# find glog
#! FIXME
SET(GLOG_INCLUDE_DIRS /usr/local/include/glog)
SET(GLOG_LIBRARY_DIRS /usr/local/lib)
SET(GLOG_LIBRARIES /usr/local/lib/libglog.so)
#
INCLUDE_DIRECTORIES(${GLOG_INCLUDE_DIRS})
LINK_DIRECTORIES(${GLOG_LIBRARY_DIRS})

# gather it all together

# build our actual library
INCLUDE_DIRECTORIES(include)
ADD_LIBRARY(ben SHARED
  src/ben.cpp
  src/ben_module.cpp
  )
TARGET_LINK_LIBRARIES(ben
  ${Boost_LIBRARIES}
  ${PYTHON_LIBRARIES}
  ${NUMPY_LIBRARIES}
  ${EIGEN3_LIBRARIES}
  ${GLOG_LIBRARIES}
  )