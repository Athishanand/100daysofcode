import math, random

def generateOTP():

    digits = "0123456789"

    OTP = ""


    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


if __name__ == "__main__":
    print("Your 4 digits OTP is:", generateOTP())
