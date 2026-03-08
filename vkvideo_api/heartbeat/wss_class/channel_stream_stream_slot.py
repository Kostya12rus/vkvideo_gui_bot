# region ------ AUTO GENERATED CLASS "WssChannelStreamStreamSlot" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssChannelStreamStreamSlotPushPubDataDataStreamCountSources ------
class WssChannelStreamStreamSlotPushPubDataDataStreamCountSources:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.source: str = data_json.get("source", "")
        self.viewers: int = data_json.get("viewers", 0)
        self.views: int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED WssChannelStreamStreamSlotPushPubDataDataStreamCountSources ------

# region ------ AUTO GENERATED WssChannelStreamStreamSlotPushPubDataDataStreamCount ------
class WssChannelStreamStreamSlotPushPubDataDataStreamCount:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.likes: int = data_json.get("likes", 0)
        self.sources: list[WssChannelStreamStreamSlotPushPubDataDataStreamCountSources] = [WssChannelStreamStreamSlotPushPubDataDataStreamCountSources(item) for item in data_json.get("sources", [])]
        self.viewers: int = data_json.get("viewers", 0)
        self.views: int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED WssChannelStreamStreamSlotPushPubDataDataStreamCount ------

# region ------ AUTO GENERATED WssChannelStreamStreamSlotPushPubDataDataStreamCategory ------
class WssChannelStreamStreamSlotPushPubDataDataStreamCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
# endregion ------ AUTO GENERATED WssChannelStreamStreamSlotPushPubDataDataStreamCategory ------

# region ------ AUTO GENERATED WssChannelStreamStreamSlotPushPubDataDataStreamTitledata ------
class WssChannelStreamStreamSlotPushPubDataDataStreamTitledata:
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
# endregion ------ AUTO GENERATED WssChannelStreamStreamSlotPushPubDataDataStreamTitledata ------

# region ------ AUTO GENERATED WssChannelStreamStreamSlotPushPubDataDataStream ------
class WssChannelStreamStreamSlotPushPubDataDataStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.category: WssChannelStreamStreamSlotPushPubDataDataStreamCategory = WssChannelStreamStreamSlotPushPubDataDataStreamCategory(data_json.get("category", None))
        self.count: WssChannelStreamStreamSlotPushPubDataDataStreamCount = WssChannelStreamStreamSlotPushPubDataDataStreamCount(data_json.get("count", None))
        self.has_access: bool = data_json.get("hasAccess", False)
        self.id: str = data_json.get("id", "")
        self.is_ended: bool = data_json.get("isEnded", False)
        self.is_online: bool = data_json.get("isOnline", False)
        self.planned_at: None = data_json.get("plannedAt", None)
        self.preview_url: str = data_json.get("previewUrl", "")
        self.title: str = data_json.get("title", "")
        self.title_data: list[WssChannelStreamStreamSlotPushPubDataDataStreamTitledata] = [WssChannelStreamStreamSlotPushPubDataDataStreamTitledata(item) for item in data_json.get("titleData", [])]
# endregion ------ AUTO GENERATED WssChannelStreamStreamSlotPushPubDataDataStream ------

# region ------ AUTO GENERATED WssChannelStreamStreamSlotPushPubDataData ------
class WssChannelStreamStreamSlotPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream: WssChannelStreamStreamSlotPushPubDataDataStream = WssChannelStreamStreamSlotPushPubDataDataStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED WssChannelStreamStreamSlotPushPubDataData ------

# region ------ AUTO GENERATED WssChannelStreamStreamSlotPushPubData ------
class WssChannelStreamStreamSlotPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssChannelStreamStreamSlotPushPubDataData = WssChannelStreamStreamSlotPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssChannelStreamStreamSlotPushPubData ------

# region ------ AUTO GENERATED WssChannelStreamStreamSlotPushPub ------
class WssChannelStreamStreamSlotPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssChannelStreamStreamSlotPushPubData = WssChannelStreamStreamSlotPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssChannelStreamStreamSlotPushPub ------

# region ------ AUTO GENERATED WssChannelStreamStreamSlotPush ------
class WssChannelStreamStreamSlotPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssChannelStreamStreamSlotPushPub = WssChannelStreamStreamSlotPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssChannelStreamStreamSlotPush ------

# region ------ AUTO GENERATED WssChannelStreamStreamSlot ------
class WssChannelStreamStreamSlot:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssChannelStreamStreamSlotPush = WssChannelStreamStreamSlotPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssChannelStreamStreamSlot ------
# endregion ------ AUTO GENERATED CLASS "WssChannelStreamStreamSlot" from JSON by Kostya12rus ------
