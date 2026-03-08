# region ------ AUTO GENERATED CLASS "WssRaidStatusChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubDataDataOwnerOwnerStreameractivity ------
class WssRaidStatusChannelInfoPushPubDataDataOwnerOwnerStreameractivity:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.level: int = data_json.get("level", 0)
# endregion ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubDataDataOwnerOwnerStreameractivity ------

# region ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubDataDataOwnerOwner ------
class WssRaidStatusChannelInfoPushPubDataDataOwnerOwner:
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
        self.streamer_activity: WssRaidStatusChannelInfoPushPubDataDataOwnerOwnerStreameractivity = WssRaidStatusChannelInfoPushPubDataDataOwnerOwnerStreameractivity(data_json.get("streamerActivity", None))
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubDataDataOwnerOwner ------

# region ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubDataDataOwner ------
class WssRaidStatusChannelInfoPushPubDataDataOwner:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: str = data_json.get("blogUrl", "")
        self.channel_cover_image_url: str = data_json.get("channelCoverImageUrl", "")
        self.channel_cover_type: str = data_json.get("channelCoverType", "")
        self.cover_url: str = data_json.get("coverUrl", "")
        self.has_adult_content: bool = data_json.get("hasAdultContent", False)
        self.owner: WssRaidStatusChannelInfoPushPubDataDataOwnerOwner = WssRaidStatusChannelInfoPushPubDataDataOwnerOwner(data_json.get("owner", None))
# endregion ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubDataDataOwner ------

# region ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubDataDataTargetOwnerStreameractivity ------
class WssRaidStatusChannelInfoPushPubDataDataTargetOwnerStreameractivity:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.level: int = data_json.get("level", 0)
# endregion ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubDataDataTargetOwnerStreameractivity ------

# region ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubDataDataTargetOwner ------
class WssRaidStatusChannelInfoPushPubDataDataTargetOwner:
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
        self.streamer_activity: WssRaidStatusChannelInfoPushPubDataDataTargetOwnerStreameractivity = WssRaidStatusChannelInfoPushPubDataDataTargetOwnerStreameractivity(data_json.get("streamerActivity", None))
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubDataDataTargetOwner ------

# region ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubDataDataTarget ------
class WssRaidStatusChannelInfoPushPubDataDataTarget:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: str = data_json.get("blogUrl", "")
        self.channel_cover_image_url: str = data_json.get("channelCoverImageUrl", "")
        self.channel_cover_type: str = data_json.get("channelCoverType", "")
        self.cover_url: str = data_json.get("coverUrl", "")
        self.has_adult_content: bool = data_json.get("hasAdultContent", False)
        self.owner: WssRaidStatusChannelInfoPushPubDataDataTargetOwner = WssRaidStatusChannelInfoPushPubDataDataTargetOwner(data_json.get("owner", None))
# endregion ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubDataDataTarget ------

# region ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubDataData ------
class WssRaidStatusChannelInfoPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.owner: WssRaidStatusChannelInfoPushPubDataDataOwner = WssRaidStatusChannelInfoPushPubDataDataOwner(data_json.get("owner", None))
        self.status: str = data_json.get("status", "")
        self.target: WssRaidStatusChannelInfoPushPubDataDataTarget = WssRaidStatusChannelInfoPushPubDataDataTarget(data_json.get("target", None))
        self.viewers_count: int = data_json.get("viewersCount", 0)
# endregion ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubDataData ------

# region ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubData ------
class WssRaidStatusChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssRaidStatusChannelInfoPushPubDataData = WssRaidStatusChannelInfoPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssRaidStatusChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssRaidStatusChannelInfoPushPub ------
class WssRaidStatusChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssRaidStatusChannelInfoPushPubData = WssRaidStatusChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssRaidStatusChannelInfoPushPub ------

# region ------ AUTO GENERATED WssRaidStatusChannelInfoPush ------
class WssRaidStatusChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssRaidStatusChannelInfoPushPub = WssRaidStatusChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssRaidStatusChannelInfoPush ------

# region ------ AUTO GENERATED WssRaidStatusChannelInfo ------
class WssRaidStatusChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssRaidStatusChannelInfoPush = WssRaidStatusChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssRaidStatusChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssRaidStatusChannelInfo" from JSON by Kostya12rus ------
