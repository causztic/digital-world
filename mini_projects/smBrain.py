import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io


class MySMClass(sm.SM):
    startState = "initial"

    def __init__(self):
        self.resetTheta()

    def setTheta(self, theta):
        if self.original_theta == -1:
            self.original_theta = theta

    def resetTheta(self):
        self.original_theta = -1

    def getNextValues(self, state, inp):
        fvel = 0
        rvel = 0
        front_dist = 0.5
        lower_bound = front_dist - 0.1
        upper_bound = front_dist + 0.1

        # Sensors
        front_left = inp.sonars[1]
        front = inp.sonars[2]
        front_right = inp.sonars[3]
        right = inp.sonars[4]

        bot_too_far =  front > front_dist
        bot_too_near = front < front_dist - 0.1
        no_right_side = right > front_dist

        fr_lower_bound = lower_bound / math.cos(math.pi / 4)
        fr_upper_bound = upper_bound / math.cos(math.pi / 4)

        fr_within_bounds = front_right > fr_lower_bound and front_right < fr_upper_bound
        r_within_bounds = right > lower_bound and right < upper_bound

        within_bounds = fr_within_bounds and r_within_bounds

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
                fvel = 0.1
                nextState = "navigate"
            elif bot_too_near:
                fvel = -0.1
                nextState = "navigate"
            else:
                nextState = "rotate_left"
            if no_right_side:
                nextState = "rotate_right"

        if state == "rotate_left":
            if not within_bounds:
                fvel = 0
                rvel = 0.2
                nextState = "rotate_left"
            else:
                fvel = 0.2
                rvel = 0
                nextState = "navigate"
                #nextState = "compensate_right"

        # if state == "rotate_right":
        #     fvel = 0
        #     nextState ="rotate_right"
        #     else:
        #         nextState = "navigate"

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
                                  sonarMonitor=False)  # sonar monitor widget

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
