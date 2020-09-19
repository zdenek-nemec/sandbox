class BusinessLogicsCheck(object):
    """docstring for BusinessLogicsCheck"""
    def __init__(self):
        pass

    def check(self):
        return "not implemented"


class BashScriptsCheck(object):
    """docstring for BashScriptsCheck"""
    def __init__(self):
        pass

    def check(self):
        return "not implemented"


class GdcScriptsCheck(object):
    """docstring for GdcScriptsCheck"""
    def __init__(self):
        pass

    def check(self):
        return "not implemented"


class ReferenceTablesCheck(object):
    """docstring for ReferenceTablesCheck"""
    def __init__(self):
        pass

    def check(self):
        return "not implemented"


class PortalsCheck(object):
    """docstring for PortalsCheck"""
    def __init__(self):
        pass

    def check(self):
        return "not implemented"


def main():
    print("main: Started")

    print("Setup")
    business_logics_check = BusinessLogicsCheck()
    bash_scripts_check = BashScriptsCheck()
    gdc_scripts_check = GdcScriptsCheck()
    reference_tables_check = ReferenceTablesCheck()
    portals_check = PortalsCheck()

    print("Business logics check - %s" % business_logics_check.check())
    print("Bash scripts check - %s" % bash_scripts_check.check())
    print("GDC scripts check - %s" % gdc_scripts_check.check())
    print("Reference tables check - %s" % reference_tables_check.check())
    print("Portals check - %s" % portals_check.check())

    print("main: Finished")


if __name__ == "__main__":
    main()
