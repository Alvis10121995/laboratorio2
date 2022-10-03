#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(80)
m = Twist() 

print(" movimiento de robot circular ")
m.linear.x = 0.5
m.angular.z = 1.3
while not rospy.is_shutdown(): pub.publish(m)
rate.sleep()

