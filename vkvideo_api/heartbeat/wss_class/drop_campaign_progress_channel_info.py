# region ------ AUTO GENERATED CLASS "WssDropCampaignProgressChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCurrentruleProgress ------
class WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCurrentruleProgress:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.current: int = data_json.get("current", 0)
        self.goal: int = data_json.get("goal", 0)
        self.goal_reached: bool = data_json.get("goalReached", False)
# endregion ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCurrentruleProgress ------

# region ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCurrentruleProducts ------
class WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCurrentruleProducts:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.available_count: int = data_json.get("availableCount", 0)
        self.external_id: str = data_json.get("externalId", "")
        self.external_link: str = data_json.get("externalLink", "")
        self.id: int = data_json.get("id", 0)
        self.logo_url: str = data_json.get("logoUrl", "")
        self.source: str = data_json.get("source", "")
        self.title: str = data_json.get("title", "")
# endregion ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCurrentruleProducts ------

# region ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCurrentrule ------
class WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCurrentrule:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.id: int = data_json.get("id", 0)
        self.products: list[WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCurrentruleProducts] = [WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCurrentruleProducts(item) for item in data_json.get("products", [])]
        self.progress: WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCurrentruleProgress = WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCurrentruleProgress(data_json.get("progress", None))
        self.watching_duration: int = data_json.get("watchingDuration", 0)
# endregion ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCurrentrule ------

# region ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCampaignCategory ------
class WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCampaignCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.cover_url: str = data_json.get("coverUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCampaignCategory ------

# region ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCampaign ------
class WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCampaign:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.category: WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCampaignCategory = WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCampaignCategory(data_json.get("category", None))
        self.created_at: int = data_json.get("createdAt", 0)
        self.description: str = data_json.get("description", "")
        self.external_link: str = data_json.get("externalLink", "")
        self.id: int = data_json.get("id", 0)
        self.is_hidden: bool = data_json.get("isHidden", False)
        self.logo_url: str = data_json.get("logoUrl", "")
        self.rules_mode: str = data_json.get("rulesMode", "")
        self.start_at: int = data_json.get("startAt", 0)
        self.state: str = data_json.get("state", "")
        self.stop_at: int = data_json.get("stopAt", 0)
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
        self.updated_at: int = data_json.get("updatedAt", 0)
        self.vk_user_only: bool = data_json.get("vkUserOnly", False)
# endregion ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCampaign ------

# region ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubDataDataDropprogresses ------
class WssDropCampaignProgressChannelInfoPushPubDataDataDropprogresses:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.campaign: WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCampaign = WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCampaign(data_json.get("campaign", None))
        self.current_rule: WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCurrentrule = WssDropCampaignProgressChannelInfoPushPubDataDataDropprogressesCurrentrule(data_json.get("currentRule", None))
# endregion ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubDataDataDropprogresses ------

# region ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubDataData ------
class WssDropCampaignProgressChannelInfoPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.drop_progresses: list[WssDropCampaignProgressChannelInfoPushPubDataDataDropprogresses] = [WssDropCampaignProgressChannelInfoPushPubDataDataDropprogresses(item) for item in data_json.get("dropProgresses", [])]
# endregion ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubDataData ------

# region ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubData ------
class WssDropCampaignProgressChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssDropCampaignProgressChannelInfoPushPubDataData = WssDropCampaignProgressChannelInfoPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPub ------
class WssDropCampaignProgressChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssDropCampaignProgressChannelInfoPushPubData = WssDropCampaignProgressChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPushPub ------

# region ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPush ------
class WssDropCampaignProgressChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssDropCampaignProgressChannelInfoPushPub = WssDropCampaignProgressChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssDropCampaignProgressChannelInfoPush ------

# region ------ AUTO GENERATED WssDropCampaignProgressChannelInfo ------
class WssDropCampaignProgressChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssDropCampaignProgressChannelInfoPush = WssDropCampaignProgressChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssDropCampaignProgressChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssDropCampaignProgressChannelInfo" from JSON by Kostya12rus ------
