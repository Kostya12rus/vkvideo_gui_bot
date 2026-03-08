# region ------ AUTO GENERATED CLASS "WssChatPinnedMessageReactionChannelChat" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssChatPinnedMessageReactionChannelChatPushPubDataReactions ------
class WssChatPinnedMessageReactionChannelChatPushPubDataReactions:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.count: str | int = data_json.get("count", 0)
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssChatPinnedMessageReactionChannelChatPushPubDataReactions ------

# region ------ AUTO GENERATED WssChatPinnedMessageReactionChannelChatPushPubData ------
class WssChatPinnedMessageReactionChannelChatPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.id: int = data_json.get("id", 0)
        self.reactions: list[WssChatPinnedMessageReactionChannelChatPushPubDataReactions] = [WssChatPinnedMessageReactionChannelChatPushPubDataReactions(item) for item in data_json.get("reactions", [])]
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssChatPinnedMessageReactionChannelChatPushPubData ------

# region ------ AUTO GENERATED WssChatPinnedMessageReactionChannelChatPushPub ------
class WssChatPinnedMessageReactionChannelChatPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssChatPinnedMessageReactionChannelChatPushPubData = WssChatPinnedMessageReactionChannelChatPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssChatPinnedMessageReactionChannelChatPushPub ------

# region ------ AUTO GENERATED WssChatPinnedMessageReactionChannelChatPush ------
class WssChatPinnedMessageReactionChannelChatPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssChatPinnedMessageReactionChannelChatPushPub = WssChatPinnedMessageReactionChannelChatPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssChatPinnedMessageReactionChannelChatPush ------

# region ------ AUTO GENERATED WssChatPinnedMessageReactionChannelChat ------
class WssChatPinnedMessageReactionChannelChat:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssChatPinnedMessageReactionChannelChatPush = WssChatPinnedMessageReactionChannelChatPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssChatPinnedMessageReactionChannelChat ------
# endregion ------ AUTO GENERATED CLASS "WssChatPinnedMessageReactionChannelChat" from JSON by Kostya12rus ------
