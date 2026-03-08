# region ------ AUTO GENERATED CLASS "WssStreamSlotLikeCounterStreamSlot" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamSlotLikeCounterStreamSlotPushPubDataDataStreamCount ------
class WssStreamSlotLikeCounterStreamSlotPushPubDataDataStreamCount:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.likes: int = data_json.get("likes", 0)
# endregion ------ AUTO GENERATED WssStreamSlotLikeCounterStreamSlotPushPubDataDataStreamCount ------

# region ------ AUTO GENERATED WssStreamSlotLikeCounterStreamSlotPushPubDataDataStream ------
class WssStreamSlotLikeCounterStreamSlotPushPubDataDataStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.count: WssStreamSlotLikeCounterStreamSlotPushPubDataDataStreamCount = WssStreamSlotLikeCounterStreamSlotPushPubDataDataStreamCount(data_json.get("count", None))
        self.video_id: int = data_json.get("videoId", 0)
# endregion ------ AUTO GENERATED WssStreamSlotLikeCounterStreamSlotPushPubDataDataStream ------

# region ------ AUTO GENERATED WssStreamSlotLikeCounterStreamSlotPushPubDataData ------
class WssStreamSlotLikeCounterStreamSlotPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream: WssStreamSlotLikeCounterStreamSlotPushPubDataDataStream = WssStreamSlotLikeCounterStreamSlotPushPubDataDataStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED WssStreamSlotLikeCounterStreamSlotPushPubDataData ------

# region ------ AUTO GENERATED WssStreamSlotLikeCounterStreamSlotPushPubData ------
class WssStreamSlotLikeCounterStreamSlotPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotLikeCounterStreamSlotPushPubDataData = WssStreamSlotLikeCounterStreamSlotPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotLikeCounterStreamSlotPushPubData ------

# region ------ AUTO GENERATED WssStreamSlotLikeCounterStreamSlotPushPub ------
class WssStreamSlotLikeCounterStreamSlotPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotLikeCounterStreamSlotPushPubData = WssStreamSlotLikeCounterStreamSlotPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamSlotLikeCounterStreamSlotPushPub ------

# region ------ AUTO GENERATED WssStreamSlotLikeCounterStreamSlotPush ------
class WssStreamSlotLikeCounterStreamSlotPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamSlotLikeCounterStreamSlotPushPub = WssStreamSlotLikeCounterStreamSlotPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamSlotLikeCounterStreamSlotPush ------

# region ------ AUTO GENERATED WssStreamSlotLikeCounterStreamSlot ------
class WssStreamSlotLikeCounterStreamSlot:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamSlotLikeCounterStreamSlotPush = WssStreamSlotLikeCounterStreamSlotPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamSlotLikeCounterStreamSlot ------
# endregion ------ AUTO GENERATED CLASS "WssStreamSlotLikeCounterStreamSlot" from JSON by Kostya12rus ------
