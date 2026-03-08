# region ------ AUTO GENERATED CLASS "WssStreamSlotStartChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamSlotStartChannelInfoPushPubDataDataStream ------
class WssStreamSlotStartChannelInfoPushPubDataDataStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.is_hosting: bool = data_json.get("isHosting", False)
        self.video_id: int = data_json.get("videoId", 0)
# endregion ------ AUTO GENERATED WssStreamSlotStartChannelInfoPushPubDataDataStream ------

# region ------ AUTO GENERATED WssStreamSlotStartChannelInfoPushPubDataData ------
class WssStreamSlotStartChannelInfoPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream: WssStreamSlotStartChannelInfoPushPubDataDataStream = WssStreamSlotStartChannelInfoPushPubDataDataStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED WssStreamSlotStartChannelInfoPushPubDataData ------

# region ------ AUTO GENERATED WssStreamSlotStartChannelInfoPushPubData ------
class WssStreamSlotStartChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotStartChannelInfoPushPubDataData = WssStreamSlotStartChannelInfoPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotStartChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssStreamSlotStartChannelInfoPushPub ------
class WssStreamSlotStartChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotStartChannelInfoPushPubData = WssStreamSlotStartChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamSlotStartChannelInfoPushPub ------

# region ------ AUTO GENERATED WssStreamSlotStartChannelInfoPush ------
class WssStreamSlotStartChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamSlotStartChannelInfoPushPub = WssStreamSlotStartChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamSlotStartChannelInfoPush ------

# region ------ AUTO GENERATED WssStreamSlotStartChannelInfo ------
class WssStreamSlotStartChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamSlotStartChannelInfoPush = WssStreamSlotStartChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamSlotStartChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssStreamSlotStartChannelInfo" from JSON by Kostya12rus ------
