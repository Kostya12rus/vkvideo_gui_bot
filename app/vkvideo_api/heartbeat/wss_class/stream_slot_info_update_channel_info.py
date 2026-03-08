# region ------ AUTO GENERATED CLASS "WssStreamSlotInfoUpdateChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfoPushPubDataDataStreamCategory ------
class WssStreamSlotInfoUpdateChannelInfoPushPubDataDataStreamCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.cover_url: str = data_json.get("coverUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfoPushPubDataDataStreamCategory ------

# region ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfoPushPubDataDataStreamTitledata ------
class WssStreamSlotInfoUpdateChannelInfoPushPubDataDataStreamTitledata:
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
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfoPushPubDataDataStreamTitledata ------

# region ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfoPushPubDataDataStream ------
class WssStreamSlotInfoUpdateChannelInfoPushPubDataDataStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.category: WssStreamSlotInfoUpdateChannelInfoPushPubDataDataStreamCategory = WssStreamSlotInfoUpdateChannelInfoPushPubDataDataStreamCategory(data_json.get("category", None))
        self.da_nick: str = data_json.get("daNick", "")
        self.donation_url: str = data_json.get("donationUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.title_data: list[WssStreamSlotInfoUpdateChannelInfoPushPubDataDataStreamTitledata] = [WssStreamSlotInfoUpdateChannelInfoPushPubDataDataStreamTitledata(item) for item in data_json.get("titleData", [])]
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfoPushPubDataDataStream ------

# region ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfoPushPubDataData ------
class WssStreamSlotInfoUpdateChannelInfoPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream: WssStreamSlotInfoUpdateChannelInfoPushPubDataDataStream = WssStreamSlotInfoUpdateChannelInfoPushPubDataDataStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfoPushPubDataData ------

# region ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfoPushPubData ------
class WssStreamSlotInfoUpdateChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotInfoUpdateChannelInfoPushPubDataData = WssStreamSlotInfoUpdateChannelInfoPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfoPushPub ------
class WssStreamSlotInfoUpdateChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotInfoUpdateChannelInfoPushPubData = WssStreamSlotInfoUpdateChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfoPushPub ------

# region ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfoPush ------
class WssStreamSlotInfoUpdateChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamSlotInfoUpdateChannelInfoPushPub = WssStreamSlotInfoUpdateChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfoPush ------

# region ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfo ------
class WssStreamSlotInfoUpdateChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamSlotInfoUpdateChannelInfoPush = WssStreamSlotInfoUpdateChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssStreamSlotInfoUpdateChannelInfo" from JSON by Kostya12rus ------
