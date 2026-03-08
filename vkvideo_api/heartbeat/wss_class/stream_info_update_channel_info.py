# region ------ AUTO GENERATED CLASS "WssStreamInfoUpdateChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamInfoUpdateChannelInfoPushPubDataDataStreamCategory ------
class WssStreamInfoUpdateChannelInfoPushPubDataDataStreamCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.cover_url: str = data_json.get("coverUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamInfoUpdateChannelInfoPushPubDataDataStreamCategory ------

# region ------ AUTO GENERATED WssStreamInfoUpdateChannelInfoPushPubDataDataStreamTitledata ------
class WssStreamInfoUpdateChannelInfoPushPubDataDataStreamTitledata:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: str = data_json.get("blogUrl", "")
        self.content: str = data_json.get("content", "")
        self.display_name: str = data_json.get("displayName", "")
        self.id: int = data_json.get("id", 0)
        self.modificator: str = data_json.get("modificator", "")
        self.name: str = data_json.get("name", "")
        self.nick: str = data_json.get("nick", "")
        self.nick_color: str = data_json.get("nickColor", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamInfoUpdateChannelInfoPushPubDataDataStreamTitledata ------

# region ------ AUTO GENERATED WssStreamInfoUpdateChannelInfoPushPubDataDataStream ------
class WssStreamInfoUpdateChannelInfoPushPubDataDataStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.category: WssStreamInfoUpdateChannelInfoPushPubDataDataStreamCategory = WssStreamInfoUpdateChannelInfoPushPubDataDataStreamCategory(data_json.get("category", None))
        self.da_nick: str = data_json.get("daNick", "")
        self.donation_url: str = data_json.get("donationUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.title_data: list[WssStreamInfoUpdateChannelInfoPushPubDataDataStreamTitledata] = [WssStreamInfoUpdateChannelInfoPushPubDataDataStreamTitledata(item) for item in data_json.get("titleData", [])]
# endregion ------ AUTO GENERATED WssStreamInfoUpdateChannelInfoPushPubDataDataStream ------

# region ------ AUTO GENERATED WssStreamInfoUpdateChannelInfoPushPubDataData ------
class WssStreamInfoUpdateChannelInfoPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream: WssStreamInfoUpdateChannelInfoPushPubDataDataStream = WssStreamInfoUpdateChannelInfoPushPubDataDataStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED WssStreamInfoUpdateChannelInfoPushPubDataData ------

# region ------ AUTO GENERATED WssStreamInfoUpdateChannelInfoPushPubData ------
class WssStreamInfoUpdateChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamInfoUpdateChannelInfoPushPubDataData = WssStreamInfoUpdateChannelInfoPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamInfoUpdateChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssStreamInfoUpdateChannelInfoPushPub ------
class WssStreamInfoUpdateChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamInfoUpdateChannelInfoPushPubData = WssStreamInfoUpdateChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamInfoUpdateChannelInfoPushPub ------

# region ------ AUTO GENERATED WssStreamInfoUpdateChannelInfoPush ------
class WssStreamInfoUpdateChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamInfoUpdateChannelInfoPushPub = WssStreamInfoUpdateChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamInfoUpdateChannelInfoPush ------

# region ------ AUTO GENERATED WssStreamInfoUpdateChannelInfo ------
class WssStreamInfoUpdateChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamInfoUpdateChannelInfoPush = WssStreamInfoUpdateChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamInfoUpdateChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssStreamInfoUpdateChannelInfo" from JSON by Kostya12rus ------
