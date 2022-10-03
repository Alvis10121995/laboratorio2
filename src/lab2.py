#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(80)
m = Twist()

print(" 1 linea frontal \n 2 linea reversa \n ")
opc = input("seleccione ")
if opc == 1:m.linear.x = 0.5
m.linear.y = 0.5
m.angular.z = 0.0
if opc == 2:
 m.linear.x = -0.5
m.angular.z = 0.0
while not rospy.is_shutdown(): pub.publish(m)
rate.sleep()
