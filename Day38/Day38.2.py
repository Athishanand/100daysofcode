#! /usr/bin/python

import rospy
from std_msgs.msg import String
from insta.msg import learnros


def callback(data):
    rospy.loginfo("%s x: ", data.message)


def listener():
    rospy.init_node('custom_listener', anonymous=True)
    rospy.Subscriber("custom_chatter", learnros, callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
