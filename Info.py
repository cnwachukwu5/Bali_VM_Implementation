class FunctionsInfo(object):
    def __init__(self):
        self.dictionary = {}

    def add(self, functionInfo):
        function_name = functionInfo.name
        self.dictionary[function_name] = functionInfo

    def get_number_of_parameters(self, function_name):
        return self.dictionary[function_name].get_number_of_parameters()

    def get_number_of_local_variables(self, function_name):
        return self.dictionary[function_name].get_number_of_local_variables()

    def get_local_variable_location(self, function_name, name):
        return self.dictionary[function_name].get_local_variable_location(name)

    def get_parameter_location(self, function_name, name):
        return self.dictionary[function_name].get_parameter_location(name)

    def get_local_location(self, function_name, name):
        return self.dictionary[function_name].get_local_location(name)

    def get_local_variable_value(self, function_name, name):
        return self.dictionary[function_name].get_local_variable_value(name)

    def get_parameter_value(self, function_name, name):
        return self.dictionary[function_name].get_parameter_value(name)

    def get_local_value(self, function_name, name):
        return self.dictionary[function_name].get_local_value(name)

    def get_return_value_location(self, function_name):
        return self.dictionary[function_name].get_return_value_location()

    def get_return_address(self, function_name):
        return self.dictionary[function_name].get_return_address()

    def __setitem__(self, key, value):
        self.dictionary[key] = value

    def __getitem__(self, key):
        return self.dictionary[key]

class FunctionInfo(object):
    def __init__(self, name, parameters = None, local_variables = None):
        self.name = name
        self.parameters = parameters
        self.local_variables = local_variables

    def get_number_of_parameters(self):
        return len(self.parameters)

    def get_number_of_local_variables(self):
        return len(self.local_variables)

    def get_local_location(self, name):
        # check if name is a local variable
        try:
            result = self.get_local_variable_location(name)
            return result
        except Exception:
            # check if name is a parameter
            try:
                result = self.get_parameter_location(name)
                return result
            except Exception as error:
                raise Exception(error)

    def get_local_variable_location(self, name):
        if name in self.local_variables:
            index = self.local_variables.index(name) + 1
            return "bp+" + str(index)
        else:
            raise Exception("{} is not a variable of {}".format(name, self.name))

    def get_parameter_location(self, name):
        if name in self.parameters:
            index = self.parameters.index(name) # find the location
            return "bp-" + str(1 + self.get_number_of_parameters() - index)
        else:
            raise Exception("{} is not a variable of {}".format(name, self.name))

    def get_local_value(self, name):
        # check if name is a local variable
        try:
            result = self.get_local_variable_value(name)
            return result
        except Exception:
            # check if name is a parameter
            try:
                result = self.get_parameter_value(name)
                return result
            except Exception as error:
                raise Exception(error)

    def get_local_variable_value(self, name):
        res = self.get_local_variable_location(name)
        return "[" + res + "]"

    def get_parameter_value(self, name):
        res = self.get_parameter_location(name)
        return "[" + res + "]"

    def get_return_value_location(self):
        return "bp-" + str(2 + self.get_number_of_parameters())

    def get_return_address(self):
        return "bp-1"
