# ---------------------------------------------------------game

fps = 60
screen_width = 400
screen_height = 220
# ---------------------------------------------------------Hit boxes
mario_height = 24
mario_width = 16
NPCs_height = 16
NPCS_width = 16
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
s_mario_stop=(0,80,0,16,24)
s_mario_stop_l=(0,80,0,-16,24)
s_mario_jumping_r = (0,64,0,16,24)
s_mario_jumping_l = (0,64,0,-16,24)

# ---------------------------------------------------------Turtles
s_turtle_standing = (0, 0, 24, 16, 16)
s_turtle_standing_l = (0, 0, 24, -16, 16)
s_turtle_walking_r1 = (0, 16, 24, 16, 16)
s_turtle_walking_r2 = (0, 32, 24, 16, 16)
s_turtle_walking_l1 = (0, 16, 24, -16, 16)
s_turtle_walking_l2 = (0, 32, 24, -16, 16)
s_turtle_lookback_r = (0, 48, 24, 16, 16)
s_turtle_lookback_l = (0, 48, 24, -16, 16)
s_turtle_die_r1 = (0, 64, 24, 16, 16)
s_turtle_die_r2 = (0, 80,24, 16, 16)
s_turtle_die_r3 = (0, 96, 24, 16, 16)
s_turtle_die_l1 = (0, 64, 24, -16, 16)
s_turtle_die_l2 = (0, 80, 24, -16, 16)
s_turtle_die_l3 = (0, 96, 24, -16, 16)

s_redturtle_standing = (0, 0, 128, 16, 16)
s_redturtle_standing_l = (0, 0, 128, -16, 16)
s_redturtle_walking_r1 = (0, 16, 128, 16, 16)
s_redturtle_walking_r2 = (0, 32, 128, 16, 16)
s_redturtle_walking_l1 = (0, 16, 128, -16, 16)
s_redturtle_walking_l2 = (0, 32, 128, -16, 16)
s_redturtle_lookback_r = (0, 48, 128, 16, 16)
s_redturtle_lookback_l = (0, 48, 128, -16, 16)
s_redturtle_die_r1 = (0, 64, 128, 16, 16)
s_redturtle_die_r2 = (0, 80,128, 16, 16)
s_redturtle_die_r3 = (0, 96, 128, 16, 16)
s_redturtle_die_l1 = (0, 64, 128, -16, 16)
s_redturtle_die_l2 = (0, 80, 128, -16, 16)
s_redturtle_die_l3 = (0, 96, 128, -16, 16)

# ---------------------------------------------------------Crabs
s_crab_standing = (0, 0, 40, 16, 16)
s_crab_walking_r1 = (0, 16, 40, 16, 16)
s_crab_walking_r2 = (0, 32, 40, 16, 16)
s_crab_walking_r3 = (0, 48, 40, 16, 16)
s_crab_walking_l1 = (0, 16, 40, -16, 16)
s_crab_walking_l2 = (0, 32, 40, -16, 16)
s_crab_walking_l3 = (0, 48, 40, -16 , 16)
s_crab_lookback_r1 = (0, 64, 40, 16, 16)
s_crab_lookback_r2 = (0, 80, 40, 8, 16)
s_crab_lookback_l1 = (0, 64, 40, -16, 16)
s_crab_lookback_l2 = (0, 80, 40, -8, 16)
s_crab_angry_1 = (0, 88, 40, 16, 16)
s_crab_angry_2 = (0, 104, 40, 16, 16)
s_crab_angry_3 = (0, 120, 40, 16, 16)
s_crab_angry_4 = (0, 136, 40, 16, 16)
s_crab_die_1 = (0, 152, 40, 16, 16)
s_crab_die_2 = (0, 168, 40, 16, 16)

s_greencrab_standing = (0, 0, 144, 16, 16)
s_greencrab_walking_r1 = (0, 16, 144, 16, 16)
s_greencrab_walking_r2 = (0, 32, 144, 16, 16)
s_greencrab_walking_r3 = (0, 48, 144, 16, 16)
s_greencrab_walking_l1 = (0, 16, 144, -16, 16)
s_greencrab_walking_l2 = (0, 32, 144, -16, 16)
s_greencrab_walking_l3 = (0, 48, 144, -16 , 16)
s_greencrab_lookback_r1 = (0, 64, 144, 16, 16)
s_greencrab_lookback_r2 = (0, 80, 144, 8, 16)
s_greencrab_lookback_l1 = (0, 64, 144, -16, 16)
s_greencrab_lookback_l2 = (0, 80, 144, -8, 16)
s_greencrab_angry_1 = (0, 88, 144, 16, 16)
s_greencrab_angry_2 = (0, 104, 144, 16, 16)
s_greencrab_angry_3 = (0, 120, 144, 16, 16)
s_greencrab_angry_4 = (0, 136, 144, 16, 16)
s_greencrab_die_1 = (0, 152, 144, 16, 16)
s_greencrab_die_2 = (0, 168, 144, 16, 16)

s_bluecrab_standing = (0, 0, 160, 16, 16)
s_bluecrab_walking_r1 = (0, 16, 160, 16, 16)
s_bluecrab_walking_r2 = (0, 32, 160, 16, 16)
s_bluecrab_walking_r3 = (0, 48, 160, 16, 16)
s_bluecrab_walking_l1 = (0, 16, 160, -16, 16)
s_bluecrab_walking_l2 = (0, 32, 160, -16, 16)
s_bluecrab_walking_l3 = (0, 48, 160, -16 , 16)
s_bluecrab_lookback_r1 = (0, 64, 160, 16, 16)
s_bluecrab_lookback_r2 = (0, 80, 160, 8, 16)
s_bluecrab_lookback_l1 = (0, 64, 160, -16, 16)
s_bluecrab_lookback_l2 = (0, 80, 160, -8, 16)
s_bluecrab_angry_1 = (0, 88, 160, 16, 16)
s_bluecrab_angry_2 = (0, 104, 160, 16, 16)
s_bluecrab_angry_3 = (0, 120, 160, 16, 16)
s_bluecrab_angry_4 = (0, 136, 160, 16, 16)
s_bluecrab_die_1 = (0, 152, 160, 16, 16)
s_bluecrab_die_2 = (0, 168, 160, 16, 16)



# ---------------------------------------------------------physics
collide = 3.91
friction = 0.8
friction_air = 0.1
gravity = 0.9
jump_force = 10
normal_v = 3
max_v_x = 3.5
max_v_y = 2
npc_v = 1
