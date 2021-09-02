#! /usr/bin/python

import rospy
from std_msgs.msg import String
from rmp08.msg import dennis

def talk():
    pub=rospy.Publisher("talking",dennis,queue_size=10)
    rospy.init_node("publisher",anonymous=True)
    rate=rospy.Rate(1)
    rospy.loginfo("publishing messages started")
    while not rospy.is_shutdown():
        msg=dennis()
        msg.message="my structure is"
        msg.x=3.0
        msg.y=5.0
        pub.publish(msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        talk()
    except rospy.ROSInterruptException:
        pass