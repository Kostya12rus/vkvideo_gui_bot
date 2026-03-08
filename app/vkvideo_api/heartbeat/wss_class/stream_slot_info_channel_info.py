# region ------ AUTO GENERATED CLASS "WssStreamSlotInfoChannelInfo" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPushPubDataDataStreamslotCategory ------
class WssStreamSlotInfoChannelInfoPushPubDataDataStreamslotCategory:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.cover_url: str = data_json.get("coverUrl", "")
        self.id: str = data_json.get("id", "")
        self.title: str = data_json.get("title", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPushPubDataDataStreamslotCategory ------

# region ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPushPubDataDataStreamslotCount ------
class WssStreamSlotInfoChannelInfoPushPubDataDataStreamslotCount:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.viewers: int = data_json.get("viewers", 0)
# endregion ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPushPubDataDataStreamslotCount ------

# region ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPushPubDataDataStreamslotTitledata ------
class WssStreamSlotInfoChannelInfoPushPubDataDataStreamslotTitledata:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: str = data_json.get("blogUrl", "")
        self.content: str = data_json.get("content", "")
        self.display_name: str = data_json.get("displayName", "")
        self.id: int = data_json.get("id", 0)
        self.modificator: str = data_json.get("modificator", "")
        self.name: str = data_json.get("name", "")
        self.nick: str = data_json.get("nick", "")
        self.nick_color: str = data_json.get("nickColor", "")
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPushPubDataDataStreamslotTitledata ------

# region ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPushPubDataDataStreamslot ------
class WssStreamSlotInfoChannelInfoPushPubDataDataStreamslot:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.category: WssStreamSlotInfoChannelInfoPushPubDataDataStreamslotCategory = WssStreamSlotInfoChannelInfoPushPubDataDataStreamslotCategory(data_json.get("category", None))
        self.channel_cover_type: str = data_json.get("channelCoverType", "")
        self.count: WssStreamSlotInfoChannelInfoPushPubDataDataStreamslotCount = WssStreamSlotInfoChannelInfoPushPubDataDataStreamslotCount(data_json.get("count", None))
        self.cover_image_changed_at: int = data_json.get("coverImageChangedAt", 0)
        self.cover_image_url: str = data_json.get("coverImageUrl", "")
        self.created_at: int = data_json.get("createdAt", 0)
        self.id: int = data_json.get("id", 0)
        self.is_deleted: bool = data_json.get("isDeleted", False)
        self.is_infinite: bool = data_json.get("isInfinite", False)
        self.is_online: bool = data_json.get("isOnline", False)
        self.is_playback_disabled: bool = data_json.get("isPlaybackDisabled", False)
        self.is_stream_hidden_default: bool = data_json.get("isStreamHiddenDefault", False)
        self.is_temporary: bool = data_json.get("isTemporary", False)
        self.is_vk_wallpost_create: bool = data_json.get("isVkWallpostCreate", False)
        self.planned_at: None = data_json.get("plannedAt", None)
        self.planned_end_at: None = data_json.get("plannedEndAt", None)
        self.preview_url: str = data_json.get("previewUrl", "")
        self.self_public_streams_hidden: bool = data_json.get("selfPublicStreamsHidden", False)
        self.slot_url: str = data_json.get("slotUrl", "")
        self.title: str = data_json.get("title", "")
        self.title_data: list[WssStreamSlotInfoChannelInfoPushPubDataDataStreamslotTitledata] = [WssStreamSlotInfoChannelInfoPushPubDataDataStreamslotTitledata(item) for item in data_json.get("titleData", [])]
        self.updated_at: int = data_json.get("updatedAt", 0)
        self.vk_wallpost_url: str = data_json.get("vkWallpostUrl", "")
# endregion ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPushPubDataDataStreamslot ------

# region ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPushPubDataData ------
class WssStreamSlotInfoChannelInfoPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.stream_slot: WssStreamSlotInfoChannelInfoPushPubDataDataStreamslot = WssStreamSlotInfoChannelInfoPushPubDataDataStreamslot(data_json.get("streamSlot", None))
# endregion ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPushPubDataData ------

# region ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPushPubData ------
class WssStreamSlotInfoChannelInfoPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotInfoChannelInfoPushPubDataData = WssStreamSlotInfoChannelInfoPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPushPubData ------

# region ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPushPub ------
class WssStreamSlotInfoChannelInfoPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssStreamSlotInfoChannelInfoPushPubData = WssStreamSlotInfoChannelInfoPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPushPub ------

# region ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPush ------
class WssStreamSlotInfoChannelInfoPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssStreamSlotInfoChannelInfoPushPub = WssStreamSlotInfoChannelInfoPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssStreamSlotInfoChannelInfoPush ------

# region ------ AUTO GENERATED WssStreamSlotInfoChannelInfo ------
class WssStreamSlotInfoChannelInfo:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssStreamSlotInfoChannelInfoPush = WssStreamSlotInfoChannelInfoPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssStreamSlotInfoChannelInfo ------
# endregion ------ AUTO GENERATED CLASS "WssStreamSlotInfoChannelInfo" from JSON by Kostya12rus ------
