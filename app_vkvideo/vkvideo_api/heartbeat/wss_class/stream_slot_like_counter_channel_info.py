# region ------ AUTO GENERATED CLASS "WssStreamSlotLikeCounterChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamSlotLikeCounterChannelInfoPushPubDataDataStreamCount ------
class WssStreamSlotLikeCounterChannelInfoPushPubDataDataStreamCount:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.likes: int = data_json.get("likes", 0)
# endregion ------ AUTO GENERATED WssStreamSlotLikeCounterChannelInfoPushPubDataDataStreamCount ------

# region ------ AUTO GENERATED WssStreamSlotLikeCounterChannelInfoPushPubDataDataStream ------
class WssStreamSlotLikeCounterChannelInfoPushPubDataDataStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.count: WssStreamSlotLikeCounterChannelInfoPushPubDataDataStreamCount = WssStreamSlotLikeCounterChannelInfoPushPubDataDataStreamCount(data_json.get("count", None))
        self.video_id: int = data_json.get("videoId", 0)
# endregion ------ AUTO GENERATED WssStreamSlotLikeCounterChannelInfoPushPubDataDataStream ------

# region ------ AUTO GENERATED WssStreamSlotLikeCounterChannelInfoPushPubDataData ------
class WssStreamSlotLikeCounterChannelInfoPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream: WssStreamSlotLikeCounterChannelInfoPushPubDataDataStream = WssStreamSlotLikeCounterChannelInfoPushPubDataDataStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED WssStreamSlotLikeCounterChannelInfoPushPubDataData ------

# region ------ AUTO GENERATED WssStreamSlotLikeCounterChannelInfoPushPubData ------
class WssStreamSlotLikeCounterChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotLikeCounterChannelInfoPushPubDataData = WssStreamSlotLikeCounterChannelInfoPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotLikeCounterChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssStreamSlotLikeCounterChannelInfoPushPub ------
class WssStreamSlotLikeCounterChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotLikeCounterChannelInfoPushPubData = WssStreamSlotLikeCounterChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamSlotLikeCounterChannelInfoPushPub ------

# region ------ AUTO GENERATED WssStreamSlotLikeCounterChannelInfoPush ------
class WssStreamSlotLikeCounterChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamSlotLikeCounterChannelInfoPushPub = WssStreamSlotLikeCounterChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamSlotLikeCounterChannelInfoPush ------

# region ------ AUTO GENERATED WssStreamSlotLikeCounterChannelInfo ------
class WssStreamSlotLikeCounterChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamSlotLikeCounterChannelInfoPush = WssStreamSlotLikeCounterChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamSlotLikeCounterChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssStreamSlotLikeCounterChannelInfo" from JSON by Kostya12rus ------
