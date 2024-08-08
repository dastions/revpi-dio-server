import revpimodio2


INPUTS = 14
OUTPUTS = 14
class ModuleDIO:
    def __init__(self):
        # Initialize the RevPiModIO object with autorefresh set to True
        self.rpi = revpimodio2.RevPiModIO(autorefresh=True)

        self.outputs = [f"O_{i}" for i in range(1, OUTPUTS+1)]
    
    def get_inputs_list(self):
        """
        Retrieve the current input values (array).
        """
        inputs = self.get_inputs()
        
        return self.int_to_bits_list(inputs)
    
    def get_inputs(self):
        """
        Retrieve the current input values (int).
        """
        inputs = self.rpi.io.Input.get_intvalue()
        
        return inputs
    
    def get_outputs_list(self):
        """
        Retrieve the current output values.
        """
        results=[]
        for output in self.outputs:
            
            get_output_value = getattr(self.rpi.io, output, None)
            if callable(get_output_value):
                value = get_output_value()
                results.append(value)
            else:
                results.append('E')

        return results
    
    def set_output(self, id: str, value: bool):
        """
        Set the output value for a specific ID.
        
        Parameters:
        id (str): The identifier for the output to set.
        value (bool): The value to set the output to.
        """

        self.rpi.io[id].value = value

        return { f"{id}": value}

    def int_to_bits_list(self, value):
        # Get the binary representation of the integer, strip the '0b' prefix, and fill with leading zeros up to 8 bits
        binary_str = bin(value)[2:].zfill(INPUTS)
    
        # Convert the binary string to a list of integers (bits)
        bits = [(int(bit) == 1) for bit in binary_str]
    
        return bits
    

