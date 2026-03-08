# region ------ AUTO GENERATED CLASS "WssChatBanChannelChat" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssChatBanChannelChatPushPubDataBanneduser ------
class WssChatBanChannelChatPushPubDataBanneduser:
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
        self.vkplay_profile_link: str = data_json.get("vkplayProfileLink", "")
# endregion ------ AUTO GENERATED WssChatBanChannelChatPushPubDataBanneduser ------

# region ------ AUTO GENERATED WssChatBanChannelChatPushPubData ------
class WssChatBanChannelChatPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.banned_user: WssChatBanChannelChatPushPubDataBanneduser = WssChatBanChannelChatPushPubDataBanneduser(data_json.get("bannedUser", None))
        self.blog_id: int = data_json.get("blogId", 0)
        self.create_time: int = data_json.get("createTime", 0)
        self.expire_time: int = data_json.get("expireTime", 0)
        self.is_by_stream: bool = data_json.get("isByStream", False)
        self.is_permanent: bool = data_json.get("isPermanent", False)
        self.is_temporary: bool = data_json.get("isTemporary", False)
        self.remaining_time: None = data_json.get("remainingTime", None)
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssChatBanChannelChatPushPubData ------

# region ------ AUTO GENERATED WssChatBanChannelChatPushPub ------
class WssChatBanChannelChatPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssChatBanChannelChatPushPubData = WssChatBanChannelChatPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssChatBanChannelChatPushPub ------

# region ------ AUTO GENERATED WssChatBanChannelChatPush ------
class WssChatBanChannelChatPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssChatBanChannelChatPushPub = WssChatBanChannelChatPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssChatBanChannelChatPush ------

# region ------ AUTO GENERATED WssChatBanChannelChat ------
class WssChatBanChannelChat:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssChatBanChannelChatPush = WssChatBanChannelChatPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssChatBanChannelChat ------
# endregion ------ AUTO GENERATED CLASS "WssChatBanChannelChat" from JSON by Kostya12rus ------
