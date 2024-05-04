from loguru import logger
import pandas as pd
from ..db import models
from .transform_to_models import *


def transform_df_into_models(df : pd.DataFrame):
    # transfrom players
    allData = list()
    for row in df :
        playerData = transform_player(row)
        playerTeam = transform_team(row)
        halftimeData = transform_halftimedata(row)
        position = transform_position(row)
        subEvents, subSubEvents = transform_subevents(row)
        recptionResultType, receptionType = transform_reception(row)
        rowData = dict(player_data = playerData, 
                       player_team = playerTeam, 
                       halftime_data = halftimeData, 
                       position = position, 
                       sub_events = subEvents,
                       subsub_events = subSubEvents,
                       reception_result_type = recptionResultType,
                       reception_type = receptionType,
                       event = models.Event(),
                       recieve_data = models.ReceiveData(),
                       player = models.Player(),
                       team = models.Team()                       
                       )
        allData.append(rowData)
    return allData

def transform_data(df : pd.DataFrame):
    return transform_df_into_models(df)