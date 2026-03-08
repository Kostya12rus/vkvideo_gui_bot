# region ------ AUTO GENERATED CLASS "WssStreamSlotOnlineStatusChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamCategory ------
class WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.cover_url: str = data_json.get("coverUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamCategory ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamHostforstreamerOwnerStreameractivity ------
class WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamHostforstreamerOwnerStreameractivity:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.level: int = data_json.get("level", 0)
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamHostforstreamerOwnerStreameractivity ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamHostforstreamerOwner ------
class WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamHostforstreamerOwner:
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
        self.streamer_activity: WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamHostforstreamerOwnerStreameractivity = WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamHostforstreamerOwnerStreameractivity(data_json.get("streamerActivity", None))
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamHostforstreamerOwner ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamHostforstreamer ------
class WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamHostforstreamer:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: str = data_json.get("blogUrl", "")
        self.channel_cover_image_url: str = data_json.get("channelCoverImageUrl", "")
        self.channel_cover_type: str = data_json.get("channelCoverType", "")
        self.cover_url: str = data_json.get("coverUrl", "")
        self.has_adult_content: bool = data_json.get("hasAdultContent", False)
        self.owner: WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamHostforstreamerOwner = WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamHostforstreamerOwner(data_json.get("owner", None))
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamHostforstreamer ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamSources ------
class WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamSources:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.source: str = data_json.get("source", "")
        self.viewers: int = data_json.get("viewers", 0)
        self.views: int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamSources ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStream ------
class WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.category: WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamCategory = WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamCategory(data_json.get("category", None))
        self.channel_url: str = data_json.get("channelUrl", "")
        self.host_for_streamer: WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamHostforstreamer = WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamHostforstreamer(data_json.get("hostForStreamer", None))
        self.is_online: bool = data_json.get("isOnline", False)
        self.preview_url: str = data_json.get("previewUrl", "")
        self.sources: list[WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamSources] = [WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStreamSources(item) for item in data_json.get("sources", [])]
        self.stream_id: str = data_json.get("streamId", "")
        self.title: str = data_json.get("title", "")
        self.viewers: int = data_json.get("viewers", 0)
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStream ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubDataData ------
class WssStreamSlotOnlineStatusChannelInfoPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream: WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStream = WssStreamSlotOnlineStatusChannelInfoPushPubDataDataStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubDataData ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubData ------
class WssStreamSlotOnlineStatusChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotOnlineStatusChannelInfoPushPubDataData = WssStreamSlotOnlineStatusChannelInfoPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPub ------
class WssStreamSlotOnlineStatusChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotOnlineStatusChannelInfoPushPubData = WssStreamSlotOnlineStatusChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPushPub ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPush ------
class WssStreamSlotOnlineStatusChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamSlotOnlineStatusChannelInfoPushPub = WssStreamSlotOnlineStatusChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfoPush ------

# region ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfo ------
class WssStreamSlotOnlineStatusChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamSlotOnlineStatusChannelInfoPush = WssStreamSlotOnlineStatusChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamSlotOnlineStatusChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssStreamSlotOnlineStatusChannelInfo" from JSON by Kostya12rus ------
