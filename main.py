'''
Script to search for administration panels on provided URLs.
'''

from parchmentseeker import ParchmentSeeker


if __name__ == '__main__':
    domains = [

    ]

    pf = ParchmentSeeker(urls=domains)
    try:
        pf.request()
        print(f'Hosts founded: {pf.founded}')

    except ValueError as error:
        print(error)
