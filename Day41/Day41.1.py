#!/usr/bin/python
# -*- coding: utf-8 -*-ros

import rospy
from insta.srv import calculator
from insta.srv import calculatorRequest
from insta.srv import calculatorResponse


def callback_calci(req):
    result = 0

    if str(req.symbol) == '+':
        result = req.a + req.b

    elif str(req.symbol) == '-':
        result = req.a - req.b

    elif str(req.symbol) == '*':
        result = req.a * req.b

    elif str(req.symbol) == '/':

        try:
            result = req.a / req.b

        except ZeroDivisionError:
            result = "Can’t divide by 0"

    return calculatorResponse(result)


def calculate():
    rospy.init_node('Calculator')
    s = rospy.Service('calci', calculator, callback_calci)
    print("calculator starting ")
    rospy.spin()


if __name__ == "__main__":
    calculate()