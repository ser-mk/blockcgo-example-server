from collections import defaultdict
import statistics

data = """


[GIN] 2024/03/24 - 19:48:14 | 200 |     136.785µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     116.281µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     131.625µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     121.736µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     111.738µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     108.618µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     113.654µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     110.151µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     118.284µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     108.142µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     112.044µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     106.433µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     107.692µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     105.787µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     118.648µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     118.757µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     109.093µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     109.935µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     115.632µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     116.914µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     113.537µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     123.477µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     116.305µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     110.053µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     142.756µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     108.182µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     109.382µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     111.057µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     108.224µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     110.297µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     105.264µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     110.023µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     115.677µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     112.186µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     106.078µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     110.048µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     107.109µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      112.32µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     109.283µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     106.519µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     107.619µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      112.73µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     108.853µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     111.676µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     108.834µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     110.341µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     109.654µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     112.409µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     110.446µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      101.63µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     130.377µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     111.862µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     110.659µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     111.252µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     105.319µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     110.276µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     108.291µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     113.841µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     108.434µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     109.948µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     111.501µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     107.854µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     111.913µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     107.633µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     112.011µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     107.649µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     114.223µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     111.164µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     103.469µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     114.605µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     110.008µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     111.978µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      104.25µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     107.319µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     117.409µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      85.182µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      98.069µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     121.283µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     119.022µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      125.37µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     110.229µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     104.814µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |       87.18µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      85.772µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     128.318µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     102.806µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     128.288µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     121.962µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      84.752µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      84.996µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      87.004µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      90.031µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     123.311µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      81.511µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      81.468µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     104.568µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      80.836µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     102.658µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     104.084µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      90.436µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      84.436µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      92.835µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      85.749µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     101.014µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     100.192µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |     111.683µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      93.378µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      86.736µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      95.884µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      96.678µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:14 | 200 |      98.571µs |       127.0.0.1 | GET      "/cgo/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |     286.492µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |     235.177µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |     240.186µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |     239.671µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |     241.626µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |     237.306µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |     233.826µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      228.09µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |     235.412µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      80.948µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      81.463µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      80.294µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      78.622µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      78.138µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.948µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.826µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.794µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.371µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.686µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.313µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      75.854µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.247µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.878µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      75.792µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      79.193µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.819µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.277µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.702µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      75.338µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.396µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      75.481µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.109µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.453µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.566µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |        76.2µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.254µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.784µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      79.818µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      75.728µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.302µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.989µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.029µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.685µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.739µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.119µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      81.581µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.242µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.283µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.455µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.489µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      75.289µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.343µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      80.644µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.468µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.552µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.395µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.019µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |       77.18µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      75.923µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.367µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.462µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |       75.89µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.838µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.071µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.481µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.234µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.358µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.456µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      81.478µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.581µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.799µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.345µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.528µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.187µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.318µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.614µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      96.653µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      90.255µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |       78.46µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |       78.81µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      83.111µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.661µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      84.204µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |     122.121µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |     114.637µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |     114.669µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      79.062µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.864µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      78.361µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.547µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |        79.5µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.965µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.052µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      78.661µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |       77.13µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.587µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      99.608µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      77.045µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      78.342µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.842µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      79.882µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |     112.808µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      89.101µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      79.811µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      94.461µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |       77.24µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      78.002µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.775µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.739µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      78.255µs |       127.0.0.1 | GET      "/blockcall/49/1"
[GIN] 2024/03/24 - 19:48:17 | 200 |      76.702µs |       127.0.0.1 | GET      "/blockcall/49/1"



"""

times = defaultdict(list)

for line in data.strip().split('\n'):
    parts = line.split('|')
    time_str = parts[2].strip()
    time_val = float(time_str[:-2])  # remove 'µs' and convert to float
    request_type = parts[-1].strip()
    times[request_type].append(time_val)

for request_type, request_times in times.items():
    average_time = sum(request_times) / len(request_times)
    median_time = statistics.median(request_times)
    print(f"Request type: {request_type}, Average time: {average_time:.2f}µs, Median time: {median_time:.2f}µs")
