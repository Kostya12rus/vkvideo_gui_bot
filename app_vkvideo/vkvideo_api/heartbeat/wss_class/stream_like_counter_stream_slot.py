# region ------ AUTO GENERATED CLASS "WssStreamLikeCounterStreamSlot" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamLikeCounterStreamSlotPushPubData ------
class WssStreamLikeCounterStreamSlotPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.counter: int = data_json.get("counter", 0)
        self.type: str = data_json.get("type", "")
        self.user_id: int = data_json.get("userId", 0)
# endregion ------ AUTO GENERATED WssStreamLikeCounterStreamSlotPushPubData ------

# region ------ AUTO GENERATED WssStreamLikeCounterStreamSlotPushPub ------
class WssStreamLikeCounterStreamSlotPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamLikeCounterStreamSlotPushPubData = WssStreamLikeCounterStreamSlotPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamLikeCounterStreamSlotPushPub ------

# region ------ AUTO GENERATED WssStreamLikeCounterStreamSlotPush ------
class WssStreamLikeCounterStreamSlotPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamLikeCounterStreamSlotPushPub = WssStreamLikeCounterStreamSlotPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamLikeCounterStreamSlotPush ------

# region ------ AUTO GENERATED WssStreamLikeCounterStreamSlot ------
class WssStreamLikeCounterStreamSlot:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamLikeCounterStreamSlotPush = WssStreamLikeCounterStreamSlotPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamLikeCounterStreamSlot ------
# endregion ------ AUTO GENERATED CLASS "WssStreamLikeCounterStreamSlot" from JSON by Kostya12rus ------
