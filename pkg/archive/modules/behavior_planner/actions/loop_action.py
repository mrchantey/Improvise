from pkg.modules.behavior_planner.actions.action import Action


class LoopAction(Action):
    def __init__(self, loop=False):
        Action.__init__(self)
        self.loop = loop

    def DoneRunning(self):
        print "IS LOOPING", self.loop
        if self.loop:
            self.Run()
