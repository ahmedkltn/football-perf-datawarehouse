import pandas as pd
from ..db import models

#transforming player data
def transform_player(df : pd.DataFrame) -> models.playerData:
    player_number = df["player_number"]
    player_name = df["player_name"]
    player_data = models.playerData(playerName=player_number, player_name=player_name)
    return player_data


def transform_team(df : pd.DataFrame) -> models.TeamData:
    team_name = df["team_name"]
    team_data = models.TeamData(teamName=team_name)
    return team_data


def transform_halftimedata(df : pd.DataFrame) -> models.halfTimeData :
    half = df["half"]
    halftime = df["halftimes"]
    halftimes_data = models.halfTimeData(half, halftime)
    return halftimes_data

def transform_position(df : pd.DataFrame) -> models.Position :
    position_x = df["position_x"]
    position_y = df["position_y"]
    position_2_x = df["position_2_x"].replace("-", None)
    position_2_y = df["position_2_y"].replace("-", None)
    position = models.Position(positionX=position_x, positionY=position_y, positionX2=position_2_x, positionY2=position_2_y)
    return position

def transform_subevents(df : pd.DataFrame) -> tuple[models.SubEventType, models.SubSubEventType] :
    sub_event_name = df['subEvents']
    subsub_event_name = df['subSubEvents']
    sub_event = models.SubEventType(eventName=sub_event_name)
    subsub_event = models.SubSubEventType(eventName=subsub_event_name)
    return sub_event, subsub_event

def transform_reception(df : pd.DataFrame) -> tuple[models.RecptionResultType, models.ReceptionType] :
    reception_type_name = df["receptionType"]
    reception_result_name = df["receptionResults"]
    reception_type = models.ReceptionType(name = reception_type_name)
    reception_result = models.RecptionResultType(name = reception_result_name)
    return reception_type, reception_result


    
