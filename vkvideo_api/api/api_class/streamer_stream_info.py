# region ------ AUTO GENERATED CLASS "VkapiStreamerStreamInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamAccessrestrictionsView ------
class VkapiStreamerStreamInfoDataStreamAccessrestrictionsView:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.allowed: bool = data_json.get("allowed", False)
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamAccessrestrictionsView ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamAccessrestrictions ------
class VkapiStreamerStreamInfoDataStreamAccessrestrictions:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.view: VkapiStreamerStreamInfoDataStreamAccessrestrictionsView = VkapiStreamerStreamInfoDataStreamAccessrestrictionsView(data_json.get("view", None))
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamAccessrestrictions ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamUserStreameractivity ------
class VkapiStreamerStreamInfoDataStreamUserStreameractivity:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.level: int = data_json.get("level", 0)
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamUserStreameractivity ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamUser ------
class VkapiStreamerStreamInfoDataStreamUser:
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
        self.streamer_activity: VkapiStreamerStreamInfoDataStreamUserStreameractivity = VkapiStreamerStreamInfoDataStreamUserStreameractivity(data_json.get("streamerActivity", None))
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamUser ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamCountSources ------
class VkapiStreamerStreamInfoDataStreamCountSources:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.source: str = data_json.get("source", "")
        self.viewers: int = data_json.get("viewers", 0)
        self.views: int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamCountSources ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamCount ------
