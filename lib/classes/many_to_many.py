class NationalPark:

    # Initializers and Properties
    # ==========================

    # NationalPark __init__(self, name)

    def __init__(self, name):
        """
        Initializes a NationalPark object.

        Args:
            name (str): The name of the national park.
        """
        self.name = name  # Uses the property setter for validation
        self._visitors = [] # Initializes an empty list to store visitors
        self._trips = []   # Initializes an empty list to store trips


    # NationalPark property name

    @property
    def name(self):
        """
        Getter for the name property.

        Returns:
            str: The name of the national park.
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Setter for the name property, with validation.

        Args:
            name (str): The new name for the national park.

        Raises:
            Exception: If the name is not a string or less than 4 characters.
            Exception: If the name of the national park is being changed after creation.
        """
        if hasattr(self, "_name"): # Check if the name attribute already exists (meaning the object has been initialized)
            raise Exception("Cannot change the name of the national park") # Raise error if name is being changed
        elif isinstance(name, str) and len(name) > 3: # Check if the provided name is a string and has more than 3 characters
            self._name = name # set the name if all the conditions are met
        else:
            raise Exception("The name must be a string with more than 3 characters") # raise an error if the conditions are not met


    # Object Relationship Methods and Properties
    # ==========================================

    # NationalPark trips()
    def trips(self):
        """
        Returns a list of trips associated with this national park.

        Returns:
            list: A list of Trip objects.
        """
        return [trip for trip in Trip.all if trip.national_park == self] # List comprehension to filter the trips

    # NationalPark visitors()
    def visitors(self):
        """
        Returns a list of unique visitors who have visited this national park.

        Returns:
            list: A list of Visitor objects.
        """
        v_visited = [] # Initialize an empty list to store unique visitors
        for trip in Trip.all: # Iterate through all trips
            if trip.national_park == self: # Check if the trip is associated with this park
                if trip.visitor not in v_visited: # Check if the visitor has already been added to the list
                    v_visited.append(trip.visitor) # Add the visitor to the list if they are not already there
        return v_visited # Return the list of unique visitors

    # Aggregate and Association Methods
    # ==================================

    # NationalPark total_visits()
    def total_visits(self):
        """
        Returns the total number of visits to this national park.

        Returns:
            int: The total number of visits.
        """
        total_visit = {} # Initialize an empty dictionary to store visit counts
        for trip in Trip.all: # Iterate through all trips
            if trip.national_park == self: # Check if the trip is associated with this park
                if self not in total_visit: # Check if the park has already been added to the dictionary
                    total_visit[self] = 1 # Initialize the visit count to 1
                else:
                    total_visit[self] += 1 # Increment the visit count
        return total_visit[self] # Return the total visit count


    # NationalPark best_visitor()
    def best_visitor(self):
        """
        Returns the visitor who has visited this national park the most.

        Returns:
            Visitor: The Visitor object who has visited the most.
        """
        best_visitor = {} # Initialize an empty dictionary to store visitor visit counts
        for trip in Trip.all: # Iterate through all trips
            if trip.national_park == self: # Check if the trip is associated with this park
                if trip.visitor not in best_visitor: # Check if the visitor has already been added to the dictionary
                    best_visitor[trip.visitor] = 1 # Initialize the visit count to 1
                else:
                    best_visitor[trip.visitor] += 1 # Increment the visit count

        return max(best_visitor, key=best_visitor.get) # Return the visitor with the maximum visit count


    # NationalPark classmethod most_visited()
    @classmethod
    def most_visited(cls):
        """
        Returns the national park that has been visited the most.

        Returns:
            NationalPark: The most visited NationalPark object.
        """
        most_visited = {} # Initialize an empty dictionary to store park visit counts
        for trip in Trip.all: # Iterate through all trips
            if trip.national_park not in most_visited: # Check if the park has already been added to the dictionary
                most_visited[trip.national_park] = 1 # Initialize the visit count to 1
            else:
                most_visited[trip.national_park] += 1 # Increment the visit count

        return max(most_visited, key=most_visited.get) # Return the park with the maximum visit count

    # The __repr__() method in your NationalPark class 
    # ensures that when you print a NationalPark object, you see its name
    def __repr__(self):
        """
        Returns a string representation of the NationalPark object.

        Returns:
            str: The name of the national park.
        """
        return f"{self.name}"


