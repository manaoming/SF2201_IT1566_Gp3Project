import shelve


class TravelPlan:
    def __init__(self, destination, people, start_date, duration, accommodation,):
        self.__destination = destination
        self.__people = people
        self.__start_date = start_date
        self.__duration = duration
        self.__accommodation = accommodation
        
    def get_destination(self):
        return self.__destination
    
    def get_people(self):
        return self.__people
    
    def get_start_date(self):
        return self.__start_date
    
    def get_duration(self):
        return self.__duration
    
    def get_accommodation(self):
        return self.__accommodation

    def set_destination(self, destination):
        self.__destination = destination
    
    def set_start_date(self, start_date):
        self.__start_date = start_date
    
    def set_people(self, people):
        self.__people = people

    def set_duration(self, duration):
        self.__duration = duration

    def set_accommodation(self, accommodation):
        self.__accommodation = accommodation
        

def add_plan(destination, people, start_date, duration, accommodation, userid=0):
    plans = shelve.open("plans")
    if str(userid) not in plans:
        plans[str(userid)] = []
    try:  # No, PyCharm, \/ this thing should be a list, we're good
        plans[str(userid)] += [TravelPlan(destination, people, start_date, duration, accommodation)]
        print(f"Travel plan for user {userid} to {destination} created")
        print(f"People: {people}, start date: {start_date}, duration: {duration}, accommodation: {accommodation}")
        plans.close()
    except IOError:
        print("Error accessing plans database")
        raise IOError
    pass

