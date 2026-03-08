# region ------ AUTO GENERATED CLASS "WssMessageChannelChat" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataFlags ------
class WssMessageChannelChatPushPubDataDataFlags:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.is_first_message: bool = data_json.get("isFirstMessage", False)
        self.is_parent_deleted: bool = data_json.get("isParentDeleted", False)
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataFlags ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataAuthorStreameractivity ------
class WssMessageChannelChatPushPubDataDataAuthorStreameractivity:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.level: int = data_json.get("level", 0)
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataAuthorStreameractivity ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataAuthorRoles ------
class WssMessageChannelChatPushPubDataDataAuthorRoles:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.id: str = data_json.get("id", "")
        self.large_url: str = data_json.get("largeUrl", "")
        self.medium_url: str = data_json.get("mediumUrl", "")
        self.name: str = data_json.get("name", "")
        self.priority: int = data_json.get("priority", 0)
        self.small_url: str = data_json.get("smallUrl", "")
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataAuthorRoles ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataAuthorBadgesAchievement ------
class WssMessageChannelChatPushPubDataDataAuthorBadgesAchievement:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.name: str = data_json.get("name", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataAuthorBadgesAchievement ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataAuthorBadges ------
class WssMessageChannelChatPushPubDataDataAuthorBadges:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.achievement: WssMessageChannelChatPushPubDataDataAuthorBadgesAchievement = WssMessageChannelChatPushPubDataDataAuthorBadgesAchievement(data_json.get("achievement", None))
        self.id: str = data_json.get("id", "")
        self.is_created: bool = data_json.get("isCreated", False)
        self.large_url: str = data_json.get("largeUrl", "")
        self.medium_url: str = data_json.get("mediumUrl", "")
        self.name: str = data_json.get("name", "")
        self.small_url: str = data_json.get("smallUrl", "")
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataAuthorBadges ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataAuthor ------
class WssMessageChannelChatPushPubDataDataAuthor:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.avatar_url: str = data_json.get("avatarUrl", "")
        self.badges: list[WssMessageChannelChatPushPubDataDataAuthorBadges] = [WssMessageChannelChatPushPubDataDataAuthorBadges(item) for item in data_json.get("badges", [])]
        self.display_name: str = data_json.get("displayName", "")
        self.has_avatar: bool = data_json.get("hasAvatar", False)
        self.id: int = data_json.get("id", 0)
        self.is_channel_moderator: bool = data_json.get("isChannelModerator", False)
        self.is_chat_moderator: bool = data_json.get("isChatModerator", False)
        self.is_owner: bool = data_json.get("isOwner", False)
        self.is_verified_streamer: bool = data_json.get("isVerifiedStreamer", False)
        self.name: str = data_json.get("name", "")
        self.nick: str = data_json.get("nick", "")
        self.nick_color: int = data_json.get("nickColor", 0)
        self.profile_links: list = data_json.get("profileLinks", [])
        self.roles: list = [WssMessageChannelChatPushPubDataDataAuthorRoles(item) for item in data_json.get("roles", [])]
        self.streamer_activity: WssMessageChannelChatPushPubDataDataAuthorStreameractivity = WssMessageChannelChatPushPubDataDataAuthorStreameractivity(data_json.get("streamerActivity", None))
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataAuthor ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataUserStreameractivity ------
class WssMessageChannelChatPushPubDataDataUserStreameractivity:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.level: int = data_json.get("level", 0)
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataUserStreameractivity ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataUserBadgesAchievement ------
class WssMessageChannelChatPushPubDataDataUserBadgesAchievement:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.name: str = data_json.get("name", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataUserBadgesAchievement ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataUserBadges ------
class WssMessageChannelChatPushPubDataDataUserBadges:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.achievement: WssMessageChannelChatPushPubDataDataUserBadgesAchievement = WssMessageChannelChatPushPubDataDataUserBadgesAchievement(data_json.get("achievement", None))
        self.id: str = data_json.get("id", "")
        self.is_created: bool = data_json.get("isCreated", False)
        self.large_url: str = data_json.get("largeUrl", "")
        self.medium_url: str = data_json.get("mediumUrl", "")
        self.name: str = data_json.get("name", "")
        self.small_url: str = data_json.get("smallUrl", "")
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataUserBadges ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataUserRoles ------
class WssMessageChannelChatPushPubDataDataUserRoles:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.id: str = data_json.get("id", "")
        self.large_url: str = data_json.get("largeUrl", "")
        self.medium_url: str = data_json.get("mediumUrl", "")
        self.name: str = data_json.get("name", "")
        self.priority: int = data_json.get("priority", 0)
        self.small_url: str = data_json.get("smallUrl", "")
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataUserRoles ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataUser ------
class WssMessageChannelChatPushPubDataDataUser:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.avatar_url: str = data_json.get("avatarUrl", "")
        self.badges: list[WssMessageChannelChatPushPubDataDataUserBadges] = [WssMessageChannelChatPushPubDataDataUserBadges(item) for item in data_json.get("badges", [])]
        self.display_name: str = data_json.get("displayName", "")
        self.has_avatar: bool = data_json.get("hasAvatar", False)
        self.id: int = data_json.get("id", 0)
        self.is_channel_moderator: bool = data_json.get("isChannelModerator", False)
        self.is_chat_moderator: bool = data_json.get("isChatModerator", False)
        self.is_owner: bool = data_json.get("isOwner", False)
        self.is_verified_streamer: bool = data_json.get("isVerifiedStreamer", False)
        self.name: str = data_json.get("name", "")
        self.nick: str = data_json.get("nick", "")
        self.nick_color: int = data_json.get("nickColor", 0)
        self.profile_links: list = data_json.get("profileLinks", [])
        self.roles: list[WssMessageChannelChatPushPubDataDataUserRoles] = [WssMessageChannelChatPushPubDataDataUserRoles(item) for item in data_json.get("roles", [])]
        self.streamer_activity: WssMessageChannelChatPushPubDataDataUserStreameractivity = WssMessageChannelChatPushPubDataDataUserStreameractivity(data_json.get("streamerActivity", None))
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataUser ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataParentAuthorRoles ------
class WssMessageChannelChatPushPubDataDataParentAuthorRoles:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.id: str = data_json.get("id", "")
        self.large_url: str = data_json.get("largeUrl", "")
        self.medium_url: str = data_json.get("mediumUrl", "")
        self.name: str = data_json.get("name", "")
        self.priority: int = data_json.get("priority", 0)
        self.small_url: str = data_json.get("smallUrl", "")
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataParentAuthorRoles ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataParentAuthorBadgesAchievement ------
class WssMessageChannelChatPushPubDataDataParentAuthorBadgesAchievement:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.name: str = data_json.get("name", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataParentAuthorBadgesAchievement ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataParentAuthorBadges ------
class WssMessageChannelChatPushPubDataDataParentAuthorBadges:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.achievement: WssMessageChannelChatPushPubDataDataParentAuthorBadgesAchievement = WssMessageChannelChatPushPubDataDataParentAuthorBadgesAchievement(data_json.get("achievement", None))
        self.id: str = data_json.get("id", "")
        self.is_created: bool = data_json.get("isCreated", False)
        self.large_url: str = data_json.get("largeUrl", "")
        self.medium_url: str = data_json.get("mediumUrl", "")
        self.name: str = data_json.get("name", "")
        self.small_url: str = data_json.get("smallUrl", "")
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataParentAuthorBadges ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataParentAuthor ------
class WssMessageChannelChatPushPubDataDataParentAuthor:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.avatar_url: str = data_json.get("avatarUrl", "")
        self.badges: list = [WssMessageChannelChatPushPubDataDataParentAuthorBadges(item) for item in data_json.get("badges", [])]
        self.display_name: str = data_json.get("displayName", "")
        self.has_avatar: bool = data_json.get("hasAvatar", False)
        self.id: int = data_json.get("id", 0)
        self.is_channel_moderator: bool = data_json.get("isChannelModerator", False)
        self.is_chat_moderator: bool = data_json.get("isChatModerator", False)
        self.is_owner: bool = data_json.get("isOwner", False)
        self.is_verified_streamer: bool = data_json.get("isVerifiedStreamer", False)
        self.name: str = data_json.get("name", "")
        self.nick: str = data_json.get("nick", "")
        self.nick_color: int = data_json.get("nickColor", 0)
        self.profile_links: list = data_json.get("profileLinks", [])
        self.roles: list = [WssMessageChannelChatPushPubDataDataParentAuthorRoles(item) for item in data_json.get("roles", [])]
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataParentAuthor ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataParentData ------
class WssMessageChannelChatPushPubDataDataParentData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.content: str = data_json.get("content", "")
        self.id: str = data_json.get("id", "")
        self.image_format: str = data_json.get("imageFormat", "")
        self.is_animated: bool = data_json.get("isAnimated", False)
        self.large_url: str = data_json.get("largeUrl", "")
        self.medium_url: str = data_json.get("mediumUrl", "")
        self.modificator: str = data_json.get("modificator", "")
        self.name: str = data_json.get("name", "")
        self.small_url: str = data_json.get("smallUrl", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataParentData ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataParent ------
class WssMessageChannelChatPushPubDataDataParent:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.author: WssMessageChannelChatPushPubDataDataParentAuthor = WssMessageChannelChatPushPubDataDataParentAuthor(data_json.get("author", None))
        self.created_at: int = data_json.get("createdAt", 0)
        self.data: list[WssMessageChannelChatPushPubDataDataParentData] = [WssMessageChannelChatPushPubDataDataParentData(item) for item in data_json.get("data", [])]
        self.id: int = data_json.get("id", 0)
        self.is_deleted: bool = data_json.get("isDeleted", False)
        self.is_private: bool = data_json.get("isPrivate", False)
        self.styles: list = data_json.get("styles", [])
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataParent ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataData ------
class WssMessageChannelChatPushPubDataDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: None = data_json.get("blogUrl", None)
        self.content: str = data_json.get("content", "")
        self.display_name: str = data_json.get("displayName", "")
        self.donation: bool = data_json.get("donation", False)
        self.explicit: bool = data_json.get("explicit", False)
        self.id: str | int = data_json.get("id", 0)
        self.image_format: str = data_json.get("imageFormat", "")
        self.is_animated: bool = data_json.get("isAnimated", False)
        self.large_url: str = data_json.get("largeUrl", "")
        self.medium_url: str = data_json.get("mediumUrl", "")
        self.modificator: str = data_json.get("modificator", "")
        self.name: str = data_json.get("name", "")
        self.nick: str = data_json.get("nick", "")
        self.nick_color: str = data_json.get("nickColor", "")
        self.small_url: str = data_json.get("smallUrl", "")
        self.type: str = data_json.get("type", "")
        self.url: str = data_json.get("url", "")
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataDataData ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubDataData ------
class WssMessageChannelChatPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.author: WssMessageChannelChatPushPubDataDataAuthor = WssMessageChannelChatPushPubDataDataAuthor(data_json.get("author", None))
        self.created_at: int = data_json.get("createdAt", 0)
        self.data: list[WssMessageChannelChatPushPubDataDataData] = [WssMessageChannelChatPushPubDataDataData(item) for item in data_json.get("data", [])]
        self.flags: WssMessageChannelChatPushPubDataDataFlags = WssMessageChannelChatPushPubDataDataFlags(data_json.get("flags", None))
        self.id: int = data_json.get("id", 0)
        self.is_deleted: bool = data_json.get("isDeleted", False)
        self.is_private: bool = data_json.get("isPrivate", False)
        self.parent: WssMessageChannelChatPushPubDataDataParent | None = WssMessageChannelChatPushPubDataDataParent(data_json.get("parent", None))
        self.stream_slot: None = data_json.get("streamSlot", None)
        self.styles: list | list[str] = data_json.get("styles", [])
        self.thread_id: str | None = data_json.get("threadId", "")
        self.user: WssMessageChannelChatPushPubDataDataUser = WssMessageChannelChatPushPubDataDataUser(data_json.get("user", None))
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubDataData ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPubData ------
class WssMessageChannelChatPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssMessageChannelChatPushPubDataData = WssMessageChannelChatPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPubData ------

# region ------ AUTO GENERATED WssMessageChannelChatPushPub ------
class WssMessageChannelChatPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssMessageChannelChatPushPubData = WssMessageChannelChatPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssMessageChannelChatPushPub ------

# region ------ AUTO GENERATED WssMessageChannelChatPush ------
class WssMessageChannelChatPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssMessageChannelChatPushPub = WssMessageChannelChatPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssMessageChannelChatPush ------

# region ------ AUTO GENERATED WssMessageChannelChat ------
class WssMessageChannelChat:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssMessageChannelChatPush = WssMessageChannelChatPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssMessageChannelChat ------
# endregion ------ AUTO GENERATED CLASS "WssMessageChannelChat" from JSON by Kostya12rus ------
