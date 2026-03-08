# region ------ AUTO GENERATED CLASS "WssStreamSlotInfoUpdateStreamSlot" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlotPushPubDataDataStreamCategory ------
class WssStreamSlotInfoUpdateStreamSlotPushPubDataDataStreamCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.cover_url: str = data_json.get("coverUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlotPushPubDataDataStreamCategory ------

# region ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlotPushPubDataDataStreamTitledata ------
class WssStreamSlotInfoUpdateStreamSlotPushPubDataDataStreamTitledata:
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
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlotPushPubDataDataStreamTitledata ------

# region ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlotPushPubDataDataStream ------
class WssStreamSlotInfoUpdateStreamSlotPushPubDataDataStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.category: WssStreamSlotInfoUpdateStreamSlotPushPubDataDataStreamCategory = WssStreamSlotInfoUpdateStreamSlotPushPubDataDataStreamCategory(data_json.get("category", None))
        self.da_nick: str = data_json.get("daNick", "")
        self.donation_url: str = data_json.get("donationUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.title_data: list[WssStreamSlotInfoUpdateStreamSlotPushPubDataDataStreamTitledata] = [WssStreamSlotInfoUpdateStreamSlotPushPubDataDataStreamTitledata(item) for item in data_json.get("titleData", [])]
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlotPushPubDataDataStream ------

# region ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlotPushPubDataData ------
class WssStreamSlotInfoUpdateStreamSlotPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream: WssStreamSlotInfoUpdateStreamSlotPushPubDataDataStream = WssStreamSlotInfoUpdateStreamSlotPushPubDataDataStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlotPushPubDataData ------

# region ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlotPushPubData ------
class WssStreamSlotInfoUpdateStreamSlotPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotInfoUpdateStreamSlotPushPubDataData = WssStreamSlotInfoUpdateStreamSlotPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlotPushPubData ------

# region ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlotPushPub ------
class WssStreamSlotInfoUpdateStreamSlotPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotInfoUpdateStreamSlotPushPubData = WssStreamSlotInfoUpdateStreamSlotPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlotPushPub ------

# region ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlotPush ------
class WssStreamSlotInfoUpdateStreamSlotPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamSlotInfoUpdateStreamSlotPushPub = WssStreamSlotInfoUpdateStreamSlotPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlotPush ------

# region ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlot ------
class WssStreamSlotInfoUpdateStreamSlot:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamSlotInfoUpdateStreamSlotPush = WssStreamSlotInfoUpdateStreamSlotPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamSlotInfoUpdateStreamSlot ------
# endregion ------ AUTO GENERATED CLASS "WssStreamSlotInfoUpdateStreamSlot" from JSON by Kostya12rus ------
