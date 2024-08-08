import revpimodio2
from app.logger import log

class ModuleDIO:
    def __init__(self):
        # Initialize the RevPiModIO object with autorefresh set to True
        self.rpi = "revpimodio2.RevPiModIO(autorefresh=True)"
    
    def get_inputs(self):
        """
        Retrieve the current input values.
        """
        return self.rpi.io.get_input_values()
    
    def get_outputs(self):
        """
        Retrieve the current output values.
        """
        return self.rpi.io.get_output_values()
    
    def set_output(self, id: str, value: bool):
        """
        Set the output value for a specific ID.
        
        Parameters:
        id (str): The identifier for the output to set.
        value (bool): The value to set the output to.
        """
        self.rpi.io[id].value = value

        return True

# Example usage
# module = ModuleDIO()
# inputs = module.get_inputs()
# outputs = module.get_outputs()
# module.set_output('O_1', 1)

