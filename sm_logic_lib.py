import json

class make():
    blueprint = {'bodies': [{'childs': []}],'version': 4}
    id_count = 0
    
    def logic_gate(pos_x, pos_y, pos_z, type=0, output=None, rot=[2,1], color="222222"):
        output_list = []
        if output != None: 
            for id in output:
                output_list.append({'id': id})
        else: output_list=None
        make.blueprint['bodies'][0]['childs'].append({'color': color, 'controller': {'active': False, 'controllers': output_list, 'id': make.id_count, 'joints': None, 'mode': type}, 'pos': {'x': pos_x, 'y': pos_y, 'z': pos_z}, 'shapeId': "9f0f56e8-2c31-4d83-996c-d00a9b296c3f", 'xaxis': rot[0], 'zaxis': rot[1]})
        make.id_count += 1
        return make.id_count-1

    def connect(controller, destination):
        if make.blueprint['bodies'][0]['childs'][controller]['controller']['controllers'] == None:
            output_list = []
            for id in destination:
                output_list.append({'id': id})
            make.blueprint['bodies'][0]['childs'][controller]['controller']['controllers'] = output_list
        else:       
            for id in destination:
                make.blueprint['bodies'][0]['childs'][controller]['controller']['controllers'].append({'id': id})
    
    def print():
        print(json.dumps(make.blueprint, indent=3))
