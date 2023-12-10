range_list = list()


def rangeIntializer(startR: int, endR: int, segments: int):
    init_range = startR
    end_range = endR
    diff_range = endR - startR
    if diff_range % 2 == 0:
        segment_steps = int(diff_range / segments)
    else:
        segment_steps = int(diff_range / segments) + 1

    
    for i in range(0, segments):
        if i == 0:
            s_range_temp = init_range
            e_range_temp = s_range_temp + segment_steps
            range_list.append([s_range_temp, e_range_temp])
        elif i == segments - 1:
            range_list.append([e_range_temp, end_range])
        else:
            s_range_temp = e_range_temp
            e_range_temp = s_range_temp + segment_steps
            range_list.append([s_range_temp, e_range_temp])
    return range_list








