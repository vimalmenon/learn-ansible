
def check_colors(value):
    return True if value == "red" else False


class TestModule(object):
    def tests(self):
        return {
            "color": check_colors
        }
