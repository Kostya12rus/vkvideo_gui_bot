from enum import Enum

from .channel_state_channel_info import WssChannelStateChannelInfo
from .channel_stream_channel_info import WssChannelStreamChannelInfo
from .channel_stream_stream_slot import WssChannelStreamStreamSlot
from .chat_ban_channel_chat import WssChatBanChannelChat
from .chat_ban_channel_info import WssChatBanChannelInfo
from .chat_pinned_message_reaction_channel_chat import WssChatPinnedMessageReactionChannelChat
from .chat_pinned_message_reaction_v_channel_chat import WssChatPinnedMessageReactionVChannelChat
from .clean_chat_messages_channel_chat import WssCleanChatMessagesChannelChat
from .cp_balance_change_channel_info import WssCpBalanceChangeChannelInfo
from .cp_bonus_pending_channel_info import WssCpBonusPendingChannelInfo
from .delete_message_channel_chat import WssDeleteMessageChannelChat
from .drop_campaign_progress_channel_info import WssDropCampaignProgressChannelInfo
from .drop_progress_channel_info import WssDropProgressChannelInfo
from .message_channel_chat import WssMessageChannelChat
from .prediction_channel_info import WssPredictionChannelInfo
from .raid_status_channel_info import WssRaidStatusChannelInfo
from .raid_status_stream_slot import WssRaidStatusStreamSlot
from .stream_end_channel_info import WssStreamEndChannelInfo
from .stream_end_stream_slot import WssStreamEndStreamSlot
from .stream_info_update_channel_info import WssStreamInfoUpdateChannelInfo
from .stream_info_update_stream_slot import WssStreamInfoUpdateStreamSlot
from .stream_like_counter_channel_info import WssStreamLikeCounterChannelInfo
from .stream_like_counter_stream_slot import WssStreamLikeCounterStreamSlot
from .stream_online_status_channel_info import WssStreamOnlineStatusChannelInfo
from .stream_online_status_stream_slot import WssStreamOnlineStatusStreamSlot
from .stream_slot_end_channel_info import WssStreamSlotEndChannelInfo
from .stream_slot_end_stream_slot import WssStreamSlotEndStreamSlot
from .stream_slot_info_channel_info import WssStreamSlotInfoChannelInfo
from .stream_slot_info_update_channel_info import WssStreamSlotInfoUpdateChannelInfo
from .stream_slot_info_update_stream_slot import WssStreamSlotInfoUpdateStreamSlot
from .stream_slot_like_counter_channel_info import WssStreamSlotLikeCounterChannelInfo
from .stream_slot_like_counter_stream_slot import WssStreamSlotLikeCounterStreamSlot
from .stream_slot_online_status_channel_info import WssStreamSlotOnlineStatusChannelInfo
from .stream_slot_online_status_stream_slot import WssStreamSlotOnlineStatusStreamSlot
from .stream_slot_start_channel_info import WssStreamSlotStartChannelInfo
from .stream_slot_start_stream_slot import WssStreamSlotStartStreamSlot
from .stream_start_channel_info import WssStreamStartChannelInfo
from .stream_start_stream_slot import WssStreamStartStreamSlot


