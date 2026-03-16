# region ------ AUTO GENERATED CLASS "WssChannelStreamChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssChannelStreamChannelInfoPushPubDataDataStreamCountSources ------
class WssChannelStreamChannelInfoPushPubDataDataStreamCountSources:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.source: str = data_json.get("source", "")
        self.viewers: int = data_json.get("viewers", 0)
        self.views: int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED WssChannelStreamChannelInfoPushPubDataDataStreamCountSources ------

# region ------ AUTO GENERATED WssChannelStreamChannelInfoPushPubDataDataStreamCount ------
class WssChannelStreamChannelInfoPushPubDataDataStreamCount:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.likes: int = data_json.get("likes", 0)
        self.sources: list[WssChannelStreamChannelInfoPushPubDataDataStreamCountSources] = [WssChannelStreamChannelInfoPushPubDataDataStreamCountSources(item) for item in data_json.get("sources", [])]
        self.viewers: int = data_json.get("viewers", 0)
        self.views: int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED WssChannelStreamChannelInfoPushPubDataDataStreamCount ------

# region ------ AUTO GENERATED WssChannelStreamChannelInfoPushPubDataDataStreamCategory ------
class WssChannelStreamChannelInfoPushPubDataDataStreamCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
# endregion ------ AUTO GENERATED WssChannelStreamChannelInfoPushPubDataDataStreamCategory ------

# region ------ AUTO GENERATED WssChannelStreamChannelInfoPushPubDataDataStreamTitledata ------
class WssChannelStreamChannelInfoPushPubDataDataStreamTitledata:
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
# endregion ------ AUTO GENERATED WssChannelStreamChannelInfoPushPubDataDataStreamTitledata ------

# region ------ AUTO GENERATED WssChannelStreamChannelInfoPushPubDataDataStream ------
class WssChannelStreamChannelInfoPushPubDataDataStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.category: WssChannelStreamChannelInfoPushPubDataDataStreamCategory = WssChannelStreamChannelInfoPushPubDataDataStreamCategory(data_json.get("category", None))
        self.count: WssChannelStreamChannelInfoPushPubDataDataStreamCount = WssChannelStreamChannelInfoPushPubDataDataStreamCount(data_json.get("count", None))
        self.has_access: bool = data_json.get("hasAccess", False)
        self.id: str = data_json.get("id", "")
        self.is_ended: bool = data_json.get("isEnded", False)
        self.is_online: bool = data_json.get("isOnline", False)
        self.planned_at: None = data_json.get("plannedAt", None)
        self.preview_url: str = data_json.get("previewUrl", "")
        self.title: str = data_json.get("title", "")
        self.title_data: list[WssChannelStreamChannelInfoPushPubDataDataStreamTitledata] = [WssChannelStreamChannelInfoPushPubDataDataStreamTitledata(item) for item in data_json.get("titleData", [])]
# endregion ------ AUTO GENERATED WssChannelStreamChannelInfoPushPubDataDataStream ------

# region ------ AUTO GENERATED WssChannelStreamChannelInfoPushPubDataData ------
class WssChannelStreamChannelInfoPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream: WssChannelStreamChannelInfoPushPubDataDataStream = WssChannelStreamChannelInfoPushPubDataDataStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED WssChannelStreamChannelInfoPushPubDataData ------

# region ------ AUTO GENERATED WssChannelStreamChannelInfoPushPubData ------
class WssChannelStreamChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssChannelStreamChannelInfoPushPubDataData = WssChannelStreamChannelInfoPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssChannelStreamChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssChannelStreamChannelInfoPushPub ------
class WssChannelStreamChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssChannelStreamChannelInfoPushPubData = WssChannelStreamChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssChannelStreamChannelInfoPushPub ------

# region ------ AUTO GENERATED WssChannelStreamChannelInfoPush ------
class WssChannelStreamChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssChannelStreamChannelInfoPushPub = WssChannelStreamChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssChannelStreamChannelInfoPush ------

# region ------ AUTO GENERATED WssChannelStreamChannelInfo ------
class WssChannelStreamChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssChannelStreamChannelInfoPush = WssChannelStreamChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssChannelStreamChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssChannelStreamChannelInfo" from JSON by Kostya12rus ------
