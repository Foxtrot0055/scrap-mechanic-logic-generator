import sm_logic_lib as sm

def full_adder(pos_x, pos_y, pos_z, cin_id):
    a = sm.make.logic_gate(pos_x, pos_y, pos_z)
    b = sm.make.logic_gate(pos_x, pos_y+1, pos_z)
    cin = sm.make.logic_gate(pos_x, pos_y+2, pos_z, [cin_id])

    d = sm.make.logic_gate(pos_x+2, pos_y+2, pos_z,[a,b,cin],"222222",0,0,2)
    ab = sm.make.logic_gate(pos_x+1, pos_y+1, pos_z, [a, b]) 
    ac = sm.make.logic_gate(pos_x+1, pos_y, pos_z, [a, cin]) 
    bc = sm.make.logic_gate(pos_x+1,pos_y, pos_z, [b, cin])

    cout = sm.make.logic_gate(pos_x+2, pos_y+1, pos_z, [ab, ac, bc], "222222", 0, 0, 1) 
    return cout

def rc_adder(pos_x, pos_y, pos_z, bitwidth):
    cout = sm.make.logic_gate(pos_x,pos_y+3,pos_z)
    for bit in range(bitwidth):
        cout = full_adder(pos_x, pos_y+-3*bit, pos_z, cout)

rc_adder(0, 0, 0, 8)
sm.make.print()
