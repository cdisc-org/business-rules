import inspect

def fn_name_to_pretty_label(name):
    return ' '.join([w.title() for w in name.split('_')])

def export_rule_data(variables, actions):
    """ export_rule_data is used to export all information about the
    variables, actions, and operators to the client. This will return a
    dictionary with three keys:
    - variables: a list of all available variables along with their label, type and options
    - actions: a list of all actions along with their label and params
    - variable_type_operators: a dictionary of all field_types -> list of available operators
    """
    from . import operators
    actions_data = actions.get_all_actions()
    variables_data = variables.get_all_variables()
    variable_type_operators = {}
    for variable_class in inspect.getmembers(operators, lambda x: getattr(x, 'export_in_rule_data', False)):
        variable_type = variable_class[1] # getmembers returns (name, value)
        variable_type_operators[variable_type.name] = variable_type.get_all_operators()

    return {"variables": variables_data,
            "actions": actions_data,
            "variable_type_operators": variable_type_operators}
