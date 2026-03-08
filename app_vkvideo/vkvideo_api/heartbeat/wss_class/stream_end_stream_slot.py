# region ------ AUTO GENERATED CLASS "WssStreamEndStreamSlot" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamEndStreamSlotPushPubData ------
class WssStreamEndStreamSlotPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.type: str = data_json.get("type", "")
        self.video_id: int = data_json.get("videoId", 0)
# endregion ------ AUTO GENERATED WssStreamEndStreamSlotPushPubData ------

# region ------ AUTO GENERATED WssStreamEndStreamSlotPushPub ------
class WssStreamEndStreamSlotPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamEndStreamSlotPushPubData = WssStreamEndStreamSlotPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamEndStreamSlotPushPub ------

# region ------ AUTO GENERATED WssStreamEndStreamSlotPush ------
class WssStreamEndStreamSlotPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamEndStreamSlotPushPub = WssStreamEndStreamSlotPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamEndStreamSlotPush ------

# region ------ AUTO GENERATED WssStreamEndStreamSlot ------
class WssStreamEndStreamSlot:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamEndStreamSlotPush = WssStreamEndStreamSlotPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamEndStreamSlot ------
# endregion ------ AUTO GENERATED CLASS "WssStreamEndStreamSlot" from JSON by Kostya12rus ------
