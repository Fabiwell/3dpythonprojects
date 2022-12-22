# Import the necessary modules
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor

# Create the main class for our program
class MyProgram(ShowBase):
    def __init__(self):
        # Initialize the ShowBase class
        ShowBase.__init__(self)

        # Load an actor model
        self.actor = Actor("models/panda-model",
                           {"walk": "models/panda-walk4"})
        self.actor.setPos(0, 0, 0)
        self.actor.loop("walk")

        # Create a scene and set it as the current scene
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

# Create an instance of our program and run it
program = MyProgram()
program.run()