class WSSEventName(Enum):
    ON_MESSAGE = "on_message"
    ON_CONNECTED = "on_connected"
    ON_DISCONNECTED = "on_disconnected"
    CHANNEL_STATE_CHANNEL_INFO = "channel_state_channel_info"
    CHANNEL_STREAM_CHANNEL_INFO = "channel_stream_channel_info"
    CHANNEL_STREAM_STREAM_SLOT = "channel_stream_stream_slot"
    CHAT_BAN_CHANNEL_CHAT = "chat_ban_channel_chat"
    CHAT_BAN_CHANNEL_INFO = "chat_ban_channel_info"
    CHAT_PINNED_MESSAGE_REACTION_CHANNEL_CHAT = "chat_pinned_message_reaction_channel_chat"
    CHAT_PINNED_MESSAGE_REACTION_V_CHANNEL_CHAT = "chat_pinned_message_reaction_v_channel_chat"
    CLEAN_CHAT_MESSAGES_CHANNEL_CHAT = "clean_chat_messages_channel_chat"
    CP_BALANCE_CHANGE_CHANNEL_INFO = "cp_balance_change_channel_info"
    CP_BONUS_PENDING_CHANNEL_INFO = "cp_bonus_pending_channel_info"
    DELETE_MESSAGE_CHANNEL_CHAT = "delete_message_channel_chat"
    DROP_CAMPAIGN_PROGRESS_CHANNEL_INFO = "drop_campaign_progress_channel_info"
    DROP_PROGRESS_CHANNEL_INFO = "drop_progress_channel_info"
    MESSAGE_CHANNEL_CHAT = "message_channel_chat"
    PREDICTION_CHANNEL_INFO = "prediction_channel_info"
    RAID_STATUS_CHANNEL_INFO = "raid_status_channel_info"
    RAID_STATUS_STREAM_SLOT = "raid_status_stream_slot"
    STREAM_END_CHANNEL_INFO = "stream_end_channel_info"
    STREAM_END_STREAM_SLOT = "stream_end_stream_slot"
    STREAM_INFO_UPDATE_CHANNEL_INFO = "stream_info_update_channel_info"
    STREAM_INFO_UPDATE_STREAM_SLOT = "stream_info_update_stream_slot"
    STREAM_LIKE_COUNTER_CHANNEL_INFO = "stream_like_counter_channel_info"
    STREAM_LIKE_COUNTER_STREAM_SLOT = "stream_like_counter_stream_slot"
    STREAM_ONLINE_STATUS_CHANNEL_INFO = "stream_online_status_channel_info"
    STREAM_ONLINE_STATUS_STREAM_SLOT = "stream_online_status_stream_slot"
    STREAM_SLOT_END_CHANNEL_INFO = "stream_slot_end_channel_info"
    STREAM_SLOT_END_STREAM_SLOT = "stream_slot_end_stream_slot"
    STREAM_SLOT_INFO_CHANNEL_INFO = "stream_slot_info_channel_info"
    STREAM_SLOT_INFO_UPDATE_CHANNEL_INFO = "stream_slot_info_update_channel_info"
    STREAM_SLOT_INFO_UPDATE_STREAM_SLOT = "stream_slot_info_update_stream_slot"
    STREAM_SLOT_LIKE_COUNTER_CHANNEL_INFO = "stream_slot_like_counter_channel_info"
    STREAM_SLOT_LIKE_COUNTER_STREAM_SLOT = "stream_slot_like_counter_stream_slot"
    STREAM_SLOT_ONLINE_STATUS_CHANNEL_INFO = "stream_slot_online_status_channel_info"
    STREAM_SLOT_ONLINE_STATUS_STREAM_SLOT = "stream_slot_online_status_stream_slot"
    STREAM_SLOT_START_CHANNEL_INFO = "stream_slot_start_channel_info"
    STREAM_SLOT_START_STREAM_SLOT = "stream_slot_start_stream_slot"
    STREAM_START_CHANNEL_INFO = "stream_start_channel_info"
    STREAM_START_STREAM_SLOT = "stream_start_stream_slot"


