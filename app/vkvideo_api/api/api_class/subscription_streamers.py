# region ------ AUTO GENERATED CLASS "VkapiSubscriptionStreamers" from JSON by Kostya12rus ------
# region ------ AUTO GENERATED VkapiSubscriptionStreamersDataBlogOwner ------
class VkapiSubscriptionStreamersDataBlogOwner:
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
        self.vkplay_profile_link: None = data_json.get("vkplayProfileLink", None)
# endregion ------ AUTO GENERATED VkapiSubscriptionStreamersDataBlogOwner ------

# region ------ AUTO GENERATED VkapiSubscriptionStreamersDataBlog ------
class VkapiSubscriptionStreamersDataBlog:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog_url: str = data_json.get("blogUrl", "")
        self.channel_cover_image_url: str = data_json.get("channelCoverImageUrl", "")
        self.channel_cover_type: str = data_json.get("channelCoverType", "")
        self.cover_url: str = data_json.get("coverUrl", "")
        self.has_adult_content: bool = data_json.get("hasAdultContent", False)
        self.owner: VkapiSubscriptionStreamersDataBlogOwner = VkapiSubscriptionStreamersDataBlogOwner(data_json.get("owner", None))
        self.title: str = data_json.get("title", "")
# endregion ------ AUTO GENERATED VkapiSubscriptionStreamersDataBlog ------

# region ------ AUTO GENERATED VkapiSubscriptionStreamersData ------
class VkapiSubscriptionStreamersData:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.blog: VkapiSubscriptionStreamersDataBlog = VkapiSubscriptionStreamersDataBlog(data_json.get("blog", None))
        self.custom_price: int = data_json.get("customPrice", 0)
        self.level_id: int = data_json.get("levelId", 0)
        self.name: str = data_json.get("name", "")
        self.next_pay_time: None = data_json.get("nextPayTime", None)
        self.off_time: int | None = data_json.get("offTime", 0)
        self.on_time: int = data_json.get("onTime", 0)
        self.owner_id: int = data_json.get("ownerId", 0)
        self.period: int = data_json.get("period", 0)
        self.price: int = data_json.get("price", 0)
        self.subscriber_id: int = data_json.get("subscriberId", 0)
# endregion ------ AUTO GENERATED VkapiSubscriptionStreamersData ------

# region ------ AUTO GENERATED VkapiSubscriptionStreamers ------
class VkapiSubscriptionStreamers:
    def __init__(self, data_json: dict = None):
        if not data_json: data_json = {}
        self._data_json = data_json

        self.data: list[VkapiSubscriptionStreamersData] = [VkapiSubscriptionStreamersData(item) for item in data_json.get("data", [])]
        self.limit: int = data_json.get("limit", 0)
        self.offset: int = data_json.get("offset", 0)
        self.total: int = data_json.get("total", 0)
# endregion ------ AUTO GENERATED VkapiSubscriptionStreamers ------
# endregion ------ AUTO GENERATED CLASS "VkapiSubscriptionStreamers" from JSON by Kostya12rus ------
