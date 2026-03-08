# region ------ AUTO GENERATED CLASS "WssStreamInfoUpdateStreamSlot" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamInfoUpdateStreamSlotPushPubDataDataStreamCategory ------
class WssStreamInfoUpdateStreamSlotPushPubDataDataStreamCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.cover_url: str = data_json.get("coverUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamInfoUpdateStreamSlotPushPubDataDataStreamCategory ------

# region ------ AUTO GENERATED WssStreamInfoUpdateStreamSlotPushPubDataDataStreamTitledata ------
class WssStreamInfoUpdateStreamSlotPushPubDataDataStreamTitledata:
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
# endregion ------ AUTO GENERATED WssStreamInfoUpdateStreamSlotPushPubDataDataStreamTitledata ------

# region ------ AUTO GENERATED WssStreamInfoUpdateStreamSlotPushPubDataDataStream ------
class WssStreamInfoUpdateStreamSlotPushPubDataDataStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.category: WssStreamInfoUpdateStreamSlotPushPubDataDataStreamCategory = WssStreamInfoUpdateStreamSlotPushPubDataDataStreamCategory(data_json.get("category", None))
        self.da_nick: str = data_json.get("daNick", "")
        self.donation_url: str = data_json.get("donationUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.title_data: list[WssStreamInfoUpdateStreamSlotPushPubDataDataStreamTitledata] = [WssStreamInfoUpdateStreamSlotPushPubDataDataStreamTitledata(item) for item in data_json.get("titleData", [])]
# endregion ------ AUTO GENERATED WssStreamInfoUpdateStreamSlotPushPubDataDataStream ------

# region ------ AUTO GENERATED WssStreamInfoUpdateStreamSlotPushPubDataData ------
class WssStreamInfoUpdateStreamSlotPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream: WssStreamInfoUpdateStreamSlotPushPubDataDataStream = WssStreamInfoUpdateStreamSlotPushPubDataDataStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED WssStreamInfoUpdateStreamSlotPushPubDataData ------

# region ------ AUTO GENERATED WssStreamInfoUpdateStreamSlotPushPubData ------
class WssStreamInfoUpdateStreamSlotPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamInfoUpdateStreamSlotPushPubDataData = WssStreamInfoUpdateStreamSlotPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamInfoUpdateStreamSlotPushPubData ------

# region ------ AUTO GENERATED WssStreamInfoUpdateStreamSlotPushPub ------
class WssStreamInfoUpdateStreamSlotPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamInfoUpdateStreamSlotPushPubData = WssStreamInfoUpdateStreamSlotPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamInfoUpdateStreamSlotPushPub ------

# region ------ AUTO GENERATED WssStreamInfoUpdateStreamSlotPush ------
class WssStreamInfoUpdateStreamSlotPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamInfoUpdateStreamSlotPushPub = WssStreamInfoUpdateStreamSlotPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamInfoUpdateStreamSlotPush ------

# region ------ AUTO GENERATED WssStreamInfoUpdateStreamSlot ------
class WssStreamInfoUpdateStreamSlot:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamInfoUpdateStreamSlotPush = WssStreamInfoUpdateStreamSlotPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamInfoUpdateStreamSlot ------
# endregion ------ AUTO GENERATED CLASS "WssStreamInfoUpdateStreamSlot" from JSON by Kostya12rus ------
