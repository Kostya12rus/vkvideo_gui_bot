# region ------ AUTO GENERATED CLASS "WssStreamLikeCounterChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamLikeCounterChannelInfoPushPubData ------
class WssStreamLikeCounterChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.counter: int = data_json.get("counter", 0)
        self.type: str = data_json.get("type", "")
        self.user_id: int = data_json.get("userId", 0)
# endregion ------ AUTO GENERATED WssStreamLikeCounterChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssStreamLikeCounterChannelInfoPushPub ------
class WssStreamLikeCounterChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamLikeCounterChannelInfoPushPubData = WssStreamLikeCounterChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamLikeCounterChannelInfoPushPub ------

# region ------ AUTO GENERATED WssStreamLikeCounterChannelInfoPush ------
class WssStreamLikeCounterChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamLikeCounterChannelInfoPushPub = WssStreamLikeCounterChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamLikeCounterChannelInfoPush ------

# region ------ AUTO GENERATED WssStreamLikeCounterChannelInfo ------
class WssStreamLikeCounterChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamLikeCounterChannelInfoPush = WssStreamLikeCounterChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamLikeCounterChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssStreamLikeCounterChannelInfo" from JSON by Kostya12rus ------
