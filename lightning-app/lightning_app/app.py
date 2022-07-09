import lightning_app as la


class LitApp(la.LightningFlow):
    def __init__(self) -> None:
        super().__init__()

    def run(self):
        pass


app = la.LightningApp(LitApp())
