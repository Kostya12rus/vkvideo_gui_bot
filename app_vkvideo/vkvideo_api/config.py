MAX_RETRIES = 3
MAX_REQUEST_IN_TIME = 10
MAX_TIMEOUT_IN_SECONDS = 30

UPDATE_SUBSCRIPTIONS_LIST_INTERVAL = 300
UPDATE_ONLINE_SUBSCRIPTIONS_LIST_INTERVAL = 60
UPDATE_DROPS_LIST_INTERVAL = 300
UPDATE_CATALOG_LIST_INTERVAL = 300


BASE_URL = "https://live.vkvideo.ru/"
API_URL = "https://api.live.vkvideo.ru/"
HTTP_REQUESTS_TIME_SLEEP = [0.1, 0.3]

WSS_URL = "wss://pubsub.live.vkvideo.ru/connection/websocket?cf_protocol_version=v2"
WSS_TYPE_MESSAGE_RE = r"(\w.*):(\d+)(?:@\d+)?(?:#(\d+))?"
WSS_REQUESTS_TIME_SLEEP = [0.1, 0.3]
WSS_SUBSCRIPTIONS_ON_CONNECT = 300

USER_INFO_URL = "v8/actor"
USER_CURRENT_URL = "v1/user/current"
USER_HEARTBEAT_VIEWER_URL = "v1/channel/{}/stream/{}/heartbeat/viewer?" #c1ymba, c106cb61-1e5b-4f0b-bf6a-e5e4b2709bc0
USER_STREAM_VIEWS_URL = "v1/user/stream/views/?limit={}" #limit=3
DROP_CAMPAING_PRODUCTS_REQUEST_URL = "v1/drop_campaign/{}/products_request" #620

STREAMER_INFO_URL = "v1/blog/{}" #c1ymba
STREAMER_CHAT_URL = "v1/channel/{}/stream/slot/default/chat?limit={}" #c1ymba, limit=20
STREAMER_FOLLOW_URL = "v1/blog/{}/follow" #c1ymba
STREAMER_UNFOLLOW_URL = "v1/blog/{}/unsubscribe" #c1ymba
STREAMER_LIKE_URL = "v8/reaction" #c1ymba
STREAMER_STREAM_INFO_URL = "v1/channel/{}/stream/slot/default" #c1ymba
STREAMER_PINNED_MESSAGE_URL = "v1/channel/{}/stream/slot/default/chat/pinned_message" #c1ymba
STREAMER_CLAN_URL = "v8/channel/{}/clan" #c1ymba
STREAMER_PREDICTION_URL = "v1/channel/{}/stream/slot/default/prediction" #c1ymba
STREAMER_DROP_PROGRESS_URL = "v1/channel/{}/stream/slot/default/drop_campaign/progress/" #c1ymba
STREAMER_SMILE_URL = "v1/blog/{}/smile/user_set/?mode=public_video_stream" #c1ymba
STREAMER_RAID_URL = "v1/channel/{}/stream/slot/default/raid" #c1ymba
STREAMER_RAID_USER_STATE_URL = "v1/channel/{}/stream/slot/default/raid/user_state" #c1ymba
STREAMER_RAID_VIEWER_URL = "v1/channel/{}/stream/slot/default/raid/viewer" #c1ymba
STREAMER_POINT_URL = "v1/channel/{}/point" #c1ymba
STREAMER_POINT_BONUS_URL = "v1/channel/{}/point/bonus/" #c1ymba
STREAMER_POINT_REWARD_URL = "v1/channel/{}/point/reward/" #c1ymba
STREAMER_PENDING_BONUS_URL = "v1/channel/{}/point/pending_bonus/" #c1ymba
STREAMER_PENDING_BONUS_GATHER_URL = "v1/channel/{}/point/pending_bonus/{}/gather" #c1ymba, f65f6f87-4e29-4a84-8ce8-55cc054a3055

STREAMERS_ONLINE_SUBSCRIPTIONS_URL = "v1/%2Fuser%2Fpublic_video_stream%2Fsubscriptions%2Fonline%2F?limit={}&offset={}" #limit=50&offset=0
STREAMERS_SUBSCRIPTIONS_URL = "v1/user/subscriptions?limit={}&offset={}&with_follow=true" #limit=30&offset=0
STREAMERS_DROP_URL = "v1/catalog/public_video_streams/drops/?limit={}&offset={}" #limit=40&offset=0
STREAMERS_CATALOG_URL = "v1/catalog/public_video_streams/category/{}/stream/?limit={}&offset={}" #limit=40&offset=0

