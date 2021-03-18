while True:
    print('Please paste your binary that needs translated. No spaces/strings')
    try:
        bin = input('')
    except ValueError as err:
        print(err)
    output = int(bin, 2)
    print('\n')
    print(output)