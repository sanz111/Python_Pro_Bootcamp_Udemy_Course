import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_NAME = "rosling"
PIXELA_TOKEN = "jfudsjklnfdiwoqfbdjksfad"
GRAPH_ID = "graph1"
headers ={
    "X-USER-TOKEN": PIXELA_TOKEN
}

# step 1：创建一个账户
# API 文档：https://docs.pixe.la/entry/post-user
# 注：token 和 username 都是自己随便写的，只要运行过一次就已经在服务器注册了。再运行的话会显示账户已经存在。

# user_params = {
#     "token": PIXELA_TOKEN,
#     "username": USER_NAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.json())

# step 2：创建图表 create a graph definition
# API 文档：https://docs.pixe.la/entry/post-graph

# graph_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "sora"
# }

# response = requests.post(url=graph_endpoint, json=graph_config,headers=headers)
# print(response.json())

# Step 3：获取图表 Get the graph
# 链接地址： https://pixe.la/v1/users/{user_name}/graphs/{graph_name}.html

# Step 4：向图表中添加数值 Post value to the graph
# API 文档：https://docs.pixe.la/entry/post-pixel
# graph_post_value_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}"
#
# today = datetime.now()  # 指定今天
# today = datetime(year=2022, month=1, day=5)  # 指定日期
#
# today_date = today.strftime("%Y%m%d")
# print(today_date)
#
# pixel_data = {
#     "date":today.strftime("%Y%m%d"),
#     "quantity":"0.5",
# }
# headers ={
#     "X-USER-TOKEN": PIXELA_TOKEN
# }
# response = requests.post(url=graph_post_value_endpoint, headers=headers, json=pixel_data)
# print(response.json())

# Step 6：更新图表中的数值 Update value to the graph
# API 文档：https://docs.pixe.la/entry/put-pixel

# update_date = datetime(year=2022, month=1,day=6)
# graph_update_value_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{update_date.strftime('%Y%m%d')}"
# new_pixel_data = {
#     "quantity":"13"
# }
# response = requests.put(url=graph_update_value_endpoint, headers=headers, json=new_pixel_data)
# print(response.json())

# Step 6：删除图表中的数值 Delete value to the graph
# API 文档：https://docs.pixe.la/entry/delete-pixel

update_date = datetime(year=2022, month=1, day=5)
graph_delete_value_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{update_date.strftime('%Y%m%d')}"

response = requests.delete(url=graph_delete_value_endpoint,headers=headers)
print(response.json())