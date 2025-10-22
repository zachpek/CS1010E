def set_smooth(left, centre, right):
    # Returns a function which smoothes a wave based on left, centre and right parameters. All numbers in the final smoothed wave will be integers.
    # The returned function returns the original wave if the 3 parameters left, centre and right do not add up to 1.
    # Arguments are all integers or floats.

    if left + centre + right != 1:
        return lambda wave: wave
    
    def smoother(wave):
        wave_length = len(wave)
        for i in range(wave_length):
            if i == 0:
                smoothed_i = 0 + wave[i] * centre + wave[i + 1] * right
            elif i == wave_length - 1:
                smoothed_i = prev_elem * left + wave[i] * centre + 0
            else:
                smoothed_i = prev_elem * left + wave[i] * centre + wave[i + 1] * right
            prev_elem = wave[i]
            wave[i] = int(smoothed_i)
        return wave

    return smoother

def smooth_transformer(parameter_list, repetitive_list):
    # Produces a smoother which applies each smoother produced by the nth element of parameter_list the number of times specified in the nth element of repetitive_list.
    # parameter_list is a non-empty list of triplets, each of the triplets being a set of parameters for setting smoothing function
    # repetitive_list is a non-empty list of positive integers
    # parameter_list and repetitive_list are of the same length, m

    m = len(parameter_list)
    
    def smoother(wave):
        for i in range(m):
            left, centre, right = parameter_list[i]
            smoother = set_smooth(left, centre, right)
            for _ in range(repetitive_list[i]):
                wave = smoother(wave)
        return wave

    return smoother
