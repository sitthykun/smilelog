from Consoler import Consoler


if __name__ == '__main__':
    # instant first object
    console1     = Consoler(
                    enable=True
    )

    # try to stop some actions, that will affect to call Consoler
    console1.disable([1, 3, 7])

    # instant second object
    console2     = Consoler(
                    enable=True
    )

    # first object
    # 1 value as dict
    console1.info('information', {'data':'my information'})
    # 2
    console1.warning('Warning', {'data': 'my warning message'})
    # 3
    console1.success('Success Title', {'data': 'it works'})
    # 4
    console2.error('My Error Title', {'data':'dangerous process'})
    # 5 with string
    console2.track('Track my code', 'Called me')
    # 6 with string
    console2.success('Success', 'Hello String')
