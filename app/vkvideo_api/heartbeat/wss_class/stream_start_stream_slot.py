# region ------ AUTO GENERATED CLASS "WssStreamStartStreamSlot" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamStartStreamSlotPushPubData ------
class WssStreamStartStreamSlotPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.is_hosting: int = data_json.get("isHosting", 0)
        self.type: str = data_json.get("type", "")
        self.video_id: int = data_json.get("videoId", 0)
# endregion ------ AUTO GENERATED WssStreamStartStreamSlotPushPubData ------

# region ------ AUTO GENERATED WssStreamStartStreamSlotPushPub ------
class WssStreamStartStreamSlotPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamStartStreamSlotPushPubData = WssStreamStartStreamSlotPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamStartStreamSlotPushPub ------

# region ------ AUTO GENERATED WssStreamStartStreamSlotPush ------
class WssStreamStartStreamSlotPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamStartStreamSlotPushPub = WssStreamStartStreamSlotPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamStartStreamSlotPush ------

# region ------ AUTO GENERATED WssStreamStartStreamSlot ------
class WssStreamStartStreamSlot:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamStartStreamSlotPush = WssStreamStartStreamSlotPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamStartStreamSlot ------
# endregion ------ AUTO GENERATED CLASS "WssStreamStartStreamSlot" from JSON by Kostya12rus ------
