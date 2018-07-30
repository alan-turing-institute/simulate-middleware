"""
This module has helper classes and methods to deal
with fields and their validation
"""


class Field(object):
    """
    A class to represents fields in cases
    and do logical processing and validation
    with them
    """

    def __init__(self, name, properties={}):
        """
        Initialise a field
        """
        self.display_name = name
        self.process_name = name
        self.properties = properties
        self._validate()

    def set_properties(self, **properties):
        """
        Set a given set of properties
        """
        self.properties.update(properties)
        self._validate()

    def _validate(self):
        """
        Ensure that the internal state is valid
        """
        self.process_name = self.display_name
        label = self.properties.get('label')
        if label is not None:
            self.process_name = label
        prefix = self.properties.get('prefix')
        suffix = self.properties.get('suffix')
        if prefix is not None:
            self.process_name = prefix + self.process_name
        if suffix is not None:
            self.process_name = self.process_name + suffix

    def validate_value(self, fullname, new_value):
        """
        Check to make sure the current value is allowed.

        The current implementation only handles floats
        and the fields
        * min
        * max
        """
        widget = self.properties.get('type')
        widget = 'slider' if not widget else widget
        if widget == 'slider':
            return self._validate_float(fullname, new_value)
        elif widget == 'file':
            # This needs to be changed to something sensible
            return True
        else:
            print('Unknown widget type {}'.format(widget))
            return False

    def _validate_float(self, fullname, new_value):
        """
        Check to make sure the current floating point value is allowed.

        The current implementation only handles the fields
            * min
            * max
            * step
        """
        try:
            new_value = float(new_value)
        except ValueError:
            return False
        if fullname != self.process_name:
            return False
        min_value = self.properties.get('min')
        if min_value is not None and float(min_value) > new_value:
            return False
        max_value = self.properties.get('max')
        if max_value is not None and float(max_value) < new_value:
            return False
        step_value = self.properties.get('step')
        if step_value is not None and new_value % float(step_value):
            return False
        return True
