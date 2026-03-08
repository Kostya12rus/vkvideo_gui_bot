from enum import Enum

from .subscription_streamers import VkapiSubscriptionStreamers
from .drop_streamers import VkapiDropStreamers
from .streamer_info import VkapiStreamerInfo
from .streamer_stream_info import VkapiStreamerStreamInfo
from .streamer_pending_bonus import VkapiStreamerPendingBonus


class VKAPIEventName(Enum):
    SUBSCRIPTION_STREAMERS = "subscription_streamers"
    DROP_STREAMERS = "drop_streamers"
    STREAMER_INFO = "streamer_info"
    STREAMER_STREAM_INFO = "streamer_stream_info"
    STREAMER_PENDING_BONUS = "streamer_pending_bonus"


VKAPIEventClass = {
    VKAPIEventName.SUBSCRIPTION_STREAMERS: VkapiSubscriptionStreamers,
    VKAPIEventName.DROP_STREAMERS: VkapiDropStreamers,
    VKAPIEventName.STREAMER_INFO: VkapiStreamerInfo,
    VKAPIEventName.STREAMER_STREAM_INFO: VkapiStreamerStreamInfo,
    VKAPIEventName.STREAMER_PENDING_BONUS: VkapiStreamerPendingBonus,
}

__all__ = [
    "VKAPIEventName", "VKAPIEventClass",
    "VkapiSubscriptionStreamers",
    "VkapiDropStreamers",
    "VkapiStreamerInfo",
    "VkapiStreamerStreamInfo",
    "VkapiStreamerPendingBonus",
]