WSSEventClass = {
    WSSEventName.CHANNEL_STATE_CHANNEL_INFO: WssChannelStateChannelInfo,
    WSSEventName.CHANNEL_STREAM_CHANNEL_INFO: WssChannelStreamChannelInfo,
    WSSEventName.CHANNEL_STREAM_STREAM_SLOT: WssChannelStreamStreamSlot,
    WSSEventName.CHAT_BAN_CHANNEL_CHAT: WssChatBanChannelChat,
    WSSEventName.CHAT_PINNED_MESSAGE_REACTION_CHANNEL_CHAT: WssChatPinnedMessageReactionChannelChat,
    WSSEventName.CHAT_PINNED_MESSAGE_REACTION_V_CHANNEL_CHAT: WssChatPinnedMessageReactionVChannelChat,
    WSSEventName.CLEAN_CHAT_MESSAGES_CHANNEL_CHAT: WssCleanChatMessagesChannelChat,
    WSSEventName.CP_BALANCE_CHANGE_CHANNEL_INFO: WssCpBalanceChangeChannelInfo,
    WSSEventName.CP_BONUS_PENDING_CHANNEL_INFO: WssCpBonusPendingChannelInfo,
    WSSEventName.DELETE_MESSAGE_CHANNEL_CHAT: WssDeleteMessageChannelChat,
    WSSEventName.DROP_CAMPAIGN_PROGRESS_CHANNEL_INFO: WssDropCampaignProgressChannelInfo,
    WSSEventName.DROP_PROGRESS_CHANNEL_INFO: WssDropProgressChannelInfo,
    WSSEventName.MESSAGE_CHANNEL_CHAT: WssMessageChannelChat,
    WSSEventName.PREDICTION_CHANNEL_INFO: WssPredictionChannelInfo,
    WSSEventName.RAID_STATUS_CHANNEL_INFO: WssRaidStatusChannelInfo,
    WSSEventName.RAID_STATUS_STREAM_SLOT: WssRaidStatusStreamSlot,
    WSSEventName.STREAM_END_CHANNEL_INFO: WssStreamEndChannelInfo,
    WSSEventName.STREAM_END_STREAM_SLOT: WssStreamEndStreamSlot,
    WSSEventName.STREAM_INFO_UPDATE_CHANNEL_INFO: WssStreamInfoUpdateChannelInfo,
    WSSEventName.STREAM_INFO_UPDATE_STREAM_SLOT: WssStreamInfoUpdateStreamSlot,
    WSSEventName.STREAM_LIKE_COUNTER_CHANNEL_INFO: WssStreamLikeCounterChannelInfo,
    WSSEventName.STREAM_LIKE_COUNTER_STREAM_SLOT: WssStreamLikeCounterStreamSlot,
    WSSEventName.STREAM_ONLINE_STATUS_CHANNEL_INFO: WssStreamOnlineStatusChannelInfo,
    WSSEventName.STREAM_ONLINE_STATUS_STREAM_SLOT: WssStreamOnlineStatusStreamSlot,
    WSSEventName.STREAM_SLOT_END_CHANNEL_INFO: WssStreamSlotEndChannelInfo,
    WSSEventName.STREAM_SLOT_END_STREAM_SLOT: WssStreamSlotEndStreamSlot,
    WSSEventName.STREAM_SLOT_INFO_CHANNEL_INFO: WssStreamSlotInfoChannelInfo,
    WSSEventName.STREAM_SLOT_INFO_UPDATE_CHANNEL_INFO: WssStreamSlotInfoUpdateChannelInfo,
    WSSEventName.STREAM_SLOT_INFO_UPDATE_STREAM_SLOT: WssStreamSlotInfoUpdateStreamSlot,
    WSSEventName.STREAM_SLOT_LIKE_COUNTER_CHANNEL_INFO: WssStreamSlotLikeCounterChannelInfo,
    WSSEventName.STREAM_SLOT_LIKE_COUNTER_STREAM_SLOT: WssStreamSlotLikeCounterStreamSlot,
    WSSEventName.STREAM_SLOT_ONLINE_STATUS_CHANNEL_INFO: WssStreamSlotOnlineStatusChannelInfo,
    WSSEventName.STREAM_SLOT_ONLINE_STATUS_STREAM_SLOT: WssStreamSlotOnlineStatusStreamSlot,
    WSSEventName.STREAM_SLOT_START_CHANNEL_INFO: WssStreamSlotStartChannelInfo,
    WSSEventName.STREAM_SLOT_START_STREAM_SLOT: WssStreamSlotStartStreamSlot,
    WSSEventName.STREAM_START_CHANNEL_INFO: WssStreamStartChannelInfo,
    WSSEventName.STREAM_START_STREAM_SLOT: WssStreamStartStreamSlot,
}

__all__ = [
    "WSSEventName", "WSSEventClass",
    "WssChannelStateChannelInfo",
    "WssChannelStreamChannelInfo",
    "WssChannelStreamStreamSlot",
    "WssChatBanChannelChat",
    "WssChatBanChannelInfo",
    "WssChatPinnedMessageReactionChannelChat",
    "WssChatPinnedMessageReactionVChannelChat",
    "WssCleanChatMessagesChannelChat",
    "WssCpBalanceChangeChannelInfo",
    "WssCpBonusPendingChannelInfo",
    "WssDeleteMessageChannelChat",
    "WssDropCampaignProgressChannelInfo",
    "WssDropProgressChannelInfo",
    "WssMessageChannelChat",
    "WssPredictionChannelInfo",
    "WssRaidStatusChannelInfo",
    "WssRaidStatusStreamSlot",
    "WssStreamEndChannelInfo",
    "WssStreamEndStreamSlot",
    "WssStreamInfoUpdateChannelInfo",
    "WssStreamInfoUpdateStreamSlot",
    "WssStreamLikeCounterChannelInfo",
    "WssStreamLikeCounterStreamSlot",
    "WssStreamOnlineStatusChannelInfo",
    "WssStreamOnlineStatusStreamSlot",
    "WssStreamSlotEndChannelInfo",
    "WssStreamSlotEndStreamSlot",
    "WssStreamSlotInfoChannelInfo",
    "WssStreamSlotInfoUpdateChannelInfo",
    "WssStreamSlotInfoUpdateStreamSlot",
    "WssStreamSlotLikeCounterChannelInfo",
    "WssStreamSlotLikeCounterStreamSlot",
    "WssStreamSlotOnlineStatusChannelInfo",
    "WssStreamSlotOnlineStatusStreamSlot",
    "WssStreamSlotStartChannelInfo",
    "WssStreamSlotStartStreamSlot",
    "WssStreamStartChannelInfo",
    "WssStreamStartStreamSlot",
]
