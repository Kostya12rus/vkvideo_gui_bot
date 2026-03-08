# region ------ AUTO GENERATED CLASS "WssCleanChatMessagesChannelChat" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssCleanChatMessagesChannelChatPushPubData ------
class WssCleanChatMessagesChannelChatPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.type: str = data_json.get("type", "")
        self.user_id: int = data_json.get("userId", 0)
# endregion ------ AUTO GENERATED WssCleanChatMessagesChannelChatPushPubData ------

# region ------ AUTO GENERATED WssCleanChatMessagesChannelChatPushPub ------
class WssCleanChatMessagesChannelChatPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssCleanChatMessagesChannelChatPushPubData = WssCleanChatMessagesChannelChatPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssCleanChatMessagesChannelChatPushPub ------

# region ------ AUTO GENERATED WssCleanChatMessagesChannelChatPush ------
class WssCleanChatMessagesChannelChatPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssCleanChatMessagesChannelChatPushPub = WssCleanChatMessagesChannelChatPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssCleanChatMessagesChannelChatPush ------

# region ------ AUTO GENERATED WssCleanChatMessagesChannelChat ------
class WssCleanChatMessagesChannelChat:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssCleanChatMessagesChannelChatPush = WssCleanChatMessagesChannelChatPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssCleanChatMessagesChannelChat ------
# endregion ------ AUTO GENERATED CLASS "WssCleanChatMessagesChannelChat" from JSON by Kostya12rus ------
