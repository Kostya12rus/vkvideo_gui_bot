# region ------ AUTO GENERATED CLASS "WssStreamSlotOnlineStatusStreamSlot" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamCategory ------
class WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.cover_url: str = data_json.get("coverUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamCategory ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamHostforstreamerOwnerStreameractivity ------
class WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamHostforstreamerOwnerStreameractivity:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.level: int = data_json.get("level", 0)
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamHostforstreamerOwnerStreameractivity ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamHostforstreamerOwner ------
class WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamHostforstreamerOwner:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.avatar_url: str = data_json.get("avatarUrl", "")
        self.display_name: str = data_json.get("displayName", "")
        self.has_avatar: bool = data_json.get("hasAvatar", False)
        self.id: int = data_json.get("id", 0)
        self.is_verified_streamer: bool = data_json.get("isVerifiedStreamer", False)
        self.name: str = data_json.get("name", "")
        self.nick: str = data_json.get("nick", "")
        self.nick_color: int = data_json.get("nickColor", 0)
        self.profile_links: list = data_json.get("profileLinks", [])
        self.streamer_activity: WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamHostforstreamerOwnerStreameractivity = WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamHostforstreamerOwnerStreameractivity(data_json.get("streamerActivity", None))
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamHostforstreamerOwner ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamHostforstreamer ------
class WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamHostforstreamer:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: str = data_json.get("blogUrl", "")
        self.channel_cover_image_url: str = data_json.get("channelCoverImageUrl", "")
        self.channel_cover_type: str = data_json.get("channelCoverType", "")
        self.cover_url: str = data_json.get("coverUrl", "")
        self.has_adult_content: bool = data_json.get("hasAdultContent", False)
        self.owner: WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamHostforstreamerOwner = WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamHostforstreamerOwner(data_json.get("owner", None))
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamHostforstreamer ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamSources ------
class WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamSources:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.source: str = data_json.get("source", "")
        self.viewers: int = data_json.get("viewers", 0)
        self.views: int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamSources ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStream ------
class WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.category: WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamCategory = WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamCategory(data_json.get("category", None))
        self.channel_url: str = data_json.get("channelUrl", "")
        self.host_for_streamer: WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamHostforstreamer = WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamHostforstreamer(data_json.get("hostForStreamer", None))
        self.is_online: bool = data_json.get("isOnline", False)
        self.preview_url: str = data_json.get("previewUrl", "")
        self.sources: list[WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamSources] = [WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStreamSources(item) for item in data_json.get("sources", [])]
        self.stream_id: str = data_json.get("streamId", "")
        self.title: str = data_json.get("title", "")
        self.viewers: int = data_json.get("viewers", 0)
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStream ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubDataData ------
class WssStreamSlotOnlineStatusStreamSlotPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream: WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStream = WssStreamSlotOnlineStatusStreamSlotPushPubDataDataStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubDataData ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubData ------
class WssStreamSlotOnlineStatusStreamSlotPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotOnlineStatusStreamSlotPushPubDataData = WssStreamSlotOnlineStatusStreamSlotPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPubData ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPub ------
class WssStreamSlotOnlineStatusStreamSlotPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotOnlineStatusStreamSlotPushPubData = WssStreamSlotOnlineStatusStreamSlotPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPushPub ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPush ------
class WssStreamSlotOnlineStatusStreamSlotPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamSlotOnlineStatusStreamSlotPushPub = WssStreamSlotOnlineStatusStreamSlotPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlotPush ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlot ------
class WssStreamSlotOnlineStatusStreamSlot:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamSlotOnlineStatusStreamSlotPush = WssStreamSlotOnlineStatusStreamSlotPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusStreamSlot ------
# endregion ------ AUTO GENERATED CLASS "WssStreamSlotOnlineStatusStreamSlot" from JSON by Kostya12rus ------
