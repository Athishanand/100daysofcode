#sub
#! /usr/bin/python

import rospy
from geometry_msgs.msg import Twist

def call(msg):
	print(msg.linear.x)
	print(msg.angular.z)

def subscriber():
	rospy.init_node("subscriber")
	rospy.Subscriber("hello", Twist,call)
	rospy.spin()

if __name__=="__main__":

  subscriber()