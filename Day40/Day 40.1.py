#!/usr/bin/python

import rospy
from insta.srv import multiplier,multiplierResponse

def multiplier_client(x,y):
    rospy.init_node("client")
    rospy.wait_for_service("multiplication")
    rate=rospy.Rate(1)
    while not rospy.is_shutdown():
        try:
            multiply_two_ints=rospy.ServiceProxy("multiplication",multiplier)
            response=multiply_two_ints(x,y)
            rospy.loginfo(response.result)
            rate.sleep()
        except rospy.ServiceException as e:
            print("service call failed %s",e)


if __name__ == "__main__":
    multiplier_client(7,5)
