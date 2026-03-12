# region ------ AUTO GENERATED CLASS "VkapiCatalogStreamers" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED VkapiCatalogStreamersDataCategoryCount ------
class VkapiCatalogStreamersDataCategoryCount:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.viewers: int = data_json.get("viewers", 0)
# endregion ------ AUTO GENERATED VkapiCatalogStreamersDataCategoryCount ------

# region ------ AUTO GENERATED VkapiCatalogStreamersDataCategory ------
class VkapiCatalogStreamersDataCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.count: VkapiCatalogStreamersDataCategoryCount = VkapiCatalogStreamersDataCategoryCount(data_json.get("count", None))
        self.cover_url: str = data_json.get("coverUrl", "")
        self.id: str = data_json.get("id", "")
        self.is_followed: bool = data_json.get("isFollowed", False)
        self.is_hidden: bool = data_json.get("isHidden", False)
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED VkapiCatalogStreamersDataCategory ------

# region ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsStreamCategory ------
class VkapiCatalogStreamersDataStreamblogsStreamCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.cover_url: str = data_json.get("coverUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsStreamCategory ------

# region ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsStreamCountSources ------
class VkapiCatalogStreamersDataStreamblogsStreamCountSources:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.source: str = data_json.get("source", "")
        self.viewers: int = data_json.get("viewers", 0)
        self.views: int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsStreamCountSources ------

# region ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsStreamCount ------
class VkapiCatalogStreamersDataStreamblogsStreamCount:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.likes: int = data_json.get("likes", 0)
        self.sources: list[VkapiCatalogStreamersDataStreamblogsStreamCountSources] = [VkapiCatalogStreamersDataStreamblogsStreamCountSources(item) for item in data_json.get("sources", [])]
        self.viewers: int = data_json.get("viewers", 0)
        self.views: int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsStreamCount ------

# region ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsStreamAccessrestrictionsView ------
class VkapiCatalogStreamersDataStreamblogsStreamAccessrestrictionsView:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.allowed: bool = data_json.get("allowed", False)
# endregion ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsStreamAccessrestrictionsView ------

# region ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsStreamAccessrestrictions ------
class VkapiCatalogStreamersDataStreamblogsStreamAccessrestrictions:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.view: VkapiCatalogStreamersDataStreamblogsStreamAccessrestrictionsView = VkapiCatalogStreamersDataStreamblogsStreamAccessrestrictionsView(data_json.get("view", None))
# endregion ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsStreamAccessrestrictions ------

# region ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsStreamTitledata ------
class VkapiCatalogStreamersDataStreamblogsStreamTitledata:
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
# endregion ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsStreamTitledata ------

# region ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsStream ------
class VkapiCatalogStreamersDataStreamblogsStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.access_restrictions: VkapiCatalogStreamersDataStreamblogsStreamAccessrestrictions = VkapiCatalogStreamersDataStreamblogsStreamAccessrestrictions(data_json.get("accessRestrictions", None))
        self.category: VkapiCatalogStreamersDataStreamblogsStreamCategory = VkapiCatalogStreamersDataStreamblogsStreamCategory(data_json.get("category", None))
        self.count: VkapiCatalogStreamersDataStreamblogsStreamCount = VkapiCatalogStreamersDataStreamblogsStreamCount(data_json.get("count", None))
        self.created_at: int = data_json.get("createdAt", 0)
        self.da_nick: str = data_json.get("daNick", "")
        self.data: list = data_json.get("data", [])
        self.donation_url: str = data_json.get("donationUrl", "")
        self.embed_url: str = data_json.get("embedUrl", "")
        self.end_time: None = data_json.get("endTime", None)
        self.has_access: bool = data_json.get("hasAccess", False)
        self.id: str = data_json.get("id", "")
        self.is_ended: bool = data_json.get("isEnded", False)
        self.is_hidden: bool = data_json.get("isHidden", False)
        self.is_infinite: bool = data_json.get("isInfinite", False)
        self.is_liked: bool = data_json.get("isLiked", False)
        self.is_online: bool = data_json.get("isOnline", False)
        self.is_playback_disabled: bool = data_json.get("isPlaybackDisabled", False)
        self.is_public: bool = data_json.get("isPublic", False)
        self.is_should_record: bool = data_json.get("isShouldRecord", False)
        self.planned_at: None = data_json.get("plannedAt", None)
        self.planned_end_at: None = data_json.get("plannedEndAt", None)
        self.preview_url: str = data_json.get("previewUrl", "")
        self.start_time: int = data_json.get("startTime", 0)
        self.title: str = data_json.get("title", "")
        self.title_data: list[VkapiCatalogStreamersDataStreamblogsStreamTitledata] = [VkapiCatalogStreamersDataStreamblogsStreamTitledata(item) for item in data_json.get("titleData", [])]
        self.ws_chat_channel: str = data_json.get("wsChatChannel", "")
        self.ws_chat_channel_private: str = data_json.get("wsChatChannelPrivate", "")
        self.ws_chat_slot_channel: str = data_json.get("wsChatSlotChannel", "")
        self.ws_chat_slot_channel_private: str = data_json.get("wsChatSlotChannelPrivate", "")
        self.ws_stream_channel: str = data_json.get("wsStreamChannel", "")
        self.ws_stream_channel_private: str = data_json.get("wsStreamChannelPrivate", "")
        self.ws_stream_slot: str = data_json.get("wsStreamSlot", "")
        self.ws_stream_slot_channel: str = data_json.get("wsStreamSlotChannel", "")
        self.ws_stream_slot_channel_private: str = data_json.get("wsStreamSlotChannelPrivate", "")
        self.ws_stream_slot_private: str = data_json.get("wsStreamSlotPrivate", "")
        self.ws_stream_viewers_channel: str = data_json.get("wsStreamViewersChannel", "")
# endregion ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsStream ------

# region ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsBlogOwnerStreameractivity ------
class VkapiCatalogStreamersDataStreamblogsBlogOwnerStreameractivity:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.level: int = data_json.get("level", 0)
# endregion ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsBlogOwnerStreameractivity ------

# region ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsBlogOwner ------
class VkapiCatalogStreamersDataStreamblogsBlogOwner:
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
        self.streamer_activity: VkapiCatalogStreamersDataStreamblogsBlogOwnerStreameractivity = VkapiCatalogStreamersDataStreamblogsBlogOwnerStreameractivity(data_json.get("streamerActivity", None))
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsBlogOwner ------

# region ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsBlog ------
class VkapiCatalogStreamersDataStreamblogsBlog:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: str = data_json.get("blogUrl", "")
        self.cover_url: str = data_json.get("coverUrl", "")
        self.has_adult_content: bool = data_json.get("hasAdultContent", False)
        self.owner: VkapiCatalogStreamersDataStreamblogsBlogOwner = VkapiCatalogStreamersDataStreamblogsBlogOwner(data_json.get("owner", None))
        self.title: str = data_json.get("title", "")
# endregion ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogsBlog ------

# region ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogs ------
class VkapiCatalogStreamersDataStreamblogs:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog: VkapiCatalogStreamersDataStreamblogsBlog = VkapiCatalogStreamersDataStreamblogsBlog(data_json.get("blog", None))
        self.stream: VkapiCatalogStreamersDataStreamblogsStream = VkapiCatalogStreamersDataStreamblogsStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED VkapiCatalogStreamersDataStreamblogs ------

# region ------ AUTO GENERATED VkapiCatalogStreamersData ------
class VkapiCatalogStreamersData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.category: VkapiCatalogStreamersDataCategory = VkapiCatalogStreamersDataCategory(data_json.get("category", None))
        self.stream_blogs: list[VkapiCatalogStreamersDataStreamblogs] = [VkapiCatalogStreamersDataStreamblogs(item) for item in data_json.get("streamBlogs", [])]
# endregion ------ AUTO GENERATED VkapiCatalogStreamersData ------

# region ------ AUTO GENERATED VkapiCatalogStreamersExtra ------
class VkapiCatalogStreamersExtra:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.is_last: bool = data_json.get("isLast", False)
        self.offset: int = data_json.get("offset", 0)
# endregion ------ AUTO GENERATED VkapiCatalogStreamersExtra ------

# region ------ AUTO GENERATED VkapiCatalogStreamers ------
class VkapiCatalogStreamers:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: VkapiCatalogStreamersData = VkapiCatalogStreamersData(data_json.get("data", None))
        self.extra: VkapiCatalogStreamersExtra = VkapiCatalogStreamersExtra(data_json.get("extra", None))
# endregion ------ AUTO GENERATED VkapiCatalogStreamers ------
# endregion ------ AUTO GENERATED CLASS "VkapiCatalogStreamers" from JSON by Kostya12rus ------
