#pub
#!/usr/bin/python

import rospy
from geometry_msgs.msg import Twist

def publisher():
	rospy.init_node('hi', )
	pub = rospy.Publisher('hello', Twist, queue_size=10)
	rate = rospy.Rate(10)
	a=Twist()
	while not rospy.is_shutdown():
		a.linear.x =10
		a.angular.z =20
		pub.publish(a)
		rate.sleep()

publisher()