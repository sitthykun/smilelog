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
    # 1
    console1.info('information', {'data':'my content'})
    # 2
    console1.warning('Warning', {'data': 'my content'})
    # 3
    console1.success('Success', {'data': 'my content'})
    # second object
    # 4
    console2.info('information', {'data':'my content'})
    # 5
    console2.warning('Warning', {'data': 'my content'})
    # 6
    console2.success('Success', {'data': 'my content'})
    # 7
    console2.info('information', {'data':'my content'})
    # 8
    console2.warning('Warning', {'data': 'my content'})
    # 9
    console2.success('Success', {'data': 'my content'})
