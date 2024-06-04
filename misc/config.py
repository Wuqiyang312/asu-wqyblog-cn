from pathlib import Path

# disable test and debug features
TESTING = False
DEBUG = False

# where to find the ImageBuildes
UPSTREAM_URL = "https://mirrors.tuna.tsinghua.edu.cn/openwrt"

# where to store created images
STORE_PATH = Path.cwd() / "public/store/"

# where to store JSON files
JSON_PATH = Path.cwd() / "public/json/v1/"

# maximum custom rootfs size
MAX_CUSTOM_ROOTFS_SIZE_MB = 1024

# manual mapping of package ABI changes
MAPPING_ABI = {"libubus20191227": "libubus"}

# External repositories to allow
REPOSITORY_ALLOW_LIST = [
    "https://mirrors.tuna.tsinghua.edu.cn/openwrt",
    "http://mirrors.tuna.tsinghua.edu.cn/openwrt",
    "https://mirror.nju.edu.cn/openwrt",
    "http://mirror.nju.edu.cn/openwrt",
]

# connection string for Redis
REDIS_URL = "redis://localhost:6379"

# run jobs in worker processes or on the server (for testing)
# ASYNC_QUEUE = True

# allow users to add a boot script to the images
# ALLOW_DEFAULTS = False

# definition of branches, see and use branches.yml instead (unless testing)
# BRANCHES = {}

# what branches.yml file to load
# BRANCHES_FILE = "./branches.yml"

# where to downlaod the images from
UPSTREAM_PATH = "https://mirror.nju.edu.cn/openwrt"

# token used to trigger an update of targets
# if an empty string is set, the update happens periodically
UPDATE_TOKEN=""

# base container for the imagebuilder
# BASE_CONTAINER = "ghcr.io/openwrt/imagebuilder"
