from MotorModule import Motor

motor= Motor(2,3,4,17,22,27)

def main():
    motor.move(0.6,0,2)
    motor.stop(2)
    motor.move(-0.5,0.2,2)
    motor.stop(2)

if __name__ == '__main__':
    while True:
        main()