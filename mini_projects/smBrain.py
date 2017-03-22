import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io


class MySMClass(sm.SM):
    startState = "initial"

    def __init__(self):
        self.original_theta = -1
        self.turns = 0

    def setTheta(self, theta):
        if self.original_theta == -1:
            self.original_theta = theta

    def resetTheta(self):
        self.original_theta = -1

    def getNextValues(self, state, inp):
        fvel = 0
        rvel = 0

        t = inp.odometry.theta
        p = math.pi / 2
        fvel = 0.2
        rvel = 0
        state_rotation = state == "rotate_left" or state == "rotate_right"
        bot_too_far = inp.sonars[2] > 0.7
        #bot_too_near = inp.sonars[1] < 0.3 or inp.sonars[2] < 0.3 or inp.sonars[3] < 0.3
        bot_too_near = inp.sonars[2] < 0.6
        no_right_side = inp.sonars[4] > 0.6

        if state == "initial":
            if bot_too_far:
                fvel = 0.2
                nextState = "initial"
            elif bot_too_near:
                fvel = -0.2
                nextState = "initial"
            else:
                nextState = "rotate_left"

        if state == "navigate":
            if bot_too_far:
                fvel = 0.2
                nextState = "navigate"
            elif bot_too_near:
                fvel = -0.2
                nextState = "navigate"
            else:
                nextState = "rotate_left"
            if no_right_side:
                nextState = "rotate_right"

        if state_rotation:
            fvel = 0
            self.setTheta(t)

        if state == "rotate_left":
            fvel = 0.3
            rvel = 0.5
            if self.original_theta > 6.2 and t < 0.02:
                self.original_theta = 0
            if abs(t - self.original_theta) < p:
                rvel = math.pi / 6
                nextState = "rotate_left"
            else:
                nextState = "compensate_right"

        if state == "rotate_right":
            fvel = 0.3
            rvel = -0.5
            if self.original_theta < 0.02 and t > 6.2:
                self.original_theta = 2 * math.pi
            if abs(t - self.original_theta) < p:
                rvel = -math.pi / 6
                nextState = "rotate_right"
            else:
                nextState = "compensate_left"

        if state == "compensate_right":
            fvel = 0
            if abs(self.original_theta - t) > p:
                rvel = -0.1
                nextState = "compensate_right"
            else:
                self.resetTheta()
                nextState = "navigate"

        if state == "compensate_left":
            fvel = 0
            if abs(self.original_theta - t) > p:
                rvel = 0.1
                nextState = "compensate_left"
            else:
                self.resetTheta()
                nextState = "navigate"

        if state != nextState:
            print nextState
        return (nextState, io.Action(fvel=fvel, rvel=rvel))

mySM = MySMClass()
mySM.name = 'brainSM'

######################################################################
###
# Brain methods
###
######################################################################


def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar' + str(sonarNum),
                                        lambda:
                                        io.SensorInput().sonars[sonarNum]))

# this function is called when the brain is (re)loaded


def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=True,  # slime trails
                                  sonarMonitor=True)  # sonar monitor widget

    # set robot's behavior
    robot.behavior = mySM

# this function is called when the start button is pushed


def brainStart():
    robot.behavior.start(traceTasks=robot.gfx.tasks())

# this function is called 10 times per second


def step():
    inp = io.SensorInput()
    # print inp.sonars[3]
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())

# called when the stop button is pushed


def brainStop():
    pass

# called when brain or world is reloaded (before setup)


def shutdown():
    pass
