# region ------ AUTO GENERATED CLASS "WssStreamSlotStartStreamSlot" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamSlotStartStreamSlotPushPubDataDataStream ------
class WssStreamSlotStartStreamSlotPushPubDataDataStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.is_hosting: bool = data_json.get("isHosting", False)
        self.video_id: int = data_json.get("videoId", 0)
# endregion ------ AUTO GENERATED WssStreamSlotStartStreamSlotPushPubDataDataStream ------

# region ------ AUTO GENERATED WssStreamSlotStartStreamSlotPushPubDataData ------
class WssStreamSlotStartStreamSlotPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream: WssStreamSlotStartStreamSlotPushPubDataDataStream = WssStreamSlotStartStreamSlotPushPubDataDataStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED WssStreamSlotStartStreamSlotPushPubDataData ------

# region ------ AUTO GENERATED WssStreamSlotStartStreamSlotPushPubData ------
class WssStreamSlotStartStreamSlotPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotStartStreamSlotPushPubDataData = WssStreamSlotStartStreamSlotPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotStartStreamSlotPushPubData ------

# region ------ AUTO GENERATED WssStreamSlotStartStreamSlotPushPub ------
class WssStreamSlotStartStreamSlotPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotStartStreamSlotPushPubData = WssStreamSlotStartStreamSlotPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamSlotStartStreamSlotPushPub ------

# region ------ AUTO GENERATED WssStreamSlotStartStreamSlotPush ------
class WssStreamSlotStartStreamSlotPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamSlotStartStreamSlotPushPub = WssStreamSlotStartStreamSlotPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamSlotStartStreamSlotPush ------

# region ------ AUTO GENERATED WssStreamSlotStartStreamSlot ------
class WssStreamSlotStartStreamSlot:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamSlotStartStreamSlotPush = WssStreamSlotStartStreamSlotPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamSlotStartStreamSlot ------
# endregion ------ AUTO GENERATED CLASS "WssStreamSlotStartStreamSlot" from JSON by Kostya12rus ------
