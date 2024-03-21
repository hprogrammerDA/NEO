"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""

from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).
    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.
    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation:str, hazardous:bool, diameter:float, name=None):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `designation`, `name`, `diameter`, and `hazardous`.
        # You should coerce these values to their appropriate data type and
        # handle any edge cases, such as a empty name being represented by `None`
        # and a missing diameter being represented by `float('nan')`.

        self.designation = str(designation) #b

        if name is None or name == '':
            self.name = None
        else:
            self.name = str(name) #b
        
        if hazardous is None or hazardous == '':
            self.hazardous = False
        elif hazardous == 'Y':
            self.hazardous = True
        else:
            self.hazardous = False
        
        if diameter is None or diameter == '':
            self.diameter = float('nan')
        else:
            self.diameter = float(diameter)

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        # TODO: Use self.designation and self.name to build a fullname for this object.
        if self.name:
            fullname = f"{self.designation} ({self.name})"
        else:
            fullname = f"{self.designation}"
        return fullname

    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        if self.hazardous is True: #== 'N':
            hazard_text = 'is'
        elif self.hazardous is False: #== 'Y':
            hazard_text = 'is not'
        else: 
            hazard_text = 'is unknown to be/not to be'
        return f"NEO {self.fullname} has a diameter of {self.diameter} km and {hazard_text} potentially hazardous"

    #def __repr__(self):
    #    """Return `repr(self)`, a computer-readable string representation of this object."""
    #    if self.name:
    #        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
    #            f"diameter={self.diameter!r}, hazardous={self.hazardous!r})" #self.diameter:.3f
    #    else:
    #        return f"NearEarthObject(designation={self.designation!r}, name=None, " \
    #            f"diameter={self.diameter!r}, hazardous={self.hazardous!r})" #self.diameter:.3f
        
    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        if self.name:
            return "NearEarthObject(designation={!r}, name={!r}, diameter={!r}, hazardous={!r})".format(
                self.designation, self.name, self.diameter, self.hazardous)
        else:
            return "NearEarthObject(designation={!r}, name=None, diameter={!r}, hazardous={!r})".format(
                self.designation, self.diameter, self.hazardous)


# Testing # 
#neo = NearEarthObject(designation = 433, name = 'One REALLY BIG fake asteroid', hazardous = False, diameter = 16.840)
#neo = NearEarthObject(designation = 433, hazardous = 'N', diameter = '')
#print(neo)


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, _designation, time, distance, velocity):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `_designation`, `time`, `distance`, and `velocity`.
        # You should coerce these values to their appropriate data type and handle any edge cases.
        # The `cd_to_datetime` function will be useful.
        self._designation = str(_designation) #b
        self.time = cd_to_datetime(time)  # TODO: Use the cd_to_datetime function for this attribute.
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        
        # TODO: Use this object's `.time` attribute and the `datetime_to_str` function to
        # build a formatted representation of the approach time.
        # TODO: Use self.designation and self.name to build a fullname for this object.
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        return f"At {self.time_str}, object with designation '{self._designation}' approaches Earth at a distance of {self.distance} au and a velocity of {self.velocity} km/s"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"

# Testing # 
#ca = CloseApproach(_designation = '2020 FK (one Really BIG fake asteroid)', time = '1900-Jan-01 00:00', distance = 0.25, velocity = 56.78)
#print(ca)
#print(ca.time_str)
#print(ca.distance)
#print(ca.velocity)




