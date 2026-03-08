# region ------ AUTO GENERATED CLASS "WssChannelStateChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssChannelStateChannelInfoPushPubDataDataChannel ------
class WssChannelStateChannelInfoPushPubDataDataChannel:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel_url: str = data_json.get("channelUrl", "")
        self.state: str = data_json.get("state", "")
# endregion ------ AUTO GENERATED WssChannelStateChannelInfoPushPubDataDataChannel ------

# region ------ AUTO GENERATED WssChannelStateChannelInfoPushPubDataData ------
class WssChannelStateChannelInfoPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: WssChannelStateChannelInfoPushPubDataDataChannel = WssChannelStateChannelInfoPushPubDataDataChannel(data_json.get("channel", None))
# endregion ------ AUTO GENERATED WssChannelStateChannelInfoPushPubDataData ------

# region ------ AUTO GENERATED WssChannelStateChannelInfoPushPubData ------
class WssChannelStateChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssChannelStateChannelInfoPushPubDataData = WssChannelStateChannelInfoPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssChannelStateChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssChannelStateChannelInfoPushPub ------
class WssChannelStateChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssChannelStateChannelInfoPushPubData = WssChannelStateChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssChannelStateChannelInfoPushPub ------

# region ------ AUTO GENERATED WssChannelStateChannelInfoPush ------
class WssChannelStateChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssChannelStateChannelInfoPushPub = WssChannelStateChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssChannelStateChannelInfoPush ------

# region ------ AUTO GENERATED WssChannelStateChannelInfo ------
class WssChannelStateChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssChannelStateChannelInfoPush = WssChannelStateChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssChannelStateChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssChannelStateChannelInfo" from JSON by Kostya12rus ------
