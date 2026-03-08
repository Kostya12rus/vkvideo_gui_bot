# region ------ AUTO GENERATED CLASS "WssStreamStartChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamStartChannelInfoPushPubData ------
class WssStreamStartChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.is_hosting: int = data_json.get("isHosting", 0)
        self.type: str = data_json.get("type", "")
        self.video_id: int = data_json.get("videoId", 0)
# endregion ------ AUTO GENERATED WssStreamStartChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssStreamStartChannelInfoPushPub ------
class WssStreamStartChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamStartChannelInfoPushPubData = WssStreamStartChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamStartChannelInfoPushPub ------

# region ------ AUTO GENERATED WssStreamStartChannelInfoPush ------
class WssStreamStartChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamStartChannelInfoPushPub = WssStreamStartChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamStartChannelInfoPush ------

# region ------ AUTO GENERATED WssStreamStartChannelInfo ------
class WssStreamStartChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamStartChannelInfoPush = WssStreamStartChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamStartChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssStreamStartChannelInfo" from JSON by Kostya12rus ------
