def compute_arm_config(link1_length,link2_length,joint0_angle,joint1_angle):
    joint1_x = link1_length*cos(joint0_angle)
    joint1_y = link1_length*sin(joint0_angle)
    p2_x = joint1_x + link2_length*cos(joint0_angle+joint1_angle)
    p2_y = joint1_y + link2_length*sin(joint0_angle + joint1_angle)
    return joint1_x,joint1_y,p2_x,p2_y