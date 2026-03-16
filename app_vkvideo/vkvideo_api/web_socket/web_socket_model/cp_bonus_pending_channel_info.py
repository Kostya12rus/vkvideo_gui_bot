# region ------ AUTO GENERATED CLASS "WssCpBonusPendingChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssCpBonusPendingChannelInfoPushPubDataDataBonus ------
class WssCpBonusPendingChannelInfoPushPubDataDataBonus:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel_point_amount: int = data_json.get("channelPointAmount", 0)
        self.description: str = data_json.get("description", "")
        self.name: str = data_json.get("name", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssCpBonusPendingChannelInfoPushPubDataDataBonus ------

# region ------ AUTO GENERATED WssCpBonusPendingChannelInfoPushPubDataData ------
class WssCpBonusPendingChannelInfoPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.bonus: WssCpBonusPendingChannelInfoPushPubDataDataBonus = WssCpBonusPendingChannelInfoPushPubDataDataBonus(data_json.get("bonus", None))
        self.channel_point_amount: int = data_json.get("channelPointAmount", 0)
        self.description: str = data_json.get("description", "")
        self.id: str = data_json.get("id", "")
        self.name: str = data_json.get("name", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssCpBonusPendingChannelInfoPushPubDataData ------

# region ------ AUTO GENERATED WssCpBonusPendingChannelInfoPushPubData ------
class WssCpBonusPendingChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssCpBonusPendingChannelInfoPushPubDataData = WssCpBonusPendingChannelInfoPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssCpBonusPendingChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssCpBonusPendingChannelInfoPushPub ------
class WssCpBonusPendingChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssCpBonusPendingChannelInfoPushPubData = WssCpBonusPendingChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssCpBonusPendingChannelInfoPushPub ------

# region ------ AUTO GENERATED WssCpBonusPendingChannelInfoPush ------
class WssCpBonusPendingChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssCpBonusPendingChannelInfoPushPub = WssCpBonusPendingChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssCpBonusPendingChannelInfoPush ------

# region ------ AUTO GENERATED WssCpBonusPendingChannelInfo ------
class WssCpBonusPendingChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssCpBonusPendingChannelInfoPush = WssCpBonusPendingChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssCpBonusPendingChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssCpBonusPendingChannelInfo" from JSON by Kostya12rus ------
