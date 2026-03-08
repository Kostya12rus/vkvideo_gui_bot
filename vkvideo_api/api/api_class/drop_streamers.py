# region ------ AUTO GENERATED CLASS "VkapiDropStreamers" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED VkapiDropStreamersExtra ------
class VkapiDropStreamersExtra:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.is_last: bool = data_json.get("isLast", False)
        self.offset: int = data_json.get("offset", 0)
# endregion ------ AUTO GENERATED VkapiDropStreamersExtra ------

# region ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsBlogOwnerStreameractivity ------
class VkapiDropStreamersDataStreamblogsBlogOwnerStreameractivity:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.level: int = data_json.get("level", 0)
# endregion ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsBlogOwnerStreameractivity ------

# region ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsBlogOwner ------
class VkapiDropStreamersDataStreamblogsBlogOwner:
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
        self.streamer_activity: VkapiDropStreamersDataStreamblogsBlogOwnerStreameractivity = VkapiDropStreamersDataStreamblogsBlogOwnerStreameractivity(data_json.get("streamerActivity", None))
# endregion ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsBlogOwner ------

# region ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsBlog ------
class VkapiDropStreamersDataStreamblogsBlog:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: str = data_json.get("blogUrl", "")
        self.cover_url: str = data_json.get("coverUrl", "")
        self.has_adult_content: bool = data_json.get("hasAdultContent", False)
        self.owner: VkapiDropStreamersDataStreamblogsBlogOwner = VkapiDropStreamersDataStreamblogsBlogOwner(data_json.get("owner", None))
        self.title: str = data_json.get("title", "")
# endregion ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsBlog ------

