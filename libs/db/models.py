class models :
      def to_dict(self):
        return {attr: getattr(self, attr) for attr in self.__dict__}


class Event(models):
    def __init__(self, id, eventTypeID, subEventTypeID, subSubEventTypeID, recieveDataID, insertDate, shotDirectionTypeID):
        self.id = id
        self.eventTypeID = eventTypeID
        self.subEventTypeID = subEventTypeID
        self.subSubEventTypeID = subSubEventTypeID
        self.recieveDataID = recieveDataID
        self.insertDate = insertDate
        self.shotDirectionTypeID = shotDirectionTypeID
  

class ReceptionType(models):
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ReceiveData(models):
    def __init__(self, id, playerID, receptionTypeID, receptionResultTypeID, insertDate):
        self.id = id
        self.playerID = playerID
        self.receptionTypeID = receptionTypeID
        self.receptionResultTypeID = receptionResultTypeID
        self.insertDate = insertDate

class Position(models):
    def __init__(self, id, positionX, positionY, positionX2, positionY2, insertDate):
        self.id = id
        self.positionX = positionX
        self.positionY = positionY
        self.positionX2 = positionX2
        self.positionY2 = positionY2
        self.insertDate = insertDate    

class playerData(models):
    def __init__(self, id, playerID, playerNumber, playerName):
        self.id = id
        self.playerID = playerID
        self.playerNumber = playerNumber
        self.playerName = playerName
        
class TeamData(models):
    def __init__(self, id, teamName, teamID):
        self.id = id
        self.teamName = teamName
        self.teamID = teamID
    
class RecptionResultType(models):
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Player(models):
    def __init__(self, id, insertDate):
        self.id = id
        self.insertDate = insertDate

class PlayerEvents(models):
    def __init__(self, id, playerID, teamID, insertDate, PositionID, eventsID, halfTimeDataID):
        self.id = id
        self.playerID = playerID
        self.teamID = teamID
        self.insertDate = insertDate
        self.PositionID = PositionID
        self.eventsID = eventsID
        self.halfTimeDataID = halfTimeDataID

class Team(models): 
    def __init__(self, id, insertDate):
        self.id = id
        self.insertDate = insertDate

class SubSubEventType(models):
    def __init__(self, id, eventName):
        self.id = id
        self.eventName = eventName

class SubEventType(models):
    def __init__(self, id, eventName):
        self.id = id
        self.eventName = eventName

class halfTimeData(models):
    def __init__(self, id, half, halfTime, insertData):
        self.id = id
        self.half = half
        self.halfTime = halfTime
        self.insertData = insertData
