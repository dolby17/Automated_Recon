class Phase3Module:
    def __init__(self, target, config):
        self.target = target
        self.config = config

    def run(self):
        raise NotImplementedError("run() must be implemented")

    def results(self):
        raise NotImplementedError("results() must be implemented")
