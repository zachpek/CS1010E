def calc_poly(const_seq, var_poly):
    # Computes the value of a single variable polynomial function given the value of its single variable.
    # 
    # Args:
    #     const_seq (tuple[Union[float, int], ...]): Coefficients of polynomial from lowest (0) to highest order.
    #     var_poly (float or int): The value of the variable.
    # 
    # Returns:
    #     float or int: Computed value of polynomial for coefficients const_seq and value of variable var_poly.

    term = lambda order: const_seq[order] * var_poly ** order
    computed_value_poly = sum(map(term, range(len(const_seq))))
    return computed_value_poly