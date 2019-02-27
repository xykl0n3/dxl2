import dxl2
import time
from dxl2 import register

conn = dxl2.Connection("/dev/tty.usbserial-FT1SF3Q6")
conn.open_port()

 m = dxl2.Motor(conn, 4, dxl2.MotorType.AX)
# print(m.read(register.Instruction.PRESENT_POSITION))

# for i in range(1, 13):
#     m = dxl2.Motor(conn, i, dxl2.MotorType.AX)
#     m.write(register.Instruction.MOVING_SPEED, 100)
#     # print(i, m.read(register.Instruction.PRESENT_POSITION))
#     if i == 2:
#         m.write(register.Instruction.GOAL_POSITION, 205)
#     elif i % 3 != 1:
#         m.write(register.Instruction.GOAL_POSITION, 450)
#     else:
#         m.write(register.Instruction.GOAL_POSITION, 512)


# # print(m.read(register.Instruction.GOAL_POSITION))

# # from dynamixel_sdk import *

# # port_handler = PortHandler("/dev/tty.usbserial-FT1SF3Q6")
# # port_handler.openPort()
# # packet_handler = PacketHandler(1.0)
# # print(packet_handler.ping(port_handler, 2))""

m.write(register.Instruction.GOAL_POSITION,715)
time.sleep(1)
m.write(register.Instruction.GOAL_POSITION,250)