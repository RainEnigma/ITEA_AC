from BaseInsight import BaseInsight


class GoogleInsight(BaseInsight):
    def __init__(self, actions=None, **kwargs):
        self.actions = actions
        super().__init__(**kwargs)
