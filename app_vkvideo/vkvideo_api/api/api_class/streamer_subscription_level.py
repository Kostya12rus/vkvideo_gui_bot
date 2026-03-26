# region ------ AUTO GENERATED CLASS "VkapiStreamerSubscriptionLevel" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataExternalappsTelegram ------
class VkapiStreamerSubscriptionLevelDataExternalappsTelegram:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.groups: list = data_json.get("groups", [])
        self.is_configured: bool = data_json.get("isConfigured", False)
# endregion ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataExternalappsTelegram ------

# region ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataExternalappsDiscordDataRole ------
class VkapiStreamerSubscriptionLevelDataExternalappsDiscordDataRole:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.id: str = data_json.get("id", "")
        self.name: str = data_json.get("name", "")
# endregion ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataExternalappsDiscordDataRole ------

# region ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataExternalappsDiscordData ------
class VkapiStreamerSubscriptionLevelDataExternalappsDiscordData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.role: VkapiStreamerSubscriptionLevelDataExternalappsDiscordDataRole = VkapiStreamerSubscriptionLevelDataExternalappsDiscordDataRole(data_json.get("role", None))
# endregion ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataExternalappsDiscordData ------

# region ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataExternalappsDiscord ------
class VkapiStreamerSubscriptionLevelDataExternalappsDiscord:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: VkapiStreamerSubscriptionLevelDataExternalappsDiscordData = VkapiStreamerSubscriptionLevelDataExternalappsDiscordData(data_json.get("data", None))
        self.is_configured: bool = data_json.get("isConfigured", False)
# endregion ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataExternalappsDiscord ------

# region ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataExternalapps ------
class VkapiStreamerSubscriptionLevelDataExternalapps:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.discord: VkapiStreamerSubscriptionLevelDataExternalappsDiscord = VkapiStreamerSubscriptionLevelDataExternalappsDiscord(data_json.get("discord", None))
        self.telegram: VkapiStreamerSubscriptionLevelDataExternalappsTelegram = VkapiStreamerSubscriptionLevelDataExternalappsTelegram(data_json.get("telegram", None))
# endregion ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataExternalapps ------

# region ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataCurrencyprices ------
class VkapiStreamerSubscriptionLevelDataCurrencyprices:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.r_u_b: int = data_json.get("RUB", 0)
# endregion ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataCurrencyprices ------

# region ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataSmiles ------
class VkapiStreamerSubscriptionLevelDataSmiles:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.base_name: str = data_json.get("baseName", "")
        self.id: str = data_json.get("id", "")
        self.image_format: str = data_json.get("imageFormat", "")
        self.is_animated: bool = data_json.get("isAnimated", False)
        self.large_url: str = data_json.get("largeUrl", "")
        self.medium_url: str = data_json.get("mediumUrl", "")
        self.name: str = data_json.get("name", "")
        self.small_url: str = data_json.get("smallUrl", "")
# endregion ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataSmiles ------

