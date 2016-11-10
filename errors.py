class SingularMatrixError(RuntimeError):
    def __init__(self,**kwargs):
        self.args = kwargs