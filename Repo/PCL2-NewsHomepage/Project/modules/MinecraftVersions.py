from homepagebuilder.interfaces import Logger
import requests
import json
import re

LAUNCHER_MANIFSET_URL = 'https://piston-meta.mojang.com/mc/game/version_manifest.json'
MANIFSET = None
VERSIONS_DICT = None
FULL_VERSIONS = None
LATEST_VERSIONS = None

logger = Logger("VersionScript")

def fetch_manifset():
    try:
        response = requests.get(LAUNCHER_MANIFSET_URL,timeout=10000)
        return json.loads(response.content)
    except Exception as e:
        logger.warning("加载 MC 版本列表失败")
        logger.exception(e)
        return {}

def get_manifset():
    global MANIFSET
    if not MANIFSET:
        MANIFSET = fetch_manifset()
    return MANIFSET

def init_version_dict():
    global LATEST_VERSIONS,FULL_VERSIONS,VERSIONS_DICT
    VERSIONS_DICT = {}
    LATEST_VERSIONS = {'snapshot':None,'release':None}
    manifset = get_manifset()
    LATEST_VERSIONS.update(manifset['latest'])
    FULL_VERSIONS = manifset.get('versions')
    for version in FULL_VERSIONS:
        VERSIONS_DICT[version['id']] = version
    if get_version_type(LATEST_VERSIONS["snapshot"]) == 'release':
        LATEST_VERSIONS["snapshot"] = None
    logger.info(f'最新快照版:{LATEST_VERSIONS.get("snapshot")}; 最新正式版:{LATEST_VERSIONS["release"]}')

def get_latest(version_type = 'all',version_rank = -1):
    global LATEST_VERSIONS
    if not LATEST_VERSIONS:
        init_version_dict()
    version_rank = int(version_rank)
    if version_rank <= 0:
        if(version_type == 'all'):
            if latest_snapshot := LATEST_VERSIONS.get('snapshot'):
                return latest_snapshot
            else:
                return LATEST_VERSIONS['release']
        return LATEST_VERSIONS.get(version_type)
    count = version_rank
    for version in FULL_VERSIONS:
        if version['type'] == version_type:
            count -= 1
            if count == 0:
                return version['id']
    return ''

def get_server_jar(version_id):
    global VERSIONS_DICT
    if not (ver_info := VERSIONS_DICT.get(version_id)):
        return None
    response = requests.get(ver_info['url'],timeout=10000)
    return json.loads(response.content)['downloads']['server']['url']

SNAPSHOT_PATTERN = re.compile(r'^[0-9]{2}[w|W][0-9]{2}[A-Fa-f]$')
PRE_RELEASE_PATTERN = re.compile(r'^.*-pre[0-9]+$')
RELEASE_CANDIDATE_PATTERN = re.compile(r'^.*-rc[0-9]+$')
RELEASE_PATTERN = re.compile(r'^1\.[0-9]+(\.[0-9]+)?$')

def get_version_type(version_id):
    '''获取版本类型'''
    if re.match(SNAPSHOT_PATTERN,version_id):
        return 'snapshot'
    if re.match(PRE_RELEASE_PATTERN,version_id):
        return 'pre_release'
    if re.match(RELEASE_CANDIDATE_PATTERN,version_id):
        return 'release_candidate'
    if re.match(RELEASE_PATTERN,version_id):
        return 'release'
    return 'other'
