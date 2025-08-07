import sys
import json
import base64

# 读取原始输入
raw_input = sys.stdin.read()

# 方法1：嵌套存储（推荐）
wrapped = {"original_payload": json.loads(raw_input)}

# 方法2：或转为Base64编码（防冲突）
# wrapped = {"data_base64": base64.b64encode(raw_input.encode()).decode()}

print(json.dumps(wrapped))
