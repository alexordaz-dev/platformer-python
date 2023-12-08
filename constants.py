# ---------------------------------------------------------game

fps = 60
screen_width = 400
screen_height = 218
# ---------------------------------------------------------Hit boxes
mario_height = 24
mario_width = 16
ground_height = screen_height-220 + 204

# ---------------------------------------------------------Mario
s_mario_standing = (0, 0, 0, 16, 24)
s_mario_standing_l = (0, 0, 0, -16, 24)
s_mario_walking_r1 = (0, 16, 0, 16, 24)
s_mario_walking_r2 = (0, 32, 0, 16, 24)
s_mario_walking_r3 = (0, 48, 0, 16, 24)
s_mario_walking_l1 = (0, 16, 0, -16, 24)
s_mario_walking_l2 = (0, 32, 0, -16, 24)
s_mario_walking_l3 = (0, 48, 0, -16, 24)

# ---------------------------------------------------------physics
collide = 0.5
friction = 0.8
gravity = .25
jump_force = 5
normal_v = 3
max_v_x = 3.5
max_v_y = 2
npc_v = 1
