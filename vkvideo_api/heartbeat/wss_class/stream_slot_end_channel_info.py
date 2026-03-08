# region ------ AUTO GENERATED CLASS "WssStreamSlotEndChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamSlotEndChannelInfoPushPubDataDataStream ------
class WssStreamSlotEndChannelInfoPushPubDataDataStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.video_id: int = data_json.get("videoId", 0)
# endregion ------ AUTO GENERATED WssStreamSlotEndChannelInfoPushPubDataDataStream ------

# region ------ AUTO GENERATED WssStreamSlotEndChannelInfoPushPubDataData ------
class WssStreamSlotEndChannelInfoPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream: WssStreamSlotEndChannelInfoPushPubDataDataStream = WssStreamSlotEndChannelInfoPushPubDataDataStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED WssStreamSlotEndChannelInfoPushPubDataData ------

# region ------ AUTO GENERATED WssStreamSlotEndChannelInfoPushPubData ------
class WssStreamSlotEndChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotEndChannelInfoPushPubDataData = WssStreamSlotEndChannelInfoPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotEndChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssStreamSlotEndChannelInfoPushPub ------
class WssStreamSlotEndChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotEndChannelInfoPushPubData = WssStreamSlotEndChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamSlotEndChannelInfoPushPub ------

# region ------ AUTO GENERATED WssStreamSlotEndChannelInfoPush ------
class WssStreamSlotEndChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamSlotEndChannelInfoPushPub = WssStreamSlotEndChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamSlotEndChannelInfoPush ------

# region ------ AUTO GENERATED WssStreamSlotEndChannelInfo ------
class WssStreamSlotEndChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamSlotEndChannelInfoPush = WssStreamSlotEndChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamSlotEndChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssStreamSlotEndChannelInfo" from JSON by Kostya12rus ------
