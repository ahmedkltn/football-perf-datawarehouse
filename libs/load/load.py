from loguru import logger
from ..db import utils




def loadData(conn, allData) :
    for data in allData:
        id_player_data = utils.insertid = _into_db(conn=conn, data.player_data)
        
