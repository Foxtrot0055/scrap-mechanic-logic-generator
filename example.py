import sm_logic_lib as sm

for i in range(5):
    if i<4: input = [i+1]
    sm.make.logic_gate(i,0,0,input)
sm.make.print()

# {
#    "bodies": [
#       {
#          "childs": [
#             {
#                "color": "222222",
#                "controller": {
#                   "active": false,
#                   "controllers": [
#                      {
#                         "id": 1
#                      }
#                   ],
#                   "id": 0,
#                   "joints": null,
#                   "mode": 0
#                },
#                "pos": {
#                   "x": 0,
#                   "y": 0,
#                   "z": 0
#                },
#                "shapeId": "9f0f56e8-2c31-4d83-996c-d00a9b296c3f",
#                "xaxis": 0,
#                "zaxis": 0
#             },
#             {
#                "color": "222222",
#                "controller": {
#                   "active": false,
#                   "controllers": [
#                      {
#                         "id": 2
#                      }
#                   ],
#                   "id": 1,
#                   "joints": null,
#                   "mode": 0
#                },
#                "pos": {
#                   "x": 1,
#                   "y": 0,
#                   "z": 0
#                },
#                "shapeId": "9f0f56e8-2c31-4d83-996c-d00a9b296c3f",
#                "xaxis": 0,
#                "zaxis": 0
#             },
#             {
#                "color": "222222",
#                "controller": {
#                   "active": false,
#                   "controllers": [
#                      {
#                         "id": 3
#                      }
#                   ],
#                   "id": 2,
#                   "joints": null,
#                   "mode": 0
#                },
#                "pos": {
#                   "x": 2,
#                   "y": 0,
#                   "z": 0
#                },
#                "shapeId": "9f0f56e8-2c31-4d83-996c-d00a9b296c3f",
#                "xaxis": 0,
#                "zaxis": 0
#             },
#             {
#                "color": "222222",
#                "controller": {
#                   "active": false,
#                   "controllers": [
#                      {
#                         "id": 4
#                      }
#                   ],
#                   "id": 3,
#                   "joints": null,
#                   "mode": 0
#                },
#                "pos": {
#                   "x": 3,
#                   "y": 0,
#                   "z": 0
#                },
#                "shapeId": "9f0f56e8-2c31-4d83-996c-d00a9b296c3f",
#                "xaxis": 0,
#                "zaxis": 0
#             },
#             {
#                "color": "222222",
#                "controller": {
#                   "active": false,
#                   "controllers": [
#                      {
#                         "id": 4
#                      }
#                   ],
#                   "id": 4,
#                   "joints": null,
#                   "mode": 0
#                },
#                "pos": {
#                   "x": 4,
#                   "y": 0,
#                   "z": 0
#                },
#                "shapeId": "9f0f56e8-2c31-4d83-996c-d00a9b296c3f",
#                "xaxis": 0,
#                "zaxis": 0
#             }
#          ]
#       }
#    ],
#    "version": 4
# }
