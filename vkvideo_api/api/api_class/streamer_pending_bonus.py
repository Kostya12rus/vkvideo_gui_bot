# region ------ AUTO GENERATED CLASS "VkapiStreamerPendingBonus" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED VkapiStreamerPendingBonusDataBonusesBonus ------
class VkapiStreamerPendingBonusDataBonusesBonus:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel_point_amount: int = data_json.get("channelPointAmount", 0)
        self.description: str = data_json.get("description", "")
        self.name: str = data_json.get("name", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED VkapiStreamerPendingBonusDataBonusesBonus ------

# region ------ AUTO GENERATED VkapiStreamerPendingBonusDataBonuses ------
class VkapiStreamerPendingBonusDataBonuses:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.bonus: VkapiStreamerPendingBonusDataBonusesBonus = VkapiStreamerPendingBonusDataBonusesBonus(data_json.get("bonus", None))
        self.channel_point_amount: int = data_json.get("channelPointAmount", 0)
        self.description: str = data_json.get("description", "")
        self.id: str = data_json.get("id", "")
        self.name: str = data_json.get("name", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED VkapiStreamerPendingBonusDataBonuses ------

# region ------ AUTO GENERATED VkapiStreamerPendingBonusData ------
class VkapiStreamerPendingBonusData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.bonuses: list[VkapiStreamerPendingBonusDataBonuses] = [VkapiStreamerPendingBonusDataBonuses(item) for item in data_json.get("bonuses", [])]
# endregion ------ AUTO GENERATED VkapiStreamerPendingBonusData ------

# region ------ AUTO GENERATED VkapiStreamerPendingBonus ------
class VkapiStreamerPendingBonus:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: VkapiStreamerPendingBonusData = VkapiStreamerPendingBonusData(data_json.get("data", None))
# endregion ------ AUTO GENERATED VkapiStreamerPendingBonus ------
# endregion ------ AUTO GENERATED CLASS "VkapiStreamerPendingBonus" from JSON by Kostya12rus ------
