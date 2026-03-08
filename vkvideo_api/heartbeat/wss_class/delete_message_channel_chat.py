# region ------ AUTO GENERATED CLASS "WssDeleteMessageChannelChat" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED WssDeleteMessageChannelChatPushPubData ------
class WssDeleteMessageChannelChatPushPubData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.id: int = data_json.get("id", 0)
        self.type: str = data_json.get("type", "")
# endregion ------ AUTO GENERATED WssDeleteMessageChannelChatPushPubData ------

# region ------ AUTO GENERATED WssDeleteMessageChannelChatPushPub ------
class WssDeleteMessageChannelChatPushPub:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: WssDeleteMessageChannelChatPushPubData = WssDeleteMessageChannelChatPushPubData(data_json.get("data", None))
# endregion ------ AUTO GENERATED WssDeleteMessageChannelChatPushPub ------

# region ------ AUTO GENERATED WssDeleteMessageChannelChatPush ------
class WssDeleteMessageChannelChatPush:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.channel: str = data_json.get("channel", "")
        self.pub: WssDeleteMessageChannelChatPushPub = WssDeleteMessageChannelChatPushPub(data_json.get("pub", None))
# endregion ------ AUTO GENERATED WssDeleteMessageChannelChatPush ------

# region ------ AUTO GENERATED WssDeleteMessageChannelChat ------
class WssDeleteMessageChannelChat:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.push: WssDeleteMessageChannelChatPush = WssDeleteMessageChannelChatPush(data_json.get("push", None))
# endregion ------ AUTO GENERATED WssDeleteMessageChannelChat ------
# endregion ------ AUTO GENERATED CLASS "WssDeleteMessageChannelChat" from JSON by Kostya12rus ------
