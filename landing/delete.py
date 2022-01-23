import requests

token = "EAAC9L2YkDo0BAMZCDYWoSOEkjBUlWUZBHZCdXZC59LGtex08IFQb0hxquScZCQKxmnwmzAciahxh1x8iEsmXZAq2pAzpn3moPAJIF14VG1IplUR5aMIpLG8iNZBY8ZBkRGKeued8XDSpLyanFrB5IV6dtoDDLhSMeFZCbxcfuDruXVPeF4pLd8eIY7ZCPjEYOJkAMso5Tmw11LA93ax1V8M4XZCs4GI7fuzibV53FEAj4A51QviGUEZBrfan"
group = 1387991968282905

# all_posts= requests.get(f"https://graph.facebook.com/v12.0/1387991968282905/feed?access_token={token}")
filtered_posts = requests.get(f"https://graph.facebook.com/v12.0/{group}/feed?access_token={token}&limit=100&since=2021-12-07")

print(filtered_posts.json())
