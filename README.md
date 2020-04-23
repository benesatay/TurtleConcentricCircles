# TurtleConcentricCircles

This project is an exercise to use turtlesim in ROS. The aim of the project is drawing concentric circles. Your needs are explained to run the project. 

![alt text](https://github.com/benesatay/TurtleConcentricCircles/blob/master/outputImage.jpeg)

If you have ROS Environment follow those steps:

1. You have to make executable the code. 
To make executable run that "chmod u+x ~/catkin_ws/src/yourPathname/yourFilename.py" in terminal.
2. run roscore in terminal (writing "roscoe" is enough)
3. run "rosrun turtlesim turtlesim_node" in new terminal
4. run "rosrun yourFilename.py" in another new terminal

If you do not already setup ROS Environment, you have to follow steps that below:

Only Wily (Ubuntu 15.10), Xenial (Ubuntu 16.04) and Jessie (Debian 8) are supported by ROS Kinetic.

You have to setup one of these. I use Xenial. 

You should use VirtualBox to setup OS.

============================

--Installation OF ROS--

sudo apt-get update
sudo apt-get upgrade
wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_kinetic.sh && chmod 755 ./install_ros_kinetic.sh && bash ./install_ros_kinetic.sh

============================

--Installation of Dependentions of ROS Packages--

sudo apt-get install ros-kinetic-joy ros-kinetic-teleop-twist-joy ros-kinetic-teleop-twist-keyboard ros-kinetic-laser-proc ros-kinetic-rgbd-launch ros-kinetic-depthimage-to-laserscan ros-kinetic-rosserial-arduino ros-kinetic-rosserial-python ros-kinetic-rosserial-server ros-kinetic-rosserial-client ros-kinetic-rosserial-msgs ros-kinetic-amcl ros-kinetic-map-server ros-kinetic-move-base ros-kinetic-urdf ros-kinetic-xacro ros-kinetic-compressed-image-transport ros-kinetic-rqt-image-view ros-kinetic-gmapping ros-kinetic-navigation ros-kinetic-interactive-markers

============================

cd ~/catkin_ws/src/
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
cd ~/catkin_ws && catkin_make

============================

You have to apply steps that on the website that shared to install and configure your ROS Environment:
http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment

If you want to make more than that you can visit:
http://wiki.ros.org/ROS/Tutorials
