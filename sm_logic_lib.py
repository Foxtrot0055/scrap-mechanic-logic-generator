import json

class make():
    blueprint = {'bodies': [{'childs': [None,None,None,None,None]}]}
    id_count = 0
    def logic_gate(pos_x, pos_y, pos_z, input=None, color="222222", rot_x=0, rot_z=0, type=0):
        make.blueprint['bodies'][0]['childs'][make.id_count] = {'color': color, 'controller': {'active': False, 'controllers': input, 'id': make.id_count, 'joints': None, 'mode': type}, 'pos': {'x': pos_x, 'y': pos_y, 'z': pos_z}, 'shapeId': "9f0f56e8-2c31-4d83-996c-d00a9b296c3f", 'xaxis': rot_x, 'zaxis': rot_z}
        make.id_count += 1
    def print():
        print(json.dumps(make.blueprint, indent=3))
