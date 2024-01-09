def stdin(*ask:str, exit_safe=True, ctrl_c_exit=True):
    concat = str()
    inp_=str()
    for i in ask:
        concat+=i
    if exit_safe:
        try: inp_ = input(concat)
        except KeyboardInterrupt: exit(0) if ctrl_c_exit else ''
        except EOFError: exit(0) if ctrl_c_exit else ''
        except ValueError: exit(0) if ctrl_c_exit else ''
    else:
        inp_ = input(concat)
    return inp_