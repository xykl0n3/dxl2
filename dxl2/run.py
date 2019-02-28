import dxl2
import time
from dxl2 import register




conn = dxl2.Connection("/dev/tty.usbserial-FT1SF3Q6")
conn.open_port()

#  m = dxl2.Motor(conn, 4, dxl2.MotorType.AX)
# print(m.read(register.Instruction.PRESENT_POSITION))

# for i in range(1, 13):
#     m = dxl2.Motor(conn, i, dxl2.MotorType.AX)
#     d = dxl2.Motor(conn,i-1,dxl2.MotorType.AX)
#     m.write(register.Instruction.MOVING_SPEED, 100)
#     # print(i, m.read(register.Instruction.PRESENT_POSITION))
    
#     if i % 3 != 1:
#         m.write(register.Instruction.GOAL_POSITION, 450)
#     else:
#         m.write(register.Instruction.GOAL_POSITION, 512)



####### gait ######

def stand():

    text_file = open("stand.txt", "r")
    pos= []
    for val in text_file.read().split(','):
    pos.append(int(val))
    text_file.close()
    for i in range (1,13):
        m = dxl2.Motor(conn, i, dxl2.MotorType.AX)
        m.write(register.Instruction.GOAL_POSITION, pos)
        time.sleep(0.5)


def walk():

    text_file = open("walk.txt", "r")
    pos= []
    for val in text_file.read().split(','):
    pos.append(int(val))
    text_file.close()



