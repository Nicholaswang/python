def info(object,spacing=10,collapse=1):
    """Print methods and doc string.
        Takes module,class,list,dictionary,or string."""
        methodlist=[method for method in dir(object) if callable(getattr(object,method))]
        ProcessFunc=collapse and (lambda s:"".join(s.split())
