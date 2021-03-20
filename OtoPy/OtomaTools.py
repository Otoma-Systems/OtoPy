class OProgressBar():
    prefix = "Progress: "
    suffix = "Complete"
    decimalPlaces = 1
    length = 60
    fill = "█"
    printEnd = "\r"

    def __init__(self, completeState):
        self.completeState = completeState

    def PrintProgess(self, progressState):
        percent = ("{0:." + str(self.decimalPlaces) + "f}").format(100 * (progressState / float(self.completeState)))
        filledLength = int(self.length * progressState // self.completeState)
        bar = self.fill * filledLength + '-' * (self.length - filledLength)
        print(f'\r{self.prefix} |{bar}| {percent}% {self.suffix}', end = self.printEnd)
        # Print New Line on Complete
        if progressState == self.completeState: 
            print()