class Visitor:

    # Initializers and Properties
    # ==========================

    # Visitor __init__(self, name) 

    def __init__(self, name):
        """
        Initializes a Visitor object.

        Args:
            name (str): The name of the visitor.
        """
        self.name = name  # Uses the property setter for validation
        self._national_parks = [] # Initializes an empty list to store visited parks
        self._trips = []   # Initializes an empty list to store trips


   # Visitor property name

    @property
    def name(self):
        """
        Getter for the name property.

        Returns:
            str: The name of the visitor.
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Setter for the name property, with validation.

        Args:
            name (str): The new name for the visitor.

        Raises:
            Exception: If the name is not a string or does not meet the length criteria.
        """
        if isinstance(name, str) and 1 < len(name) < 15: # Check if the provided name is a string and meets the length criteria
            self._name = name # Set the name if the conditions are met
        else:
            raise Exception("Visitor is initialized with a name of type str") # Raise error if the conditions are not met

    # Object Relationship Methods and Properties
    # ==========================================


    # Visitor trips()
    def trips(self):
        """
        Returns a list of trips taken by this visitor.

        Returns:
            list: A list of Trip objects.
        """
        return [trip for trip in Trip.all if trip.visitor == self] # List comprehension to filter the trips


    # Visitor national_parks()
    def national_parks(self):
        """
        Returns a list of unique national parks visited by this visitor.

        Returns:
            list: A list of NationalPark objects.
        """
        p_visited = [] # Initialize an empty list to store visited parks
        for trip in Trip.all: # Iterate through all trips
            if trip.visitor == self: # Check if the trip was taken by this visitor
                if trip.national_park not in p_visited: # Check if the park has already been added to the list
                    p_visited.append(trip.national_park) # Add the park to the list if it is not already there
        return p_visited # Return the list of unique parks

    # Aggregate and Association Methods
    # ==================================

    # Visitor total_visits_at_park(park)
    def total_visits_at_park(self, park):
        """
        Returns the total number of visits this visitor has made to a specific park.

        Args:
            park (NationalPark): The NationalPark object to check visits for.

        Returns:
            int: The total number of visits to the park.
        """
        p_visited = {} # Initialize an empty dictionary to store park visit counts
        for trip in Trip.all: # Iterate through all trips
            if trip.visitor == self: # Check if the trip was taken by this visitor
                if park not in p_visited: # Check if the park has already been added to the dictionary
                    p_visited[park] = 0 # Initialize the visit count to 0
                if park == trip.national_park: # Check if the trip was to the specified park
                    p_visited[park] += 1 # Increment the visit count
        return p_visited[park] # Return the total visit count


    # The __repr__() method in your Visitor class 
    # ensures that when you print a Visitor object, you see its name
    def __repr__(self):
        """
        Returns a string representation of the Visitor object.

        Returns:
            str: The name of the visitor.
        """
        return f"{self.name}"

class Trip:


    all = []  # Class-level list to store all Trip instances

    # Initializers and Properties
    # ==========================

    # Trip __init__(self, visitor, national_park, start_date, end_date)

    def __init__(self, visitor, national_park, start_date, end_date):
        """
        Initializes a Trip object.

        Args:
            visitor (Visitor): The Visitor object associated with the trip.
            national_park (NationalPark): The NationalPark object associated with the trip.
            start_date (str): The start date of the trip (format should be validated).
            end_date (str): The end date of the trip (format should be validated).
        """
        self.visitor = visitor  # Use the property setter for validation
        self.national_park = national_park  # Use the property setter for validation
        self.start_date = start_date  # Use the property setter for validation
        self.end_date = end_date # Use the property setter for validation

        # Store all trips
        Trip.all.append(self)

        # Establish the relationships (bi-directional)
        self.national_park._visitors.append(self.visitor)
        self.national_park._trips.append(self)

        self.visitor._national_parks.append(self.national_park)
        self.visitor._trips.append(self)


    # Trip property start_date

    @property
    def start_date(self):
        """Getter for start_date."""
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Setter for start_date with validation."""
        if isinstance(start_date, str) and len(start_date) >= 7:  # Example format check
            self._start_date = start_date
        else:
            raise Exception("Trip start date must be a string (YYYY-MM-DD)")


    # Trip property end_date
    @property
    def end_date(self):
        """Getter for end_date."""
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Setter for end_date with validation."""
        if isinstance(end_date, str) and len(end_date) >= 7:  # Example format check
            self._end_date = end_date
        else:
            raise Exception("Trip end date must be a string (YYYY-MM-DD)")


    # Trip property visitor

    @property
    def visitor(self):
        """Getter for visitor."""
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        """Setter for visitor with validation."""
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception("Trip's visitor must be a Visitor object.")



    # Trip property national_park
    @property
    def national_park(self):
        """Getter for national_park."""
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        """Setter for national_park with validation."""
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception("Trip's national_park must be a NationalPark object.")

    # Object Relationship Methods and Properties
    # ==========================================
    # (None specifically for Trip, as it's the "join" class)

    # Aggregate and Association Methods
    # ==================================
    # (None specifically for Trip, as it's the "join" class)


    # The __repr__ method in your Trip class is crucial for making it easy
    #  to inspect and understand Trip objects.  It provides a clear, multi-line string
    #  representation that includes all the important information about the trip
    def __repr__(self):
        """String representation of a Trip object."""
        return f"Visitor: {self.visitor.name}\nNational Park: {self.national_park.name}\nStart Date: {self.start_date}\nEnd Date: {self.end_date}"