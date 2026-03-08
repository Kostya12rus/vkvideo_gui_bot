# region ------ AUTO GENERATED CLASS "WssRaidStatusStreamSlot" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubDataDataOwnerOwnerStreameractivity ------
class WssRaidStatusStreamSlotPushPubDataDataOwnerOwnerStreameractivity:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.level: int = data_json.get("level", 0)
# endregion ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubDataDataOwnerOwnerStreameractivity ------

# region ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubDataDataOwnerOwner ------
class WssRaidStatusStreamSlotPushPubDataDataOwnerOwner:
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
        self.streamer_activity: WssRaidStatusStreamSlotPushPubDataDataOwnerOwnerStreameractivity = WssRaidStatusStreamSlotPushPubDataDataOwnerOwnerStreameractivity(data_json.get("streamerActivity", None))
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubDataDataOwnerOwner ------

# region ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubDataDataOwner ------
class WssRaidStatusStreamSlotPushPubDataDataOwner:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: str = data_json.get("blogUrl", "")
        self.channel_cover_image_url: str = data_json.get("channelCoverImageUrl", "")
        self.channel_cover_type: str = data_json.get("channelCoverType", "")
        self.cover_url: str = data_json.get("coverUrl", "")
        self.has_adult_content: bool = data_json.get("hasAdultContent", False)
        self.owner: WssRaidStatusStreamSlotPushPubDataDataOwnerOwner = WssRaidStatusStreamSlotPushPubDataDataOwnerOwner(data_json.get("owner", None))
# endregion ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubDataDataOwner ------

# region ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubDataDataTargetOwnerStreameractivity ------
class WssRaidStatusStreamSlotPushPubDataDataTargetOwnerStreameractivity:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.level: int = data_json.get("level", 0)
# endregion ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubDataDataTargetOwnerStreameractivity ------

# region ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubDataDataTargetOwner ------
class WssRaidStatusStreamSlotPushPubDataDataTargetOwner:
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
        self.streamer_activity: WssRaidStatusStreamSlotPushPubDataDataTargetOwnerStreameractivity = WssRaidStatusStreamSlotPushPubDataDataTargetOwnerStreameractivity(data_json.get("streamerActivity", None))
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubDataDataTargetOwner ------

# region ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubDataDataTarget ------
class WssRaidStatusStreamSlotPushPubDataDataTarget:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: str = data_json.get("blogUrl", "")
        self.channel_cover_image_url: str = data_json.get("channelCoverImageUrl", "")
        self.channel_cover_type: str = data_json.get("channelCoverType", "")
        self.cover_url: str = data_json.get("coverUrl", "")
        self.has_adult_content: bool = data_json.get("hasAdultContent", False)
        self.owner: WssRaidStatusStreamSlotPushPubDataDataTargetOwner = WssRaidStatusStreamSlotPushPubDataDataTargetOwner(data_json.get("owner", None))
# endregion ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubDataDataTarget ------

# region ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubDataData ------
class WssRaidStatusStreamSlotPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.owner: WssRaidStatusStreamSlotPushPubDataDataOwner = WssRaidStatusStreamSlotPushPubDataDataOwner(data_json.get("owner", None))
        self.status: str = data_json.get("status", "")
        self.target: WssRaidStatusStreamSlotPushPubDataDataTarget = WssRaidStatusStreamSlotPushPubDataDataTarget(data_json.get("target", None))
        self.viewers_count: int = data_json.get("viewersCount", 0)
# endregion ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubDataData ------

# region ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubData ------
class WssRaidStatusStreamSlotPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssRaidStatusStreamSlotPushPubDataData = WssRaidStatusStreamSlotPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssRaidStatusStreamSlotPushPubData ------

# region ------ AUTO GENERATED WssRaidStatusStreamSlotPushPub ------
class WssRaidStatusStreamSlotPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssRaidStatusStreamSlotPushPubData = WssRaidStatusStreamSlotPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssRaidStatusStreamSlotPushPub ------

# region ------ AUTO GENERATED WssRaidStatusStreamSlotPush ------
class WssRaidStatusStreamSlotPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssRaidStatusStreamSlotPushPub = WssRaidStatusStreamSlotPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssRaidStatusStreamSlotPush ------

# region ------ AUTO GENERATED WssRaidStatusStreamSlot ------
class WssRaidStatusStreamSlot:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssRaidStatusStreamSlotPush = WssRaidStatusStreamSlotPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssRaidStatusStreamSlot ------
# endregion ------ AUTO GENERATED CLASS "WssRaidStatusStreamSlot" from JSON by Kostya12rus ------
