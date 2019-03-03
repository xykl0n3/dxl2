import dxl2
import time
from dxl2 import register




conn = dxl2.Connection("/dev/ttyUSB0")
conn.open_port()

# for i in range (1,11):
#         m = dxl2.Motor(conn, i, dxl2.MotorType.AX)
#         print(m.read(register.Instruction.PRESENT_POSITION))        


####### gait ######

# def stand():

text_file = open("motion/stand.txt", "r")
pos= []
for val in text_file.read().split(','):
        pos.append(int(val))
        text_file.close()


def write():
        for list in pos:
                for i in range (1,11):
                        m = dxl2.Motor(conn, i, dxl2.MotorType.AX)
                        m.write(register.Instruction.MOVING_SPEED,40)
                        
                        m.write(register.Instruction.GOAL_POSITION, list[i-1])

def read():     
        for i in range (1,11):
                m = dxl2.Motor(conn, i, dxl2.MotorType.AX)
                print(m.read(register.Instruction.PRESENT_POSITION))
        
# for i in range (7,9):
#         m = dxl2.Motor(conn, i, dxl2.MotorType.AX)
#        # print(m.read(register.Instruction.PRESENT_POSITION))
#         m.write(register.Instruction.MOVING_SPEED,40)
#         m.write(register.Instruction.GOAL_POSITION,512)
       
#m.write(register.Instruction.TORQUE_ENABLE,0)



# def walk():

#     text_file = open("walk.txt", "r")
#     pos= []
#     for val in text_file.read().split(','):
#     pos.append(int(val))
#     text_file.close()