# region ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsStreamCategory ------
class VkapiDropStreamersDataStreamblogsStreamCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.cover_url: str = data_json.get("coverUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsStreamCategory ------

# region ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsStreamCountSources ------
class VkapiDropStreamersDataStreamblogsStreamCountSources:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.source: str = data_json.get("source", "")
        self.viewers: int = data_json.get("viewers", 0)
        self.views: int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsStreamCountSources ------

# region ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsStreamCount ------
class VkapiDropStreamersDataStreamblogsStreamCount:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.likes: int = data_json.get("likes", 0)
        self.sources: list[VkapiDropStreamersDataStreamblogsStreamCountSources] = [VkapiDropStreamersDataStreamblogsStreamCountSources(item) for item in data_json.get("sources", [])]
        self.viewers: int = data_json.get("viewers", 0)
        self.views: int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsStreamCount ------

# region ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsStreamAccessrestrictionsView ------
class VkapiDropStreamersDataStreamblogsStreamAccessrestrictionsView:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.allowed: bool = data_json.get("allowed", False)
# endregion ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsStreamAccessrestrictionsView ------

# region ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsStreamAccessrestrictions ------
class VkapiDropStreamersDataStreamblogsStreamAccessrestrictions:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.view: VkapiDropStreamersDataStreamblogsStreamAccessrestrictionsView = VkapiDropStreamersDataStreamblogsStreamAccessrestrictionsView(data_json.get("view", None))
# endregion ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsStreamAccessrestrictions ------

# region ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsStreamTitledata ------
class VkapiDropStreamersDataStreamblogsStreamTitledata:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.content: str = data_json.get("content", "")
        self.modificator: str = data_json.get("modificator", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsStreamTitledata ------

# region ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsStream ------
class VkapiDropStreamersDataStreamblogsStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.access_restrictions: VkapiDropStreamersDataStreamblogsStreamAccessrestrictions = VkapiDropStreamersDataStreamblogsStreamAccessrestrictions(data_json.get("accessRestrictions", None))
        self.category: VkapiDropStreamersDataStreamblogsStreamCategory = VkapiDropStreamersDataStreamblogsStreamCategory(data_json.get("category", None))
        self.count: VkapiDropStreamersDataStreamblogsStreamCount = VkapiDropStreamersDataStreamblogsStreamCount(data_json.get("count", None))
        self.created_at: int = data_json.get("createdAt", 0)
        self.da_nick: str = data_json.get("daNick", "")
        self.data: list = data_json.get("data", [])
        self.embed_url: str = data_json.get("embedUrl", "")
        self.end_time: int = data_json.get("endTime", 0)
        self.has_access: bool = data_json.get("hasAccess", False)
        self.id: str = data_json.get("id", "")
        self.in_preview_mode: bool = data_json.get("inPreviewMode", False)
        self.is_ended: bool = data_json.get("isEnded", False)
        self.is_hidden: bool = data_json.get("isHidden", False)
        self.is_infinite: bool = data_json.get("isInfinite", False)
        self.is_liked: bool = data_json.get("isLiked", False)
        self.is_online: bool = data_json.get("isOnline", False)
        self.is_playback_disabled: bool = data_json.get("isPlaybackDisabled", False)
        self.is_public: bool = data_json.get("isPublic", False)
        self.is_should_record: bool = data_json.get("isShouldRecord", False)
        self.planned_at: int = data_json.get("plannedAt", 0)
        self.preview_url: str = data_json.get("previewUrl", "")
        self.start_time: int = data_json.get("startTime", 0)
        self.title: str = data_json.get("title", "")
        self.title_data: list[VkapiDropStreamersDataStreamblogsStreamTitledata] = [VkapiDropStreamersDataStreamblogsStreamTitledata(item) for item in data_json.get("titleData", [])]
        self.use_preview_mode: bool = data_json.get("usePreviewMode", False)
        self.ws_chat_channel: str = data_json.get("wsChatChannel", "")
        self.ws_chat_channel_private: str = data_json.get("wsChatChannelPrivate", "")
        self.ws_chat_slot_channel: str = data_json.get("wsChatSlotChannel", "")
        self.ws_chat_slot_channel_private: None = data_json.get("wsChatSlotChannelPrivate", None)
        self.ws_stream_channel: str = data_json.get("wsStreamChannel", "")
        self.ws_stream_channel_private: str = data_json.get("wsStreamChannelPrivate", "")
        self.ws_stream_slot: str = data_json.get("wsStreamSlot", "")
        self.ws_stream_slot_channel: str = data_json.get("wsStreamSlotChannel", "")
        self.ws_stream_slot_channel_private: None = data_json.get("wsStreamSlotChannelPrivate", None)
        self.ws_stream_slot_private: str = data_json.get("wsStreamSlotPrivate", "")
        self.ws_stream_viewers_channel: str = data_json.get("wsStreamViewersChannel", "")
# endregion ------ AUTO GENERATED VkapiDropStreamersDataStreamblogsStream ------

# region ------ AUTO GENERATED VkapiDropStreamersDataStreamblogs ------
class VkapiDropStreamersDataStreamblogs:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog: VkapiDropStreamersDataStreamblogsBlog = VkapiDropStreamersDataStreamblogsBlog(data_json.get("blog", None))
        self.stream: VkapiDropStreamersDataStreamblogsStream = VkapiDropStreamersDataStreamblogsStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED VkapiDropStreamersDataStreamblogs ------

# region ------ AUTO GENERATED VkapiDropStreamersData ------
class VkapiDropStreamersData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream_blogs: list[VkapiDropStreamersDataStreamblogs] = [VkapiDropStreamersDataStreamblogs(item) for item in data_json.get("streamBlogs", [])]
# endregion ------ AUTO GENERATED VkapiDropStreamersData ------

# region ------ AUTO GENERATED VkapiDropStreamers ------
class VkapiDropStreamers:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: VkapiDropStreamersData = VkapiDropStreamersData(data_json.get("data", None))
        self.extra: VkapiDropStreamersExtra = VkapiDropStreamersExtra(data_json.get("extra", None))
# endregion ------ AUTO GENERATED VkapiDropStreamers ------
# endregion ------ AUTO GENERATED CLASS "VkapiDropStreamers" from JSON by Kostya12rus ------
