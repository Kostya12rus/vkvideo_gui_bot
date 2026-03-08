# region ------ AUTO GENERATED CLASS "WssChatPinnedMessageReactionVChannelChat" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssChatPinnedMessageReactionVChannelChatPushPubDataDataChatpinnedmessagereactionReactions ------
class WssChatPinnedMessageReactionVChannelChatPushPubDataDataChatpinnedmessagereactionReactions:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.count: int = data_json.get("count", 0)
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssChatPinnedMessageReactionVChannelChatPushPubDataDataChatpinnedmessagereactionReactions ------

# region ------ AUTO GENERATED WssChatPinnedMessageReactionVChannelChatPushPubDataDataChatpinnedmessagereaction ------
class WssChatPinnedMessageReactionVChannelChatPushPubDataDataChatpinnedmessagereaction:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.id: int = data_json.get("id", 0)
        self.reactions: list[WssChatPinnedMessageReactionVChannelChatPushPubDataDataChatpinnedmessagereactionReactions] = [WssChatPinnedMessageReactionVChannelChatPushPubDataDataChatpinnedmessagereactionReactions(item) for item in data_json.get("reactions", [])]
# endregion ------ AUTO GENERATED WssChatPinnedMessageReactionVChannelChatPushPubDataDataChatpinnedmessagereaction ------

# region ------ AUTO GENERATED WssChatPinnedMessageReactionVChannelChatPushPubDataData ------
class WssChatPinnedMessageReactionVChannelChatPushPubDataData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.chat_pinned_message_reaction: WssChatPinnedMessageReactionVChannelChatPushPubDataDataChatpinnedmessagereaction = WssChatPinnedMessageReactionVChannelChatPushPubDataDataChatpinnedmessagereaction(data_json.get("chatPinnedMessageReaction", None))
# endregion ------ AUTO GENERATED WssChatPinnedMessageReactionVChannelChatPushPubDataData ------

# region ------ AUTO GENERATED WssChatPinnedMessageReactionVChannelChatPushPubData ------
class WssChatPinnedMessageReactionVChannelChatPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssChatPinnedMessageReactionVChannelChatPushPubDataData = WssChatPinnedMessageReactionVChannelChatPushPubDataData(data_json.get("data", None))
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssChatPinnedMessageReactionVChannelChatPushPubData ------

# region ------ AUTO GENERATED WssChatPinnedMessageReactionVChannelChatPushPub ------
class WssChatPinnedMessageReactionVChannelChatPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssChatPinnedMessageReactionVChannelChatPushPubData = WssChatPinnedMessageReactionVChannelChatPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssChatPinnedMessageReactionVChannelChatPushPub ------

# region ------ AUTO GENERATED WssChatPinnedMessageReactionVChannelChatPush ------
class WssChatPinnedMessageReactionVChannelChatPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssChatPinnedMessageReactionVChannelChatPushPub = WssChatPinnedMessageReactionVChannelChatPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssChatPinnedMessageReactionVChannelChatPush ------

# region ------ AUTO GENERATED WssChatPinnedMessageReactionVChannelChat ------
class WssChatPinnedMessageReactionVChannelChat:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssChatPinnedMessageReactionVChannelChatPush = WssChatPinnedMessageReactionVChannelChatPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssChatPinnedMessageReactionVChannelChat ------
# endregion ------ AUTO GENERATED CLASS "WssChatPinnedMessageReactionVChannelChat" from JSON by Kostya12rus ------
