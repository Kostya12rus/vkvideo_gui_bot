# region ------ AUTO GENERATED CLASS "WssPredictionChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssPredictionChannelInfoPushPubDataDataCreator ------
class WssPredictionChannelInfoPushPubDataDataCreator:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.id: int = data_json.get("id", 0)
        self.name: str = data_json.get("name", "")
        self.nick: str = data_json.get("nick", "")
# endregion ------ AUTO GENERATED WssPredictionChannelInfoPushPubDataDataCreator ------

# region ------ AUTO GENERATED WssPredictionChannelInfoPushPubDataDataDecisionsBiggestbiduser ------
class WssPredictionChannelInfoPushPubDataDataDecisionsBiggestbiduser:
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
# endregion ------ AUTO GENERATED WssPredictionChannelInfoPushPubDataDataDecisionsBiggestbiduser ------

# region ------ AUTO GENERATED WssPredictionChannelInfoPushPubDataDataDecisions ------
class WssPredictionChannelInfoPushPubDataDataDecisions:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.biggest_bid_user: WssPredictionChannelInfoPushPubDataDataDecisionsBiggestbiduser = WssPredictionChannelInfoPushPubDataDataDecisionsBiggestbiduser(data_json.get("biggestBidUser", None))
        self.biggest_win_amount: int = data_json.get("biggestWinAmount", 0)
        self.id: int = data_json.get("id", 0)
        self.is_winner: bool = data_json.get("isWinner", False)
        self.name: str = data_json.get("name", "")
        self.order: int = data_json.get("order", 0)
        self.points_bank: int = data_json.get("pointsBank", 0)
        self.proportion: float | int = data_json.get("proportion", 0)
        self.user_amount: int = data_json.get("userAmount", 0)
# endregion ------ AUTO GENERATED WssPredictionChannelInfoPushPubDataDataDecisions ------

# region ------ AUTO GENERATED WssPredictionChannelInfoPushPubDataData ------
class WssPredictionChannelInfoPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.created_at: int = data_json.get("createdAt", 0)
        self.creator: WssPredictionChannelInfoPushPubDataDataCreator = WssPredictionChannelInfoPushPubDataDataCreator(data_json.get("creator", None))
        self.decisions: list[WssPredictionChannelInfoPushPubDataDataDecisions] = [WssPredictionChannelInfoPushPubDataDataDecisions(item) for item in data_json.get("decisions", [])]
        self.duration: int = data_json.get("duration", 0)
        self.id: int = data_json.get("id", 0)
        self.points_bank: int = data_json.get("pointsBank", 0)
        self.state: str = data_json.get("state", "")
        self.title: str = data_json.get("title", "")
# endregion ------ AUTO GENERATED WssPredictionChannelInfoPushPubDataData ------

# region ------ AUTO GENERATED WssPredictionChannelInfoPushPubData ------
class WssPredictionChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssPredictionChannelInfoPushPubDataData = WssPredictionChannelInfoPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssPredictionChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssPredictionChannelInfoPushPub ------
class WssPredictionChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssPredictionChannelInfoPushPubData = WssPredictionChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssPredictionChannelInfoPushPub ------

# region ------ AUTO GENERATED WssPredictionChannelInfoPush ------
class WssPredictionChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssPredictionChannelInfoPushPub = WssPredictionChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssPredictionChannelInfoPush ------

# region ------ AUTO GENERATED WssPredictionChannelInfo ------
class WssPredictionChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssPredictionChannelInfoPush = WssPredictionChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssPredictionChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssPredictionChannelInfo" from JSON by Kostya12rus ------
