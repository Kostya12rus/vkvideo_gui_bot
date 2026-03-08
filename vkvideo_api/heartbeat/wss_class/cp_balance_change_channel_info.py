# region ------ AUTO GENERATED CLASS "WssCpBalanceChangeChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssCpBalanceChangeChannelInfoPushPubDataDataReasonBonus ------
class WssCpBalanceChangeChannelInfoPushPubDataDataReasonBonus:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel_point_amount: int = data_json.get("channelPointAmount", 0)
        self.description: str = data_json.get("description", "")
        self.name: str = data_json.get("name", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssCpBalanceChangeChannelInfoPushPubDataDataReasonBonus ------

# region ------ AUTO GENERATED WssCpBalanceChangeChannelInfoPushPubDataDataReason ------
class WssCpBalanceChangeChannelInfoPushPubDataDataReason:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.bonus: WssCpBalanceChangeChannelInfoPushPubDataDataReasonBonus = WssCpBalanceChangeChannelInfoPushPubDataDataReasonBonus(data_json.get("bonus", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssCpBalanceChangeChannelInfoPushPubDataDataReason ------

# region ------ AUTO GENERATED WssCpBalanceChangeChannelInfoPushPubDataData ------
class WssCpBalanceChangeChannelInfoPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.balance: int = data_json.get("balance", 0)
        self.delta: int = data_json.get("delta", 0)
        self.reason: WssCpBalanceChangeChannelInfoPushPubDataDataReason = WssCpBalanceChangeChannelInfoPushPubDataDataReason(data_json.get("reason", None))
# endregion ------ AUTO GENERATED WssCpBalanceChangeChannelInfoPushPubDataData ------

# region ------ AUTO GENERATED WssCpBalanceChangeChannelInfoPushPubData ------
class WssCpBalanceChangeChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssCpBalanceChangeChannelInfoPushPubDataData = WssCpBalanceChangeChannelInfoPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssCpBalanceChangeChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssCpBalanceChangeChannelInfoPushPub ------
class WssCpBalanceChangeChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssCpBalanceChangeChannelInfoPushPubData = WssCpBalanceChangeChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssCpBalanceChangeChannelInfoPushPub ------

# region ------ AUTO GENERATED WssCpBalanceChangeChannelInfoPush ------
class WssCpBalanceChangeChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssCpBalanceChangeChannelInfoPushPub = WssCpBalanceChangeChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssCpBalanceChangeChannelInfoPush ------

# region ------ AUTO GENERATED WssCpBalanceChangeChannelInfo ------
class WssCpBalanceChangeChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssCpBalanceChangeChannelInfoPush = WssCpBalanceChangeChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssCpBalanceChangeChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssCpBalanceChangeChannelInfo" from JSON by Kostya12rus ------
