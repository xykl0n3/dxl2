from enum import Enum
from typing import Tuple, Dict, List


class Instruction(Enum):
    MODEL_NUMBER_L = 1
    MODEL_NUMBER_H = 2
    MODEL_NUMBER = 3
    FIRMWARE_VERSION = 4
    ID = 5
    BAUD_RATE = 6
    RETURN_DELAY_TIME = 7
    CW_ANGLE_LIMIT_L = 8
    CW_ANGLE_LIMIT_H = 9
    CW_ANGLE_LIMIT = 10
    CCW_ANGLE_LIMIT_L = 11
    CCW_ANGLE_LIMIT_H = 12
    CCW_ANGLE_LIMIT = 13
    HI_LIM_TEMP = 14
    LO_LIM_VOLT = 15
    HI_LIM_VOLT = 16
    MAX_TORQUE_L = 17
    MAX_TORQUE_H = 18
    MAX_TORQUE = 19
    STATUS_RETURN_LVL = 20
    ALARM_LED = 21
    ALARM_SHUTDOWN = 22
    TORQUE_ENABLE = 23
    LED = 24
    CW_COMPLIANCE_MARGIN = 25
    CCW_COMPLIANCE_MARGIN = 26
    CW_COMPLIANCE_SLOPE = 27
    CCW_COMPLIANCE_SLOPE = 28
    GOAL_POSITION_L = 29
    GOAL_POSITION_H = 30
    GOAL_POSITION = 31
    MOVING_SPEED_L = 32
    MOVING_SPEED_H = 33
    MOVING_SPEED = 34
    TORQUE_LIMIT_L = 35
    TORQUE_LIMIT_H = 36
    TORQUE_LIMIT = 37
    PRESENT_POSITION_L = 38
    PRESENT_POSITION_H = 39
    PRESENT_POSITION = 40
    PRESENT_SPEED_L = 41
    PRESENT_SPEED_H = 42
    PRESENT_SPEED = 43
    PRESENT_LOAD_L = 44
    PRESENT_LOAD_H = 45
    PRESENT_LOAD = 46
    PRESENT_VOLTAGE = 47
    PRESENT_TEMPERATURE = 48
    REGISTERED = 49
    MOVING = 50
    LOCK = 51
    PUNCH_L = 52
    PUNCH_H = 53


AX: Dict[Instruction, List[int]] = {
    Instruction.MODEL_NUMBER_L: [0],
    Instruction.MODEL_NUMBER_H: [1],
    Instruction.MODEL_NUMBER: [1, 0],
    Instruction.TORQUE_ENABLE: [24],
    Instruction.GOAL_POSITION: [31, 30],
    Instruction.MOVING_SPEED: [32, 33],
    Instruction.PRESENT_POSITION: [37, 36],
}

MX: Dict[Instruction, List[int]] = {
    Instruction.MODEL_NUMBER_L: [0],
    Instruction.MODEL_NUMBER_H: [1],
    Instruction.MODEL_NUMBER: [1, 0],
    Instruction.TORQUE_ENABLE: [24],
    Instruction.GOAL_POSITION: [31, 30],
    Instruction.MOVING_SPEED: [32, 33],
    Instruction.PRESENT_POSITION: [37, 36],
}
