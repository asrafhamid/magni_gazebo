cmake_minimum_required(VERSION 2.8.3)
project(magni_gazebo)

find_package(catkin REQUIRED COMPONENTS
    roscpp
    sensor_msgs
    message_generation
)

generate_messages(DEPENDENCIES sensor_msgs)

catkin_package(
    CATKIN_DEPENDS roscpp sensor_msgs message_runtime
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

add_executable(publish_img src/publish_img.cpp)
add_dependencies(publish_img ${catkin_EXPORTED_TARGETS})
target_link_libraries(publish_img ${catkin_LIBRARIES})

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)
install(DIRECTORY param/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/param
)
