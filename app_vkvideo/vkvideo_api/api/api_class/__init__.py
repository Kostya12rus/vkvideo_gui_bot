from enum import Enum

from .catalog_streamers import VkapiCatalogStreamers
from .drop_streamers import VkapiDropStreamers
from .online_subscription_streamers import VkapiOnlineSubscriptionStreamers
from .streamer_info import VkapiStreamerInfo
from .streamer_pending_bonus import VkapiStreamerPendingBonus
from .streamer_stream_info import VkapiStreamerStreamInfo
from .streamer_subscription_level import VkapiStreamerSubscriptionLevel
from .subscription_streamers import VkapiSubscriptionStreamers


class VKAPIEventName(Enum):
    SUBSCRIPTION_STREAMERS = "subscription_streamers"
    ONLINE_SUBSCRIPTION_STREAMERS = "online_subscription_streamers"
    DROP_STREAMERS = "drop_streamers"
    CATALOG_STREAMERS = "catalog_streamers"
    STREAMER_INFO = "streamer_info"
    STREAMER_STREAM_INFO = "streamer_stream_info"
    STREAMER_PENDING_BONUS = "streamer_pending_bonus"
    STREAMER_SUBSCRIPTION_LEVEL = "streamer_subscription_level"


VKAPIEventClass = {
    VKAPIEventName.SUBSCRIPTION_STREAMERS: VkapiSubscriptionStreamers,
    VKAPIEventName.ONLINE_SUBSCRIPTION_STREAMERS: VkapiOnlineSubscriptionStreamers,
    VKAPIEventName.DROP_STREAMERS: VkapiDropStreamers,
    VKAPIEventName.CATALOG_STREAMERS: VkapiCatalogStreamers,
    VKAPIEventName.STREAMER_INFO: VkapiStreamerInfo,
    VKAPIEventName.STREAMER_STREAM_INFO: VkapiStreamerStreamInfo,
    VKAPIEventName.STREAMER_PENDING_BONUS: VkapiStreamerPendingBonus,
    VKAPIEventName.STREAMER_SUBSCRIPTION_LEVEL: VkapiStreamerSubscriptionLevel,
}

__all__ = [
    "VKAPIEventName", "VKAPIEventClass",
    "VkapiSubscriptionStreamers",
    "VkapiOnlineSubscriptionStreamers",
    "VkapiDropStreamers",
    "VkapiCatalogStreamers",
    "VkapiStreamerInfo",
    "VkapiStreamerStreamInfo",
    "VkapiStreamerPendingBonus",
    "VkapiStreamerSubscriptionLevel",
]
