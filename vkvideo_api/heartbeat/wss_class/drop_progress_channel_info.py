# region ------ AUTO GENERATED CLASS "WssDropProgressChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssDropProgressChannelInfoPushPubDataDataDropsProgress ------
class WssDropProgressChannelInfoPushPubDataDataDropsProgress:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.current: int = data_json.get("current", 0)
        self.goal: int = data_json.get("goal", 0)
# endregion ------ AUTO GENERATED WssDropProgressChannelInfoPushPubDataDataDropsProgress ------

# region ------ AUTO GENERATED WssDropProgressChannelInfoPushPubDataDataDropsDrop ------
class WssDropProgressChannelInfoPushPubDataDataDropsDrop:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.link: str = data_json.get("link", "")
        self.name: str = data_json.get("name", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssDropProgressChannelInfoPushPubDataDataDropsDrop ------

# region ------ AUTO GENERATED WssDropProgressChannelInfoPushPubDataDataDrops ------
class WssDropProgressChannelInfoPushPubDataDataDrops:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.drop: WssDropProgressChannelInfoPushPubDataDataDropsDrop = WssDropProgressChannelInfoPushPubDataDataDropsDrop(data_json.get("drop", None))
        self.progress: WssDropProgressChannelInfoPushPubDataDataDropsProgress = WssDropProgressChannelInfoPushPubDataDataDropsProgress(data_json.get("progress", None))
# endregion ------ AUTO GENERATED WssDropProgressChannelInfoPushPubDataDataDrops ------

# region ------ AUTO GENERATED WssDropProgressChannelInfoPushPubDataData ------
class WssDropProgressChannelInfoPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.drops: list[WssDropProgressChannelInfoPushPubDataDataDrops] = [WssDropProgressChannelInfoPushPubDataDataDrops(item) for item in data_json.get("drops", [])]
# endregion ------ AUTO GENERATED WssDropProgressChannelInfoPushPubDataData ------

# region ------ AUTO GENERATED WssDropProgressChannelInfoPushPubData ------
class WssDropProgressChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssDropProgressChannelInfoPushPubDataData = WssDropProgressChannelInfoPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssDropProgressChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssDropProgressChannelInfoPushPub ------
class WssDropProgressChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssDropProgressChannelInfoPushPubData = WssDropProgressChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssDropProgressChannelInfoPushPub ------

# region ------ AUTO GENERATED WssDropProgressChannelInfoPush ------
class WssDropProgressChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssDropProgressChannelInfoPushPub = WssDropProgressChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssDropProgressChannelInfoPush ------

# region ------ AUTO GENERATED WssDropProgressChannelInfo ------
class WssDropProgressChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssDropProgressChannelInfoPush = WssDropProgressChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssDropProgressChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssDropProgressChannelInfo" from JSON by Kostya12rus ------
