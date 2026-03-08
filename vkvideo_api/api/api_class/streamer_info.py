# region ------ AUTO GENERATED CLASS "VkapiStreamerInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED VkapiStreamerInfoOwnerStreameractivity ------
class VkapiStreamerInfoOwnerStreameractivity:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.level: int = data_json.get("level", 0)
# endregion ------ AUTO GENERATED VkapiStreamerInfoOwnerStreameractivity ------

# region ------ AUTO GENERATED VkapiStreamerInfoOwner ------
class VkapiStreamerInfoOwner:
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
        self.streamer_activity: VkapiStreamerInfoOwnerStreameractivity = VkapiStreamerInfoOwnerStreameractivity(data_json.get("streamerActivity", None))
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED VkapiStreamerInfoOwner ------

# region ------ AUTO GENERATED VkapiStreamerInfoCount ------
class VkapiStreamerInfoCount:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.posts: int = data_json.get("posts", 0)
        self.subscribers: int = data_json.get("subscribers", 0)
# endregion ------ AUTO GENERATED VkapiStreamerInfoCount ------

# region ------ AUTO GENERATED VkapiStreamerInfoAccessrights ------
class VkapiStreamerInfoAccessrights:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.can_create: bool = data_json.get("canCreate", False)
        self.can_create_comments: bool = data_json.get("canCreateComments", False)
        self.can_delete_comments: bool = data_json.get("canDeleteComments", False)
        self.can_edit: bool = data_json.get("canEdit", False)
        self.can_set_payout: bool = data_json.get("canSetPayout", False)
        self.can_view: bool = data_json.get("canView", False)
# endregion ------ AUTO GENERATED VkapiStreamerInfoAccessrights ------

# region ------ AUTO GENERATED VkapiStreamerInfoFlags ------
class VkapiStreamerInfoFlags:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.has_subscription_levels: bool = data_json.get("hasSubscriptionLevels", False)
# endregion ------ AUTO GENERATED VkapiStreamerInfoFlags ------

# region ------ AUTO GENERATED VkapiStreamerInfoSubscription ------
class VkapiStreamerInfoSubscription:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.custom_price: int = data_json.get("customPrice", 0)
        self.level_id: int = data_json.get("levelId", 0)
        self.off_time: None = data_json.get("offTime", None)
        self.on_time: int = data_json.get("onTime", 0)
        self.period: int = data_json.get("period", 0)
# endregion ------ AUTO GENERATED VkapiStreamerInfoSubscription ------

# region ------ AUTO GENERATED VkapiStreamerInfo ------
class VkapiStreamerInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.access_rights: VkapiStreamerInfoAccessrights = VkapiStreamerInfoAccessrights(data_json.get("accessRights", None))
        self.blog_url: str = data_json.get("blogUrl", "")
        self.channel_cover_image_url: str = data_json.get("channelCoverImageUrl", "")
        self.channel_cover_type: str = data_json.get("channelCoverType", "")
        self.count: VkapiStreamerInfoCount = VkapiStreamerInfoCount(data_json.get("count", None))
        self.cover_url: str = data_json.get("coverUrl", "")
        self.description: str = data_json.get("description", "")
        self.flags: VkapiStreamerInfoFlags = VkapiStreamerInfoFlags(data_json.get("flags", None))
        self.has_adult_content: bool = data_json.get("hasAdultContent", False)
        self.has_chat: bool = data_json.get("hasChat", False)
        self.is_black_listed: bool = data_json.get("isBlackListed", False)
        self.is_black_listed_by_user: bool = data_json.get("isBlackListedByUser", False)
        self.is_clip_creation_allowed: bool = data_json.get("isClipCreationAllowed", False)
        self.is_owner: bool = data_json.get("isOwner", False)
        self.is_read_only: bool = data_json.get("isReadOnly", False)
        self.is_subscribed: bool = data_json.get("isSubscribed", False)
        self.is_total_baned: bool = data_json.get("isTotalBaned", False)
        self.notify_subscription: bool = data_json.get("notifySubscription", False)
        self.owner: VkapiStreamerInfoOwner = VkapiStreamerInfoOwner(data_json.get("owner", None))
        self.public_web_socket_channel: str = data_json.get("publicWebSocketChannel", "")
        self.signed_query: str = data_json.get("signedQuery", "")
        self.social_links: list = data_json.get("socialLinks", [])
        self.subscription: VkapiStreamerInfoSubscription = VkapiStreamerInfoSubscription(data_json.get("subscription", None))
        self.subscription_kind: str = data_json.get("subscriptionKind", "")
        self.title: str = data_json.get("title", "")
# endregion ------ AUTO GENERATED VkapiStreamerInfo ------
# endregion ------ AUTO GENERATED CLASS "VkapiStreamerInfo" from JSON by Kostya12rus ------
