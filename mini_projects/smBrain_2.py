import math
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io


def clearTest(selectedSensors, threshold):
    return min(selectedSensors) > threshold


def wall(sensors, clearDist):
    return not clearTest(sensors, clearDist)


class MySMClass(sm.SM):
    startState = 'seek'

    def getNextValues(self, state, inp):
        fvel = 0.2
        rvel = 0.2
        sideClearDist = 0.35
        clearDist = 0.4

        forward = io.Action(fvel, 0)
        left = io.Action(0, rvel)
        right = io.Action(sideClearDist * rvel, -rvel)
        front = inp.sonars[2:4]
        rightsensors = inp.sonars[2:5]

        if state == 'seek':
            if wall(front, clearDist):
                return ('following', left)
            elif wall(rightsensors, clearDist):
                return ('following', forward)
            else:
                return ('seek', forward)
        else:
            if wall(front, clearDist):
                return ('following', left)
            elif wall(rightsensors, sideClearDist):
                return ('following', forward)
            else:
                return ('following', right)

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
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False,  # slime trails
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
