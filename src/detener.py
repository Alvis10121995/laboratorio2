#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(10)
m = Twist()
m.linear.x = 0.0
while not rospy.is_shutdown(): 
  pub.publish(m)
  rate.sleep()


