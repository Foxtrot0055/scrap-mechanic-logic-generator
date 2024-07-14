import sm_logic_lib as sm

def full_adder(pos_x, pos_y, pos_z, carry_out):
    cout = sm.make.logic_gate(pos_x, pos_y, pos_z, [carry_out], [0,0], 1)
    s = sm.make.logic_gate(pos_x, pos_y+1, pos_z, None, [0,0], 2)
    
    ab = sm.make.logic_gate(pos_x+1,pos_y,pos_z,[cout])
    ac = sm.make.logic_gate(pos_x+1,pos_y+1,pos_z, [cout])
    bc = sm.make.logic_gate(pos_x+1,pos_y+2,pos_z, [cout])

    a = sm.make.logic_gate(pos_x+2,pos_y,pos_z,[ab, ac])
    b = sm.make.logic_gate(pos_x+2,pos_y+1,pos_z,[ab, bc])
    cin = sm.make.logic_gate(pos_x+2,pos_y+2,pos_z,[ac, bc])

    return cin

def rc_adder(pos_x, pos_y, pos_z, bitwidth):
    cin = None
    for bit in range(bitwidth):
        cin = full_adder(pos_x, pos_y+bit*3, pos_z, cin)

rc_adder(0,0,0,8)
sm.make.print()
