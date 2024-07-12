import json

class sm_logic_lib():
	id_count = 0
	id_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	def logic_gate(pos_x, pos_y, pos_z, id, input=None, color="222222", rot_x=0, rot_z=0, type=0):
	    print(json.dumps({'color': color, 'controller': {'active': False, 'controllers': [input], 'id': sm_logic_lib.id_count, 'joints': None, 'mode': type}, 'pos': {'x': pos_x, 'y': pos_y, 'z': pos_z}, 'shapeId': "9f0f56e8-2c31-4d83-996c-d00a9b296c3f", 'xaxis': rot_x, 'zaxis': rot_z}, indent=3))
	    sm_logic_lib.id_list[id] = sm_logic_lib.id_count
	    sm_logic_lib.id_count += 1	    
controllers = [{"id": 1},{"id": 3},{"id": 4},{"id": 5}]
for i in range(2):
	sm_logic_lib.logic_gate(0, 0, 0, i, controllers)
print(sm_logic_lib.id_list)
