#! /usr/bin/env python
#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/turtleCircle.py

import rospy
from geometry_msgs.msg import Twist
import math
rospy.init_node('walker', anonymous=True)
velocityPublisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

PI = math.pi

speed = 10.0
angle = 90.0

def getInput():
    global radius
    print("The entered radius will be divided with 7.0 to avoid hitting to the wall!")
    inputRadius = input("Enter radius: ")
    radius = float(inputRadius)/7.0

def turnToTop(angularSpeed, relativeAngle, z):
    vel_msg = Twist()    
    vel_msg.angular.z = abs(z)
    currentAngle = 0.0
    t0 = rospy.Time.now().to_sec()
    while(currentAngle<relativeAngle):
        velocityPublisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        currentAngle = angularSpeed*(t1-t0)
        
def moveLinear(mRadius, x):
    vel_msg = Twist()
    vel_msg.linear.x = x  
    current_distance = 0   
    t0 = rospy.Time.now().to_sec()
    while(current_distance<mRadius):
        velocityPublisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance = mRadius*(t1-t0)
          
def turnToClockwise(rSpeed, z):
    vel_msg = Twist()       
    vel_msg.angular.z = -z    
    curdistance = 0
    t0 = rospy.Time.now().to_sec()
    while(curdistance<rSpeed):
        velocityPublisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        curdistance = rSpeed*(t1-t0)
        
def drawCircle(perimeter, distance, x, z):
    print('radius:', x*2)
    vel_msg = Twist()        
    vel_msg.linear.x = x
    vel_msg.angular.z = -z 
    t0 = rospy.Time.now().to_sec()
    current_perimeter = 0    
    while(current_perimeter<perimeter):
        velocityPublisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_perimeter = distance*(t1-t0)
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocityPublisher.publish(vel_msg)
        
if __name__ == '__main__':
    try:
        getInput()
        
        turnToTop(speed*PI/180, (angle*PI/180), speed*PI/180)
        moveLinear(radius, 0.5*radius)        
        turnToClockwise(speed, angle*PI/180) 
        drawCircle(2*PI*radius, radius, 0.5*radius, 1.0)
        
        turnToTop(speed*PI/180, angle*PI/180, speed*PI/180)       
        moveLinear(2*radius, 1.0*radius)        
        turnToClockwise(speed, angle*PI/180)
        drawCircle(2*2*PI*radius, 2*radius, 1.5*radius, 1.0)
        
        turnToTop(speed*PI/180, angle*PI/180, speed*PI/180)
        moveLinear(2*radius, 1.0*radius)
        turnToClockwise(speed, angle*PI/180)
        drawCircle(2*2*2*PI*radius, 2*2*radius, 2.5*radius, 1.0)
        
        turnToTop(speed*PI/180, angle*PI/180, speed*PI/180)
        moveLinear(2*radius, 1.0*radius)
        turnToClockwise(speed, angle*PI/180)
        drawCircle(2*2*2*2*PI*radius, 2*2*2*radius, 3.5*radius, 1.0)
        
    except rospy.ROSInterruptException:
        pass
