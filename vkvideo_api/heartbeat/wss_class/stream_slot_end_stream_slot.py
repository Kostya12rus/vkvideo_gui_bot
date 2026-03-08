# region ------ AUTO GENERATED CLASS "WssStreamSlotEndStreamSlot" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamSlotEndStreamSlotPushPubDataDataStream ------
class WssStreamSlotEndStreamSlotPushPubDataDataStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.video_id: int = data_json.get("videoId", 0)
# endregion ------ AUTO GENERATED WssStreamSlotEndStreamSlotPushPubDataDataStream ------

# region ------ AUTO GENERATED WssStreamSlotEndStreamSlotPushPubDataData ------
class WssStreamSlotEndStreamSlotPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream: WssStreamSlotEndStreamSlotPushPubDataDataStream = WssStreamSlotEndStreamSlotPushPubDataDataStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED WssStreamSlotEndStreamSlotPushPubDataData ------

# region ------ AUTO GENERATED WssStreamSlotEndStreamSlotPushPubData ------
class WssStreamSlotEndStreamSlotPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotEndStreamSlotPushPubDataData = WssStreamSlotEndStreamSlotPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotEndStreamSlotPushPubData ------

# region ------ AUTO GENERATED WssStreamSlotEndStreamSlotPushPub ------
class WssStreamSlotEndStreamSlotPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotEndStreamSlotPushPubData = WssStreamSlotEndStreamSlotPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamSlotEndStreamSlotPushPub ------

# region ------ AUTO GENERATED WssStreamSlotEndStreamSlotPush ------
class WssStreamSlotEndStreamSlotPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamSlotEndStreamSlotPushPub = WssStreamSlotEndStreamSlotPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamSlotEndStreamSlotPush ------

# region ------ AUTO GENERATED WssStreamSlotEndStreamSlot ------
class WssStreamSlotEndStreamSlot:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamSlotEndStreamSlotPush = WssStreamSlotEndStreamSlotPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamSlotEndStreamSlot ------
# endregion ------ AUTO GENERATED CLASS "WssStreamSlotEndStreamSlot" from JSON by Kostya12rus ------
