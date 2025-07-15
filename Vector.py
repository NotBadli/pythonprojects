import anki_vector
import time

def Rock():
    robot.motors.set_head_motor(-3)
    robot.motors.set_lift_motor(-3)
    robot.motors.set_wheel_motors(0, -50)
    time.sleep(0.5)
    robot.motors.set_head_motor(5)
    robot.motors.set_lift_motor(10)
    robot.motors.set_wheel_motors(-50, 0)
    time.sleep(0.5)

def Rock2():
    def DanceMove():
        robot.motors.set_head_motor(5)
        robot.motors.set_lift_motor(-5)
        robot.motors.set_wheel_motors(0, -100)
        time.sleep(0.5)
        robot.motors.set_head_motor(-5)
        robot.motors.set_lift_motor(5)
        robot.motors.set_wheel_motors(-100, 0)
        time.sleep(0.5)
    
    DanceMove()
    DanceMove()
    
    robot.motors.stop_all_motors

    robot.motors.set_wheel_motors(0, -100)
    time.sleep(1)

with anki_vector.Robot() as robot:

    Rock()
    Rock()
    Rock()
    Rock()
    Rock2()
    Rock2()
    Rock2()
    Rock2()

    robot.motors.stop_all_motors