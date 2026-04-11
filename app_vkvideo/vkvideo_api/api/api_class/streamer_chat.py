# region ------ AUTO GENERATED CLASS "VkapiStreamerChat" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED VkapiStreamerChatExtra ------
class VkapiStreamerChatExtra:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.is_baned: bool = data_json.get("isBaned", False)
        self.is_last: bool = data_json.get("isLast", False)
# endregion ------ AUTO GENERATED VkapiStreamerChatExtra ------

# region ------ AUTO GENERATED VkapiStreamerChatDataFlags ------
class VkapiStreamerChatDataFlags:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.is_first_message: bool = data_json.get("isFirstMessage", False)
        self.is_parent_deleted: bool = data_json.get("isParentDeleted", False)
# endregion ------ AUTO GENERATED VkapiStreamerChatDataFlags ------

# region ------ AUTO GENERATED VkapiStreamerChatDataAuthorBadgesAchievement ------
class VkapiStreamerChatDataAuthorBadgesAchievement:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.name: str = data_json.get("name", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED VkapiStreamerChatDataAuthorBadgesAchievement ------

# region ------ AUTO GENERATED VkapiStreamerChatDataAuthorBadges ------
class VkapiStreamerChatDataAuthorBadges:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.achievement: VkapiStreamerChatDataAuthorBadgesAchievement = VkapiStreamerChatDataAuthorBadgesAchievement(data_json.get("achievement", None))
        self.id: str = data_json.get("id", "")
        self.is_created: bool = data_json.get("isCreated", False)
        self.large_url: str = data_json.get("largeUrl", "")
        self.medium_url: str = data_json.get("mediumUrl", "")
        self.name: str = data_json.get("name", "")
        self.small_url: str = data_json.get("smallUrl", "")
# endregion ------ AUTO GENERATED VkapiStreamerChatDataAuthorBadges ------

# region ------ AUTO GENERATED VkapiStreamerChatDataAuthor ------
class VkapiStreamerChatDataAuthor:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.avatar_url: str = data_json.get("avatarUrl", "")
        self.badges: list[VkapiStreamerChatDataAuthorBadges] = [VkapiStreamerChatDataAuthorBadges(item) for item in data_json.get("badges", [])]
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
        self.roles: list = data_json.get("roles", [])
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED VkapiStreamerChatDataAuthor ------

# region ------ AUTO GENERATED VkapiStreamerChatDataParentAuthorBadgesAchievement ------
class VkapiStreamerChatDataParentAuthorBadgesAchievement:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.name: str = data_json.get("name", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED VkapiStreamerChatDataParentAuthorBadgesAchievement ------

# region ------ AUTO GENERATED VkapiStreamerChatDataParentAuthorBadges ------
class VkapiStreamerChatDataParentAuthorBadges:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.achievement: VkapiStreamerChatDataParentAuthorBadgesAchievement = VkapiStreamerChatDataParentAuthorBadgesAchievement(data_json.get("achievement", None))
        self.id: str = data_json.get("id", "")
        self.is_created: bool = data_json.get("isCreated", False)
        self.large_url: str = data_json.get("largeUrl", "")
        self.medium_url: str = data_json.get("mediumUrl", "")
        self.name: str = data_json.get("name", "")
        self.small_url: str = data_json.get("smallUrl", "")
# endregion ------ AUTO GENERATED VkapiStreamerChatDataParentAuthorBadges ------

# region ------ AUTO GENERATED VkapiStreamerChatDataParentAuthor ------
class VkapiStreamerChatDataParentAuthor:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.avatar_url: str = data_json.get("avatarUrl", "")
        self.badges: list = [VkapiStreamerChatDataParentAuthorBadges(item) for item in data_json.get("badges", [])]
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
        self.roles: list = data_json.get("roles", [])
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED VkapiStreamerChatDataParentAuthor ------

# region ------ AUTO GENERATED VkapiStreamerChatDataParentData ------
class VkapiStreamerChatDataParentData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: None = data_json.get("blogUrl", None)
        self.content: str = data_json.get("content", "")
        self.display_name: str = data_json.get("displayName", "")
        self.donation: bool = data_json.get("donation", False)
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
# endregion ------ AUTO GENERATED VkapiStreamerChatDataParentData ------

# region ------ AUTO GENERATED VkapiStreamerChatDataParent ------
class VkapiStreamerChatDataParent:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.author: VkapiStreamerChatDataParentAuthor = VkapiStreamerChatDataParentAuthor(data_json.get("author", None))
        self.created_at: int = data_json.get("createdAt", 0)
        self.data: list[VkapiStreamerChatDataParentData] = [VkapiStreamerChatDataParentData(item) for item in data_json.get("data", [])]
        self.id: int = data_json.get("id", 0)
        self.is_deleted: bool = data_json.get("isDeleted", False)
        self.is_private: bool = data_json.get("isPrivate", False)
        self.styles: list = data_json.get("styles", [])
# endregion ------ AUTO GENERATED VkapiStreamerChatDataParent ------

# region ------ AUTO GENERATED VkapiStreamerChatDataData ------
class VkapiStreamerChatDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: None = data_json.get("blogUrl", None)
        self.content: str = data_json.get("content", "")
        self.display_name: str = data_json.get("displayName", "")
        self.donation: bool = data_json.get("donation", False)
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
# endregion ------ AUTO GENERATED VkapiStreamerChatDataData ------

# region ------ AUTO GENERATED VkapiStreamerChatData ------
class VkapiStreamerChatData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.author: VkapiStreamerChatDataAuthor = VkapiStreamerChatDataAuthor(data_json.get("author", None))
        self.created_at: int = data_json.get("createdAt", 0)
        self.data: list[VkapiStreamerChatDataData] = [VkapiStreamerChatDataData(item) for item in data_json.get("data", [])]
        self.flags: VkapiStreamerChatDataFlags = VkapiStreamerChatDataFlags(data_json.get("flags", None))
        self.id: int = data_json.get("id", 0)
        self.is_deleted: bool = data_json.get("isDeleted", False)
        self.is_private: bool = data_json.get("isPrivate", False)
        self.parent: None | VkapiStreamerChatDataParent = VkapiStreamerChatDataParent(data_json.get("parent", None))
        self.styles: list[str] | list = data_json.get("styles", [])
        self.thread_id: None | str = data_json.get("threadId", "")
# endregion ------ AUTO GENERATED VkapiStreamerChatData ------

# region ------ AUTO GENERATED VkapiStreamerChat ------
class VkapiStreamerChat:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: list[VkapiStreamerChatData] = [VkapiStreamerChatData(item) for item in data_json.get("data", [])]
        self.extra: VkapiStreamerChatExtra = VkapiStreamerChatExtra(data_json.get("extra", None))
# endregion ------ AUTO GENERATED VkapiStreamerChat ------
# endregion ------ AUTO GENERATED CLASS "VkapiStreamerChat" from JSON by Kostya12rus ------
