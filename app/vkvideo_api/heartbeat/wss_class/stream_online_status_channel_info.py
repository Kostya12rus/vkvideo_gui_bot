# region ------ AUTO GENERATED CLASS "WssStreamOnlineStatusChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamOnlineStatusChannelInfoPushPubDataCategory ------
class WssStreamOnlineStatusChannelInfoPushPubDataCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.title: str = data_json.get("title", "")
# endregion ------ AUTO GENERATED WssStreamOnlineStatusChannelInfoPushPubDataCategory ------

# region ------ AUTO GENERATED WssStreamOnlineStatusChannelInfoPushPubDataHostforstreamerOwner ------
class WssStreamOnlineStatusChannelInfoPushPubDataHostforstreamerOwner:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.display_name: str = data_json.get("displayName", "")
# endregion ------ AUTO GENERATED WssStreamOnlineStatusChannelInfoPushPubDataHostforstreamerOwner ------

# region ------ AUTO GENERATED WssStreamOnlineStatusChannelInfoPushPubDataHostforstreamer ------
class WssStreamOnlineStatusChannelInfoPushPubDataHostforstreamer:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.owner: WssStreamOnlineStatusChannelInfoPushPubDataHostforstreamerOwner = WssStreamOnlineStatusChannelInfoPushPubDataHostforstreamerOwner(data_json.get("owner", None))
# endregion ------ AUTO GENERATED WssStreamOnlineStatusChannelInfoPushPubDataHostforstreamer ------

# region ------ AUTO GENERATED WssStreamOnlineStatusChannelInfoPushPubDataSources ------
class WssStreamOnlineStatusChannelInfoPushPubDataSources:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.source: str = data_json.get("source", "")
        self.viewers: str | int = data_json.get("viewers", 0)
        self.views: str | int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED WssStreamOnlineStatusChannelInfoPushPubDataSources ------

# region ------ AUTO GENERATED WssStreamOnlineStatusChannelInfoPushPubData ------
class WssStreamOnlineStatusChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: str = data_json.get("blogUrl", "")
        self.category: WssStreamOnlineStatusChannelInfoPushPubDataCategory = WssStreamOnlineStatusChannelInfoPushPubDataCategory(data_json.get("category", None))
        self.host_for_streamer: WssStreamOnlineStatusChannelInfoPushPubDataHostforstreamer = WssStreamOnlineStatusChannelInfoPushPubDataHostforstreamer(data_json.get("hostForStreamer", None))
        self.is_online: bool = data_json.get("isOnline", False)
        self.preview_url: str = data_json.get("previewUrl", "")
        self.sources: list[WssStreamOnlineStatusChannelInfoPushPubDataSources] = [WssStreamOnlineStatusChannelInfoPushPubDataSources(item) for item in data_json.get("sources", [])]
        self.stream_id: str = data_json.get("streamId", "")
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
        self.viewers: int = data_json.get("viewers", 0)
# endregion ------ AUTO GENERATED WssStreamOnlineStatusChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssStreamOnlineStatusChannelInfoPushPub ------
class WssStreamOnlineStatusChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamOnlineStatusChannelInfoPushPubData = WssStreamOnlineStatusChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamOnlineStatusChannelInfoPushPub ------

# region ------ AUTO GENERATED WssStreamOnlineStatusChannelInfoPush ------
class WssStreamOnlineStatusChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamOnlineStatusChannelInfoPushPub = WssStreamOnlineStatusChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamOnlineStatusChannelInfoPush ------

# region ------ AUTO GENERATED WssStreamOnlineStatusChannelInfo ------
class WssStreamOnlineStatusChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamOnlineStatusChannelInfoPush = WssStreamOnlineStatusChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamOnlineStatusChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssStreamOnlineStatusChannelInfo" from JSON by Kostya12rus ------
