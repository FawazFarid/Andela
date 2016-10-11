def data_type(arg):
  if isinstance(arg, str):
    return len(arg)
  elif arg is None:
    return 'no value'
  elif isinstance(arg, bool):
    return arg
  elif isinstance(arg, int):
    if arg < 100:
      return 'less than 100'
    elif arg == 100:
      return 'equal to 100'
    elif arg > 100:
      return 'more than 100'
  elif isinstance(arg, list):
    return arg[2] if len(arg) > 2 else None