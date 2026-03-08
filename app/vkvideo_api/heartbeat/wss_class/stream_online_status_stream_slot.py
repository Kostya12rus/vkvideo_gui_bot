# region ------ AUTO GENERATED CLASS "WssStreamOnlineStatusStreamSlot" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamOnlineStatusStreamSlotPushPubDataCategory ------
class WssStreamOnlineStatusStreamSlotPushPubDataCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.title: str = data_json.get("title", "")
# endregion ------ AUTO GENERATED WssStreamOnlineStatusStreamSlotPushPubDataCategory ------

# region ------ AUTO GENERATED WssStreamOnlineStatusStreamSlotPushPubDataHostforstreamerOwner ------
class WssStreamOnlineStatusStreamSlotPushPubDataHostforstreamerOwner:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.display_name: str = data_json.get("displayName", "")
# endregion ------ AUTO GENERATED WssStreamOnlineStatusStreamSlotPushPubDataHostforstreamerOwner ------

# region ------ AUTO GENERATED WssStreamOnlineStatusStreamSlotPushPubDataHostforstreamer ------
class WssStreamOnlineStatusStreamSlotPushPubDataHostforstreamer:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.owner: WssStreamOnlineStatusStreamSlotPushPubDataHostforstreamerOwner = WssStreamOnlineStatusStreamSlotPushPubDataHostforstreamerOwner(data_json.get("owner", None))
# endregion ------ AUTO GENERATED WssStreamOnlineStatusStreamSlotPushPubDataHostforstreamer ------

# region ------ AUTO GENERATED WssStreamOnlineStatusStreamSlotPushPubDataSources ------
class WssStreamOnlineStatusStreamSlotPushPubDataSources:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.source: str = data_json.get("source", "")
        self.viewers: str | int = data_json.get("viewers", 0)
        self.views: str | int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED WssStreamOnlineStatusStreamSlotPushPubDataSources ------

# region ------ AUTO GENERATED WssStreamOnlineStatusStreamSlotPushPubData ------
class WssStreamOnlineStatusStreamSlotPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: str = data_json.get("blogUrl", "")
        self.category: WssStreamOnlineStatusStreamSlotPushPubDataCategory = WssStreamOnlineStatusStreamSlotPushPubDataCategory(data_json.get("category", None))
        self.host_for_streamer: WssStreamOnlineStatusStreamSlotPushPubDataHostforstreamer = WssStreamOnlineStatusStreamSlotPushPubDataHostforstreamer(data_json.get("hostForStreamer", None))
        self.is_online: bool = data_json.get("isOnline", False)
        self.preview_url: str = data_json.get("previewUrl", "")
        self.sources: list[WssStreamOnlineStatusStreamSlotPushPubDataSources] = [WssStreamOnlineStatusStreamSlotPushPubDataSources(item) for item in data_json.get("sources", [])]
        self.stream_id: str = data_json.get("streamId", "")
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
        self.viewers: int = data_json.get("viewers", 0)
# endregion ------ AUTO GENERATED WssStreamOnlineStatusStreamSlotPushPubData ------

# region ------ AUTO GENERATED WssStreamOnlineStatusStreamSlotPushPub ------
class WssStreamOnlineStatusStreamSlotPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamOnlineStatusStreamSlotPushPubData = WssStreamOnlineStatusStreamSlotPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamOnlineStatusStreamSlotPushPub ------

# region ------ AUTO GENERATED WssStreamOnlineStatusStreamSlotPush ------
class WssStreamOnlineStatusStreamSlotPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamOnlineStatusStreamSlotPushPub = WssStreamOnlineStatusStreamSlotPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamOnlineStatusStreamSlotPush ------

# region ------ AUTO GENERATED WssStreamOnlineStatusStreamSlot ------
class WssStreamOnlineStatusStreamSlot:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamOnlineStatusStreamSlotPush = WssStreamOnlineStatusStreamSlotPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamOnlineStatusStreamSlot ------
# endregion ------ AUTO GENERATED CLASS "WssStreamOnlineStatusStreamSlot" from JSON by Kostya12rus ------
