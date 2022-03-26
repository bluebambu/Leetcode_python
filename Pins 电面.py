from collections import defaultdict
from queue import PriorityQueue
from typing import List
from collections import deque
from XiangUtils.xiangUtils import TreeNode, Tree, lvlOrder, Node

ID_PLACEHOLDER = '<ID>'

class Node:
    def __init__(self):
        self.children = {}
        self.endpointName = None


class PrefixTree:
    def __init__(self):
        self.root = Node()

    def addPattern(self, url: str, endpoint: str):
        parsed = self.parseUrl(url)

        # concate all elem
        self.addPatternNode(parsed, endpoint)

    def parseUrl(self, url: str):
        # parse the method and url path
        method, path = url.split(' ')
        # parse the path elem
        paths = path.split('/')

        return [method] + paths

    def addPatternNode(self, words: List[str], endpoint: str):
        cur_node = self.root

        for w in words:
            if w not in cur_node.children:
                cur_node.children[w] = Node()

            cur_node = cur_node.children[w]

        cur_node.endpointName = endpoint

    def searchUrl(self, url: str):
        parsed: List[str] = self.parseUrl(url)

        return self.searchUrlNode(parsed)

    def searchUrlNode(self, words: List[str]):
        cur_node: Node = self.root

        for w in words:
            # w might be GET, threads, 232adfwef. won't be PLACEHOLDER
            next_node = None

            # if words exceed the pattern range, then there is no children nodes
            if not cur_node.children:
                return ''

            # if cur_node don't have <ID>, then we can not auto regard unkown words as <ID>
            if ID_PLACEHOLDER in cur_node.children:
                if w not in cur_node.children:
                    next_node = cur_node.children[ID_PLACEHOLDER]
                else:
                    next_node = cur_node.children[w]
            else:
                if w not in cur_node.children:
                    return ''
                else:
                    next_node = cur_node.children[w]

            cur_node = next_node

        return cur_node.endpointName


PATTERN = {
'GET /users'                   :'get_all_users',
'GET /users/<ID>'              :'get_user',
'GET /users/<ID>/preferences'  :'get_user_preferences',
'GET /users/<ID>/<ID>'         :'get_user_posts_in_thread',
'GET /thread/<ID>'             :'get_thread',
'GET /thread/<ID>/comments'    :'get_thread_comments',
'GET /thread/<ID>/likes'       :'get_thread_likes',
'POST /thread'                 :'create_thread',
'DELETE /comments/<ID>'        :'delete_comment',
}


class Solution:
    def __init__(self):
        self.tree = PrefixTree()
        self.load_all_pattern(PATTERN)

    def getEndpointName(self, url: str):
        return self.tree.searchUrl(url)

    def load_all_pattern(self, pattern: map):
        for k in pattern:
            v = pattern[k]
            self.tree.addPattern(k, v)


s=Solution()
r = s.getEndpointName("GET /users/thisuseridlookslikewords/preferences")
print(r)
r = s.getEndpointName("GET /users22222/thisuseridlookslikewords/preferences")
print(r)