class VkapiStreamerStreamInfoDataStreamCount:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.likes: int = data_json.get("likes", 0)
        self.sources: list[VkapiStreamerStreamInfoDataStreamCountSources] = [VkapiStreamerStreamInfoDataStreamCountSources(item) for item in data_json.get("sources", [])]
        self.viewers: int = data_json.get("viewers", 0)
        self.views: int = data_json.get("views", 0)
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamCount ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamChatsettingsAccessrestrictionsView ------
class VkapiStreamerStreamInfoDataStreamChatsettingsAccessrestrictionsView:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.allowed: bool = data_json.get("allowed", False)
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamChatsettingsAccessrestrictionsView ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamChatsettingsAccessrestrictions ------
class VkapiStreamerStreamInfoDataStreamChatsettingsAccessrestrictions:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.view: VkapiStreamerStreamInfoDataStreamChatsettingsAccessrestrictionsView = VkapiStreamerStreamInfoDataStreamChatsettingsAccessrestrictionsView(data_json.get("view", None))
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamChatsettingsAccessrestrictions ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamChatsettingsMode ------
class VkapiStreamerStreamInfoDataStreamChatsettingsMode:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.is_caps_prohibited: bool = data_json.get("isCapsProhibited", False)
        self.is_links_prohibited: bool = data_json.get("isLinksProhibited", False)
        self.is_ru_en_numbers: bool = data_json.get("isRuEnNumbers", False)
        self.kind: str = data_json.get("kind", "")
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamChatsettingsMode ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamChatsettings ------
class VkapiStreamerStreamInfoDataStreamChatsettings:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.access_restrictions: VkapiStreamerStreamInfoDataStreamChatsettingsAccessrestrictions = VkapiStreamerStreamInfoDataStreamChatsettingsAccessrestrictions(data_json.get("accessRestrictions", None))
        self.allow_access: str = data_json.get("allowAccess", "")
        self.allow_access_after: int = data_json.get("allowAccessAfter", 0)
        self.allowed: bool = data_json.get("allowed", False)
        self.any_message_timeout: int = data_json.get("anyMessageTimeout", 0)
        self.blog_id: int = data_json.get("blogId", 0)
        self.channel_id: int = data_json.get("channelId", 0)
        self.mode: VkapiStreamerStreamInfoDataStreamChatsettingsMode = VkapiStreamerStreamInfoDataStreamChatsettingsMode(data_json.get("mode", None))
        self.not_restrictable: bool = data_json.get("notRestrictable", False)
        self.remaining_time: None = data_json.get("remainingTime", None)
        self.same_message_timeout: int = data_json.get("sameMessageTimeout", 0)
        self.slowmode_cooldown: int = data_json.get("slowmodeCooldown", 0)
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamChatsettings ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamCategory ------
class VkapiStreamerStreamInfoDataStreamCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.cover_url: str = data_json.get("coverUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamCategory ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamTitledata ------
class VkapiStreamerStreamInfoDataStreamTitledata:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.content: str = data_json.get("content", "")
        self.modificator: str = data_json.get("modificator", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamTitledata ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamDataSharedplayerurls ------
class VkapiStreamerStreamInfoDataStreamDataSharedplayerurls:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.type: str = data_json.get("type", "")
        self.url: str = data_json.get("url", "")
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamDataSharedplayerurls ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamDataPlayerurls ------
class VkapiStreamerStreamInfoDataStreamDataPlayerurls:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.type: str = data_json.get("type", "")
        self.url: str = data_json.get("url", "")
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamDataPlayerurls ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamData ------
class VkapiStreamerStreamInfoDataStreamData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.failover_host: str = data_json.get("failoverHost", "")
        self.player_urls: list[VkapiStreamerStreamInfoDataStreamDataPlayerurls] = [VkapiStreamerStreamInfoDataStreamDataPlayerurls(item) for item in data_json.get("playerUrls", [])]
        self.shared_player_urls: list[VkapiStreamerStreamInfoDataStreamDataSharedplayerurls] = [VkapiStreamerStreamInfoDataStreamDataSharedplayerurls(item) for item in data_json.get("sharedPlayerUrls", [])]
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
        self.vid: str = data_json.get("vid", "")
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStreamData ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoDataStream ------
class VkapiStreamerStreamInfoDataStream:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.access_restrictions: VkapiStreamerStreamInfoDataStreamAccessrestrictions = VkapiStreamerStreamInfoDataStreamAccessrestrictions(data_json.get("accessRestrictions", None))
        self.category: VkapiStreamerStreamInfoDataStreamCategory = VkapiStreamerStreamInfoDataStreamCategory(data_json.get("category", None))
        self.channel_cover_image_url: str = data_json.get("channelCoverImageUrl", "")
        self.channel_cover_type: str = data_json.get("channelCoverType", "")
        self.chat_settings: VkapiStreamerStreamInfoDataStreamChatsettings = VkapiStreamerStreamInfoDataStreamChatsettings(data_json.get("chatSettings", None))
        self.count: VkapiStreamerStreamInfoDataStreamCount = VkapiStreamerStreamInfoDataStreamCount(data_json.get("count", None))
        self.created_at: int = data_json.get("createdAt", 0)
        self.da_nick: str = data_json.get("daNick", "")
        self.data: list[VkapiStreamerStreamInfoDataStreamData] = [VkapiStreamerStreamInfoDataStreamData(item) for item in data_json.get("data", [])]
        self.donation_url: str = data_json.get("donationUrl", "")
        self.embed_url: str = data_json.get("embedUrl", "")
        self.end_time: None = data_json.get("endTime", None)
        self.has_access: bool = data_json.get("hasAccess", False)
        self.has_chat: bool = data_json.get("hasChat", False)
        self.has_chat_pinned_message: bool = data_json.get("hasChatPinnedMessage", False)
        self.id: str = data_json.get("id", "")
        self.is_black_listed_by_user: bool = data_json.get("isBlackListedByUser", False)
        self.is_channel_moderator: bool = data_json.get("isChannelModerator", False)
        self.is_chat_moderator: bool = data_json.get("isChatModerator", False)
        self.is_created: bool = data_json.get("isCreated", False)
        self.is_ended: bool = data_json.get("isEnded", False)
        self.is_hidden: bool = data_json.get("isHidden", False)
        self.is_infinite: bool = data_json.get("isInfinite", False)
        self.is_liked: bool = data_json.get("isLiked", False)
        self.is_online: bool = data_json.get("isOnline", False)
        self.is_playback_disabled: bool = data_json.get("isPlaybackDisabled", False)
        self.is_public: bool = data_json.get("isPublic", False)
        self.is_should_record: bool = data_json.get("isShouldRecord", False)
        self.is_support_program_member: bool = data_json.get("isSupportProgramMember", False)
        self.planned_at: None = data_json.get("plannedAt", None)
        self.planned_end_at: None = data_json.get("plannedEndAt", None)
        self.preview_url: str = data_json.get("previewUrl", "")
        self.start_time: int = data_json.get("startTime", 0)
        self.title: str = data_json.get("title", "")
        self.title_data: list[VkapiStreamerStreamInfoDataStreamTitledata] = [VkapiStreamerStreamInfoDataStreamTitledata(item) for item in data_json.get("titleData", [])]
        self.user: VkapiStreamerStreamInfoDataStreamUser = VkapiStreamerStreamInfoDataStreamUser(data_json.get("user", None))
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
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoDataStream ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfoData ------
class VkapiStreamerStreamInfoData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream: VkapiStreamerStreamInfoDataStream = VkapiStreamerStreamInfoDataStream(data_json.get("stream", None))
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfoData ------

# region ------ AUTO GENERATED VkapiStreamerStreamInfo ------
class VkapiStreamerStreamInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: VkapiStreamerStreamInfoData = VkapiStreamerStreamInfoData(data_json.get("data", None))
# endregion ------ AUTO GENERATED VkapiStreamerStreamInfo ------
# endregion ------ AUTO GENERATED CLASS "VkapiStreamerStreamInfo" from JSON by Kostya12rus ------
