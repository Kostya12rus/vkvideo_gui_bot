# region ------ AUTO GENERATED CLASS "WssStreamEndChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamEndChannelInfoPushPubData ------
class WssStreamEndChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.type: str = data_json.get("type", "")
        self.video_id: int = data_json.get("videoId", 0)
# endregion ------ AUTO GENERATED WssStreamEndChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssStreamEndChannelInfoPushPub ------
class WssStreamEndChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamEndChannelInfoPushPubData = WssStreamEndChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamEndChannelInfoPushPub ------

# region ------ AUTO GENERATED WssStreamEndChannelInfoPush ------
class WssStreamEndChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamEndChannelInfoPushPub = WssStreamEndChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamEndChannelInfoPush ------

# region ------ AUTO GENERATED WssStreamEndChannelInfo ------
class WssStreamEndChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamEndChannelInfoPush = WssStreamEndChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamEndChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssStreamEndChannelInfo" from JSON by Kostya12rus ------
