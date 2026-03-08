# region ------ AUTO GENERATED CLASS "VkapiOnlineSubscriptionStreamers" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamCountSources ------
class VkapiOnlineSubscriptionStreamersDataStreamblogsStreamCountSources:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.source: str = data_json.get("source", "")
        self.viewers: int = data_json.get("viewers", 0)
        self.views: int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamCountSources ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamCount ------
class VkapiOnlineSubscriptionStreamersDataStreamblogsStreamCount:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.likes: int = data_json.get("likes", 0)
        self.sources: list[VkapiOnlineSubscriptionStreamersDataStreamblogsStreamCountSources] = [VkapiOnlineSubscriptionStreamersDataStreamblogsStreamCountSources(item) for item in data_json.get("sources", [])]
        self.viewers: int = data_json.get("viewers", 0)
        self.views: int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamCount ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamAccessrestrictionsView ------
class VkapiOnlineSubscriptionStreamersDataStreamblogsStreamAccessrestrictionsView:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.allowed: bool = data_json.get("allowed", False)
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamAccessrestrictionsView ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamAccessrestrictions ------
class VkapiOnlineSubscriptionStreamersDataStreamblogsStreamAccessrestrictions:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.view: VkapiOnlineSubscriptionStreamersDataStreamblogsStreamAccessrestrictionsView = VkapiOnlineSubscriptionStreamersDataStreamblogsStreamAccessrestrictionsView(data_json.get("view", None))
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamAccessrestrictions ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamCategory ------
class VkapiOnlineSubscriptionStreamersDataStreamblogsStreamCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.cover_url: str = data_json.get("coverUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamCategory ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamHostforstreamerOwnerStreameractivity ------
class VkapiOnlineSubscriptionStreamersDataStreamblogsStreamHostforstreamerOwnerStreameractivity:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.level: int = data_json.get("level", 0)
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamHostforstreamerOwnerStreameractivity ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamHostforstreamerOwner ------
class VkapiOnlineSubscriptionStreamersDataStreamblogsStreamHostforstreamerOwner:
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
        self.streamer_activity: VkapiOnlineSubscriptionStreamersDataStreamblogsStreamHostforstreamerOwnerStreameractivity = VkapiOnlineSubscriptionStreamersDataStreamblogsStreamHostforstreamerOwnerStreameractivity(data_json.get("streamerActivity", None))
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamHostforstreamerOwner ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamHostforstreamer ------
class VkapiOnlineSubscriptionStreamersDataStreamblogsStreamHostforstreamer:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: str = data_json.get("blogUrl", "")
        self.channel_cover_image_url: str = data_json.get("channelCoverImageUrl", "")
        self.channel_cover_type: str = data_json.get("channelCoverType", "")
        self.cover_url: str = data_json.get("coverUrl", "")
        self.has_adult_content: bool = data_json.get("hasAdultContent", False)
        self.owner: VkapiOnlineSubscriptionStreamersDataStreamblogsStreamHostforstreamerOwner = VkapiOnlineSubscriptionStreamersDataStreamblogsStreamHostforstreamerOwner(data_json.get("owner", None))
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamHostforstreamer ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamTitledata ------
class VkapiOnlineSubscriptionStreamersDataStreamblogsStreamTitledata:
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
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStreamTitledata ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStream ------
class VkapiOnlineSubscriptionStreamersDataStreamblogsStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.access_restrictions: VkapiOnlineSubscriptionStreamersDataStreamblogsStreamAccessrestrictions = VkapiOnlineSubscriptionStreamersDataStreamblogsStreamAccessrestrictions(data_json.get("accessRestrictions", None))
        self.category: VkapiOnlineSubscriptionStreamersDataStreamblogsStreamCategory = VkapiOnlineSubscriptionStreamersDataStreamblogsStreamCategory(data_json.get("category", None))
        self.count: VkapiOnlineSubscriptionStreamersDataStreamblogsStreamCount = VkapiOnlineSubscriptionStreamersDataStreamblogsStreamCount(data_json.get("count", None))
        self.created_at: int = data_json.get("createdAt", 0)
        self.da_nick: str = data_json.get("daNick", "")
        self.data: list = data_json.get("data", [])
        self.donation_url: str = data_json.get("donationUrl", "")
        self.embed_url: str = data_json.get("embedUrl", "")
        self.end_time: None = data_json.get("endTime", None)
        self.has_access: bool = data_json.get("hasAccess", False)
        self.host_for_streamer: VkapiOnlineSubscriptionStreamersDataStreamblogsStreamHostforstreamer = VkapiOnlineSubscriptionStreamersDataStreamblogsStreamHostforstreamer(data_json.get("hostForStreamer", None))
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
        self.title_data: list[VkapiOnlineSubscriptionStreamersDataStreamblogsStreamTitledata] = [VkapiOnlineSubscriptionStreamersDataStreamblogsStreamTitledata(item) for item in data_json.get("titleData", [])]
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
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsStream ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsBlogOwnerStreameractivity ------
class VkapiOnlineSubscriptionStreamersDataStreamblogsBlogOwnerStreameractivity:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.level: int = data_json.get("level", 0)
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsBlogOwnerStreameractivity ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsBlogOwner ------
class VkapiOnlineSubscriptionStreamersDataStreamblogsBlogOwner:
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
        self.streamer_activity: VkapiOnlineSubscriptionStreamersDataStreamblogsBlogOwnerStreameractivity = VkapiOnlineSubscriptionStreamersDataStreamblogsBlogOwnerStreameractivity(data_json.get("streamerActivity", None))
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsBlogOwner ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsBlog ------
class VkapiOnlineSubscriptionStreamersDataStreamblogsBlog:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: str = data_json.get("blogUrl", "")
        self.cover_url: str = data_json.get("coverUrl", "")
        self.has_adult_content: bool = data_json.get("hasAdultContent", False)
        self.owner: VkapiOnlineSubscriptionStreamersDataStreamblogsBlogOwner = VkapiOnlineSubscriptionStreamersDataStreamblogsBlogOwner(data_json.get("owner", None))
        self.title: str = data_json.get("title", "")
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogsBlog ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogs ------
class VkapiOnlineSubscriptionStreamersDataStreamblogs:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog: VkapiOnlineSubscriptionStreamersDataStreamblogsBlog = VkapiOnlineSubscriptionStreamersDataStreamblogsBlog(data_json.get("blog", None))
        self.stream: VkapiOnlineSubscriptionStreamersDataStreamblogsStream = VkapiOnlineSubscriptionStreamersDataStreamblogsStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersDataStreamblogs ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersData ------
class VkapiOnlineSubscriptionStreamersData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream_blogs: list[VkapiOnlineSubscriptionStreamersDataStreamblogs] = [VkapiOnlineSubscriptionStreamersDataStreamblogs(item) for item in data_json.get("streamBlogs", [])]
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersData ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersExtra ------
class VkapiOnlineSubscriptionStreamersExtra:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.is_last: bool = data_json.get("isLast", False)
        self.offset: None = data_json.get("offset", None)
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamersExtra ------

# region ------ AUTO GENERATED VkapiOnlineSubscriptionStreamers ------
class VkapiOnlineSubscriptionStreamers:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: VkapiOnlineSubscriptionStreamersData = VkapiOnlineSubscriptionStreamersData(data_json.get("data", None))
        self.extra: VkapiOnlineSubscriptionStreamersExtra = VkapiOnlineSubscriptionStreamersExtra(data_json.get("extra", None))
# endregion ------ AUTO GENERATED VkapiOnlineSubscriptionStreamers ------
# endregion ------ AUTO GENERATED CLASS "VkapiOnlineSubscriptionStreamers" from JSON by Kostya12rus ------