# region ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataBadgesAchievement ------
class VkapiStreamerSubscriptionLevelDataBadgesAchievement:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.name: str = data_json.get("name", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataBadgesAchievement ------

# region ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataBadges ------
class VkapiStreamerSubscriptionLevelDataBadges:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.achievement: VkapiStreamerSubscriptionLevelDataBadgesAchievement = VkapiStreamerSubscriptionLevelDataBadgesAchievement(data_json.get("achievement", None))
        self.id: str = data_json.get("id", "")
        self.is_created: bool = data_json.get("isCreated", False)
        self.large_url: str = data_json.get("largeUrl", "")
        self.medium_url: str = data_json.get("mediumUrl", "")
        self.name: str = data_json.get("name", "")
        self.small_url: str = data_json.get("smallUrl", "")
# endregion ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataBadges ------

# region ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataDescription ------
class VkapiStreamerSubscriptionLevelDataDescription:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.content: str = data_json.get("content", "")
        self.height: int = data_json.get("height", 0)
        self.id: str = data_json.get("id", "")
        self.modificator: str = data_json.get("modificator", "")
        self.rendition: str = data_json.get("rendition", "")
        self.size: int = data_json.get("size", 0)
        self.type: str = data_json.get("type", "")
        self.url: str = data_json.get("url", "")
        self.width: int = data_json.get("width", 0)
# endregion ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataDescription ------

# region ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataData ------
class VkapiStreamerSubscriptionLevelDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.content: str = data_json.get("content", "")
        self.height: int = data_json.get("height", 0)
        self.id: str = data_json.get("id", "")
        self.modificator: str = data_json.get("modificator", "")
        self.rendition: str = data_json.get("rendition", "")
        self.size: int = data_json.get("size", 0)
        self.type: str = data_json.get("type", "")
        self.url: str = data_json.get("url", "")
        self.width: int = data_json.get("width", 0)
# endregion ------ AUTO GENERATED VkapiStreamerSubscriptionLevelDataData ------

# region ------ AUTO GENERATED VkapiStreamerSubscriptionLevelData ------
class VkapiStreamerSubscriptionLevelData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.badges: list[VkapiStreamerSubscriptionLevelDataBadges] = [VkapiStreamerSubscriptionLevelDataBadges(item) for item in data_json.get("badges", [])]
        self.bonus_multiplier: int | float = data_json.get("bonusMultiplier", 0)
        self.created_at: int = data_json.get("createdAt", 0)
        self.currency_prices: VkapiStreamerSubscriptionLevelDataCurrencyprices = VkapiStreamerSubscriptionLevelDataCurrencyprices(data_json.get("currencyPrices", None))
        self.data: list = [VkapiStreamerSubscriptionLevelDataData(item) for item in data_json.get("data", [])]
        self.description: list = [VkapiStreamerSubscriptionLevelDataDescription(item) for item in data_json.get("description", [])]
        self.external_apps: VkapiStreamerSubscriptionLevelDataExternalapps = VkapiStreamerSubscriptionLevelDataExternalapps(data_json.get("externalApps", None))
        self.external_id: int = data_json.get("externalId", 0)
        self.id: int = data_json.get("id", 0)
        self.is_archived: bool = data_json.get("isArchived", False)
        self.is_deleted: bool = data_json.get("isDeleted", False)
        self.name: str = data_json.get("name", "")
        self.owner_id: int = data_json.get("ownerId", 0)
        self.price: int = data_json.get("price", 0)
        self.priority: int = data_json.get("priority", 0)
        self.smiles: list[VkapiStreamerSubscriptionLevelDataSmiles] = [VkapiStreamerSubscriptionLevelDataSmiles(item) for item in data_json.get("smiles", [])]
# endregion ------ AUTO GENERATED VkapiStreamerSubscriptionLevelData ------

# region ------ AUTO GENERATED VkapiStreamerSubscriptionLevelSubscriptions ------
class VkapiStreamerSubscriptionLevelSubscriptions:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.custom_price: int = data_json.get("customPrice", 0)
        self.level_id: int = data_json.get("levelId", 0)
        self.next_pay_time: None = data_json.get("nextPayTime", None)
        self.off_time: int = data_json.get("offTime", 0)
# endregion ------ AUTO GENERATED VkapiStreamerSubscriptionLevelSubscriptions ------

# region ------ AUTO GENERATED VkapiStreamerSubscriptionLevel ------
class VkapiStreamerSubscriptionLevel:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.current_id: int = data_json.get("currentId", 0)
        self.data: list[VkapiStreamerSubscriptionLevelData] = [VkapiStreamerSubscriptionLevelData(item) for item in data_json.get("data", [])]
        self.next_id: int = data_json.get("nextId", 0)
        self.subscriptions: list[VkapiStreamerSubscriptionLevelSubscriptions] = [VkapiStreamerSubscriptionLevelSubscriptions(item) for item in data_json.get("subscriptions", [])]
# endregion ------ AUTO GENERATED VkapiStreamerSubscriptionLevel ------
# endregion ------ AUTO GENERATED CLASS "VkapiStreamerSubscriptionLevel" from JSON by Kostya12rus ------
